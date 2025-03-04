
ibm_storage_block -- Configure IBM Cloud 'ibm_storage_block' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_storage_block' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/storage_block

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.49.0
- Terraform v0.12.20



Parameters
----------

  allowed_ip_addresses (False, list, None)
    Allowed IP addresses


  tags (False, list, None)
    List of tags associated with the resource


  snapshot_capacity (False, int, None)
    Snapshot capacity in GB


  allowed_virtual_guest_ids (False, list, None)
    List of allowed virtual guest IDs


  allowed_hardware_ids (False, list, None)
    List of allowe hardware IDs


  type (True, str, None)
    (Required for new resource) Storage block type


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  iops (True, float, None)
    (Required for new resource) IOPS value required


  capacity (True, int, None)
    (Required for new resource) Storage block size


  notes (False, str, None)
    Additional note info


  hourly_billing (False, bool, False)
    Billing done hourly, if set to true


  os_format_type (True, str, None)
    (Required for new resource) OS formatr type


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

