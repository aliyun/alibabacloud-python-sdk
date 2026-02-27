# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        instance_list: List[main_models.ListInstancesResponseBodyInstanceList] = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The instances.
        self.instance_list = instance_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.ListInstancesResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstancesResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        creation_time: str = None,
        enable_hive_access: str = None,
        enable_ssl: str = None,
        endpoints: List[main_models.ListInstancesResponseBodyInstanceListEndpoints] = None,
        expiration_time: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        leader_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_type: str = None,
        suspend_reason: str = None,
        tags: List[main_models.ListInstancesResponseBodyInstanceListTags] = None,
        version: str = None,
        zone_id: str = None,
    ):
        # The commodity code, which is the same as that on the Billing Management page.
        self.commodity_code = commodity_code
        # The time when the cluster was created.
        self.creation_time = creation_time
        # Indicates whether lakehouse acceleration is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_hive_access = enable_hive_access
        self.enable_ssl = enable_ssl
        # The list of endpoints.
        self.endpoints = endpoints
        # The time when the cluster expires.
        self.expiration_time = expiration_time
        # The billing method of the instance. Valid values:
        # 
        # Valid values:
        # 
        # *   PostPaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   PrePaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     subscription
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_charge_type = instance_charge_type
        # The instance ID.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Suspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Allocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.instance_status = instance_status
        # The type of the instance.
        # 
        # Valid values:
        # 
        # *   Follower
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     read-only secondary instance
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     normal instance
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_type = instance_type
        # The ID of the primary instance.
        self.leader_instance_id = leader_instance_id
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.storage_type = storage_type
        # The reason for the suspension.
        self.suspend_reason = suspend_reason
        # The tags that are added to the resource.
        self.tags = tags
        # The version of the cluster.
        self.version = version
        self.zone_id = zone_id

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.enable_hive_access is not None:
            result['EnableHiveAccess'] = self.enable_hive_access

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.leader_instance_id is not None:
            result['LeaderInstanceId'] = self.leader_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.suspend_reason is not None:
            result['SuspendReason'] = self.suspend_reason

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EnableHiveAccess') is not None:
            self.enable_hive_access = m.get('EnableHiveAccess')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListInstancesResponseBodyInstanceListEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('LeaderInstanceId') is not None:
            self.leader_instance_id = m.get('LeaderInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SuspendReason') is not None:
            self.suspend_reason = m.get('SuspendReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListInstancesResponseBodyInstanceListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListInstancesResponseBodyInstanceListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListInstancesResponseBodyInstanceListEndpoints(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        endpoint: str = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        # Indicates whether the endpoint is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enabled = enabled
        # The endpoint.
        self.endpoint = endpoint
        # The network type.
        # 
        # Valid values:
        # 
        # *   VPCSingleTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     virtual private cloud (VPC)
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Intranet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     internal network
        # 
        #     <!-- -->
        # 
        # *   VPCAnyTunnel
        # 
        #     <!-- -->
        # 
        #     : This value is not supported by new instances
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Internet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Internet
        # 
        #     <!-- -->
        # 
        #     .
        self.type = type
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the VPC to which the instance belongs.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

