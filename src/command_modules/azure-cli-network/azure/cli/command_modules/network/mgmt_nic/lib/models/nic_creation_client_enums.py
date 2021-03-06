#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class networkSecurityGroupType(Enum):

    none = "none"
    existing_name = "existingName"
    existing_id = "existingId"


class privateIpAddressAllocation(Enum):

    dynamic = "dynamic"
    static = "static"


class privateIpAddressVersion(Enum):

    ipv4 = "ipv4"
    ipv6 = "ipv6"


class publicIpAddressType(Enum):

    none = "none"
    existing_name = "existingName"
    existing_id = "existingId"


class subnetType(Enum):

    existing_name = "existingName"
    existing_id = "existingId"


class useDnsSettings(Enum):

    true = "true"
    false = "false"


class DeploymentMode(Enum):

    incremental = "Incremental"
    complete = "Complete"
