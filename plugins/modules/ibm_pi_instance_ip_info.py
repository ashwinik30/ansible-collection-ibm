#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_pi_instance_ip_info
short_description: Retrieve IBM Cloud 'ibm_pi_instance_ip' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_pi_instance_ip' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.0
    - Terraform v0.12.20

options:
    ip:
        description:
            - None
        required: False
        type: str
    macaddress:
        description:
            - None
        required: False
        type: str
    pi_instance_name:
        description:
            - Server Name to be used for pvminstances
        required: True
        type: str
    pi_cloud_instance_id:
        description:
            - None
        required: True
        type: str
    network_id:
        description:
            - None
        required: False
        type: str
    type:
        description:
            - None
        required: False
        type: str
    external_ip:
        description:
            - None
        required: False
        type: str
    pi_network_name:
        description:
            - None
        required: True
        type: str
    ipoctet:
        description:
            - None
        required: False
        type: str
    zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environment
              variable 'IC_ZONE'.
        required: False
        type: str
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
    ('pi_instance_name', 'str'),
    ('pi_cloud_instance_id', 'str'),
    ('pi_network_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'ip',
    'macaddress',
    'pi_instance_name',
    'pi_cloud_instance_id',
    'network_id',
    'type',
    'external_ip',
    'pi_network_name',
    'ipoctet',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ip=dict(
        required=False,
        type='str'),
    macaddress=dict(
        required=False,
        type='str'),
    pi_instance_name=dict(
        required=True,
        type='str'),
    pi_cloud_instance_id=dict(
        required=True,
        type='str'),
    network_id=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    external_ip=dict(
        required=False,
        type='str'),
    pi_network_name=dict(
        required=True,
        type='str'),
    ipoctet=dict(
        required=False,
        type='str'),
    zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE'])),
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

    result = ibmcloud_terraform(
        resource_type='ibm_pi_instance_ip',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.8.0',
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
