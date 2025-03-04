#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_dns_glb_pool
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dns_glb_pool

short_description: Configure IBM Cloud 'ibm_dns_glb_pool' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_dns_glb_pool' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.49.0
    - Terraform v0.12.20

options:
    instance_id:
        description:
            - (Required for new resource) Instance Id
        required: True
        type: str
    name:
        description:
            - (Required for new resource) The unique identifier of a service instance.
        required: True
        type: str
    healthcheck_subnets:
        description:
            - Health check subnet crn of VSIs
        required: False
        type: list
        elements: str
    description:
        description:
            - Descriptive text of the load balancer pool
        required: False
        type: str
    enabled:
        description:
            - Whether the load balancer pool is enabled
        required: False
        type: bool
    notification_channel:
        description:
            - The notification channel,It is a webhook url
        required: False
        type: str
    healthcheck_region:
        description:
            - Health check region of VSIs
        required: False
        type: str
    healthy_origins_threshold:
        description:
            - The minimum number of origins that must be healthy for this pool to serve traffic
        required: False
        type: int
    origins:
        description:
            - (Required for new resource) Origins info
        required: True
        type: list
        elements: dict
    monitor:
        description:
            - The ID of the load balancer monitor to be associated to this pool
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
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
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
    ('instance_id', 'str'),
    ('name', 'str'),
    ('origins', 'list'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'instance_id',
    'name',
    'healthcheck_subnets',
    'description',
    'enabled',
    'notification_channel',
    'healthcheck_region',
    'healthy_origins_threshold',
    'origins',
    'monitor',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    instance_id=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    healthcheck_subnets=dict(
        required=False,
        elements='',
        type='list'),
    description=dict(
        required=False,
        type='str'),
    enabled=dict(
        required=False,
        type='bool'),
    notification_channel=dict(
        required=False,
        type='str'),
    healthcheck_region=dict(
        required=False,
        type='str'),
    healthy_origins_threshold=dict(
        required=False,
        type='int'),
    origins=dict(
        required=False,
        elements='',
        type='list'),
    monitor=dict(
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
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
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

    result = ibmcloud_terraform(
        resource_type='ibm_dns_glb_pool',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.49.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
