#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_en_destination_safari
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/en_destination_safari

short_description: Configure IBM Cloud 'ibm_en_destination_safari' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_en_destination_safari' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.49.0
    - Terraform v0.12.20

options:
    type:
        description:
            - (Required for new resource) The type of Destination type push_ios.
        required: True
        type: str
    description:
        description:
            - The Destination description.
        required: False
        type: str
    icon_32x32_2x:
        description:
            - The Certificate File.
        required: False
        type: str
    certificate:
        description:
            - (Required for new resource) The Certificate File.
        required: True
        type: str
    icon_16x16:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_16x16_content_type:
        description:
            - The Certificate File.
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The Destintion name.
        required: True
        type: str
    icon_32x32:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_128x128_2x:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_32x32_2x_content_type:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_128x128_content_type:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_128x128_2x_content_type:
        description:
            - The Certificate File.
        required: False
        type: str
    instance_guid:
        description:
            - (Required for new resource) Unique identifier for IBM Cloud Event Notifications instance.
        required: True
        type: str
    icon_16x16_2x:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_128x128:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_16x16_2x_content_type:
        description:
            - The Certificate File.
        required: False
        type: str
    icon_32x32_content_type:
        description:
            - The Certificate File.
        required: False
        type: str
    config:
        description:
            - Payload describing a destination configuration.
        required: False
        type: list
        elements: dict
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
    ('type', 'str'),
    ('certificate', 'str'),
    ('name', 'str'),
    ('instance_guid', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'type',
    'description',
    'icon_32x32_2x',
    'certificate',
    'icon_16x16',
    'icon_16x16_content_type',
    'name',
    'icon_32x32',
    'icon_128x128_2x',
    'icon_32x32_2x_content_type',
    'icon_128x128_content_type',
    'icon_128x128_2x_content_type',
    'instance_guid',
    'icon_16x16_2x',
    'icon_128x128',
    'icon_16x16_2x_content_type',
    'icon_32x32_content_type',
    'config',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('instance_guid', 'str'),
    ('destination_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'instance_guid',
    'destination_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    type=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    icon_32x32_2x=dict(
        required=False,
        type='str'),
    certificate=dict(
        required=False,
        type='str'),
    icon_16x16=dict(
        required=False,
        type='str'),
    icon_16x16_content_type=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    icon_32x32=dict(
        required=False,
        type='str'),
    icon_128x128_2x=dict(
        required=False,
        type='str'),
    icon_32x32_2x_content_type=dict(
        required=False,
        type='str'),
    icon_128x128_content_type=dict(
        required=False,
        type='str'),
    icon_128x128_2x_content_type=dict(
        required=False,
        type='str'),
    instance_guid=dict(
        required=False,
        type='str'),
    icon_16x16_2x=dict(
        required=False,
        type='str'),
    icon_128x128=dict(
        required=False,
        type='str'),
    icon_16x16_2x_content_type=dict(
        required=False,
        type='str'),
    icon_32x32_content_type=dict(
        required=False,
        type='str'),
    config=dict(
        required=False,
        elements='',
        type='list'),
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_en_destination_safari',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.49.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_en_destination_safari',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.49.0',
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
