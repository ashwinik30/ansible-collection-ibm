
ibm_pi_operations -- Configure IBM Cloud 'ibm_pi_operations' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_operations' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_operations

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.45.1
- Terraform v0.12.20



Parameters
----------

  pi_operation (True, str, None)
    (Required for new resource) PI instance operation type


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI Cloud instnce id


  pi_instance_name (True, str, None)
    (Required for new resource) PI instance Operation server name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

