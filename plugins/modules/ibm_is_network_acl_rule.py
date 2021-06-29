#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_network_acl_rule
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_network_acl_rule

short_description: Configure IBM Cloud 'ibm_is_network_acl_rule' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_network_acl_rule' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.27.0
    - Terraform v0.12.20

options:
    source:
        description:
            - (Required for new resource) The source CIDR block. The CIDR block 0.0.0.0/0 applies to all addresses.
        required: True
        type: str
    destination:
        description:
            - (Required for new resource) The destination CIDR block. The CIDR block 0.0.0.0/0 applies to all addresses.
        required: True
        type: str
    direction:
        description:
            - (Required for new resource) Direction of traffic to enforce, either inbound or outbound
        required: True
        type: str
    network_acl:
        description:
            - (Required for new resource) Network ACL id
        required: True
        type: str
    icmp:
        description:
            - None
        required: False
        type: list
        elements: dict
    name:
        description:
            - The user-defined name for this rule. Names must be unique within the network ACL the rule resides in. If unspecified, the name will be a hyphenated list of randomly-selected words.
        required: False
        type: str
    action:
        description:
            - (Required for new resource) Whether to allow or deny matching traffic
        required: True
        type: str
    tcp:
        description:
            - None
        required: False
        type: list
        elements: dict
    udp:
        description:
            - None
        required: False
        type: list
        elements: dict
    before:
        description:
            - The rule that this rule is immediately before. If absent, this is the last rule.
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    generation:
        description:
            - The generation of Virtual Private Cloud infrastructure
              that you want to use. Supported values are 1 for VPC
              generation 1, and 2 for VPC generation 2 infrastructure.
              If this value is not specified, 2 is used by default. This
              can also be provided via the environment variable
              'IC_GENERATION'.
        default: 2
        required: False
        type: int
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('source', 'str'),
    ('destination', 'str'),
    ('direction', 'str'),
    ('network_acl', 'str'),
    ('action', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'source',
    'destination',
    'direction',
    'network_acl',
    'icmp',
    'name',
    'action',
    'tcp',
    'udp',
    'before',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('network_acl', 'str'),
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'network_acl',
    'name',
]

TL_CONFLICTS_MAP = {
    'icmp': ['tcp', 'udp'],
    'tcp': ['icmp', 'udp'],
    'udp': ['icmp', 'tcp'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    source=dict(
        required=False,
        type='str'),
    destination=dict(
        required=False,
        type='str'),
    direction=dict(
        required=False,
        type='str'),
    network_acl=dict(
        required=False,
        type='str'),
    icmp=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    action=dict(
        required=False,
        type='str'),
    tcp=dict(
        required=False,
        elements='',
        type='list'),
    udp=dict(
        required=False,
        elements='',
        type='list'),
    before=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    generation=dict(
        type='int',
        required=False,
        fallback=(env_fallback, ['IC_GENERATION']),
        default=2),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    # VPC required arguments checks
    if module.params['generation'] == 1:
        missing_args = []
        if module.params['iaas_classic_username'] is None:
            missing_args.append('iaas_classic_username')
        if module.params['iaas_classic_api_key'] is None:
            missing_args.append('iaas_classic_api_key')
        if missing_args:
            module.fail_json(msg=(
                "VPC generation=1 missing required arguments: " +
                ", ".join(missing_args)))
    elif module.params['generation'] == 2:
        if module.params['ibmcloud_api_key'] is None:
            module.fail_json(
                msg=("VPC generation=2 missing required argument: "
                     "ibmcloud_api_key"))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_is_network_acl_rule',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.27.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_network_acl_rule',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.27.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
