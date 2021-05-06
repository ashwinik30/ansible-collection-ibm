#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cos_bucket
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cos_bucket

short_description: Configure IBM Cloud 'ibm_cos_bucket' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cos_bucket' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.24.0
    - Terraform v0.12.20

options:
    endpoint_type:
        description:
            - public or private
        required: False
        type: str
        default: public
    retention_rule:
        description:
            - A retention policy is enabled at the IBM Cloud Object Storage bucket level. Minimum, maximum and default retention period are defined by this policy and apply to all objects in the bucket.
        required: False
        type: list
        elements: dict
    force_delete:
        description:
            - COS buckets need to be empty before they can be deleted. force_delete option empty the bucket and delete it.
        required: False
        type: bool
        default: True
    key_protect:
        description:
            - CRN of the key you want to use data at rest encryption
        required: False
        type: str
    region_location:
        description:
            - Region Location info.
        required: False
        type: str
    cross_region_location:
        description:
            - Cros region location info
        required: False
        type: str
    resource_instance_id:
        description:
            - (Required for new resource) resource instance ID
        required: True
        type: str
    storage_class:
        description:
            - (Required for new resource) Storage class info
        required: True
        type: str
    activity_tracking:
        description:
            - Enables sending log data to Activity Tracker and LogDNA to provide visibility into object read and write events
        required: False
        type: list
        elements: dict
    expire_rule:
        description:
            - Enable configuration expire_rule to COS Bucket after a defined period of time
        required: False
        type: list
        elements: dict
    bucket_name:
        description:
            - (Required for new resource) COS Bucket name
        required: True
        type: str
    single_site_location:
        description:
            - single site location info
        required: False
        type: str
    allowed_ip:
        description:
            - List of IPv4 or IPv6 addresses
        required: False
        type: list
        elements: str
    metrics_monitoring:
        description:
            - Enables sending metrics to IBM Cloud Monitoring.
        required: False
        type: list
        elements: dict
    archive_rule:
        description:
            - Enable configuration archive_rule (glacier/accelerated) to COS Bucket after a defined period of time
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
    ('resource_instance_id', 'str'),
    ('storage_class', 'str'),
    ('bucket_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'endpoint_type',
    'retention_rule',
    'force_delete',
    'key_protect',
    'region_location',
    'cross_region_location',
    'resource_instance_id',
    'storage_class',
    'activity_tracking',
    'expire_rule',
    'bucket_name',
    'single_site_location',
    'allowed_ip',
    'metrics_monitoring',
    'archive_rule',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('bucket_region', 'str'),
    ('bucket_type', 'str'),
    ('resource_instance_id', 'str'),
    ('bucket_name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'bucket_region',
    'bucket_type',
    'resource_instance_id',
    'bucket_name',
    'endpoint_type',
]

TL_CONFLICTS_MAP = {
    'region_location': ['cross_region_location', 'single_site_location'],
    'cross_region_location': ['region_location', 'single_site_location'],
    'single_site_location': ['region_location', 'cross_region_location'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    endpoint_type=dict(
        required=False,
        type='str'),
    retention_rule=dict(
        required=False,
        elements='',
        type='list'),
    force_delete=dict(
        required=False,
        type='bool'),
    key_protect=dict(
        required=False,
        type='str'),
    region_location=dict(
        required=False,
        type='str'),
    cross_region_location=dict(
        required=False,
        type='str'),
    resource_instance_id=dict(
        required=False,
        type='str'),
    storage_class=dict(
        required=False,
        type='str'),
    activity_tracking=dict(
        required=False,
        elements='',
        type='list'),
    expire_rule=dict(
        required=False,
        elements='',
        type='list'),
    bucket_name=dict(
        required=False,
        type='str'),
    single_site_location=dict(
        required=False,
        type='str'),
    allowed_ip=dict(
        required=False,
        elements='',
        type='list'),
    metrics_monitoring=dict(
        required=False,
        elements='',
        type='list'),
    archive_rule=dict(
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
        resource_type='ibm_cos_bucket',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.24.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cos_bucket',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.24.0',
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
