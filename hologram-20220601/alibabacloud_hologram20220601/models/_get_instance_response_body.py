# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        instance: main_models.GetInstanceResponseBodyInstance = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code that is returned if the request failed.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The information about the instance.
        self.instance = instance
        # The request ID.
        self.request_id = request_id
        # The request result, which indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

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

        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

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

        if m.get('Instance') is not None:
            temp_model = main_models.GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        auto_renewal: str = None,
        cold_storage: int = None,
        commodity_code: str = None,
        compute_node_count: int = None,
        cpu: int = None,
        creation_time: str = None,
        disk: str = None,
        enable_hive_access: str = None,
        enable_ssl: bool = None,
        enable_serverless: bool = None,
        endpoints: List[main_models.GetInstanceResponseBodyInstanceEndpoints] = None,
        expiration_time: str = None,
        gateway_count: int = None,
        gateway_cpu: int = None,
        gateway_memory: int = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_owner: str = None,
        instance_status: str = None,
        instance_type: str = None,
        leader_instance_id: str = None,
        memory: int = None,
        region_id: str = None,
        replica_role: str = None,
        resource_group_id: str = None,
        storage_type: str = None,
        suspend_reason: str = None,
        tags: List[main_models.GetInstanceResponseBodyInstanceTags] = None,
        version: str = None,
        zone_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled.
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
        self.auto_renewal = auto_renewal
        # The cold storage capacity of the instance. Unit: GB. Standard SSD is used for hot storage, and HDD is used for cold storage.
        self.cold_storage = cold_storage
        # The commodity code.
        # 
        # Valid values:
        # 
        # *   hologram_maxcomputeAccelerate_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Lakehouse Acceleration Edition
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_combo_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Subscription
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_prepay_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Subscription
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_storage_dp_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Storage plan
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_postpay_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_postpay_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Pay-as-you-go
        # 
        #     <!-- -->
        # 
        # *   hologram_maxcomputeAccelerate_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Lakehouse Acceleration Edition
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_cu_dp_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Compute plan
        # 
        #     <!-- -->
        self.commodity_code = commodity_code
        # The number of compute nodes. In a typical configuration, a node has 16 CPU cores and 32 GB of memory.
        self.compute_node_count = compute_node_count
        # The number of CPU cores.
        self.cpu = cpu
        # The time when the instance was created.
        self.creation_time = creation_time
        # The amount of data that can be stored in the disk of the Standard storage class. Unit: GB.
        self.disk = disk
        # Indicates whether data lake acceleration is enabled.
        self.enable_hive_access = enable_hive_access
        self.enable_ssl = enable_ssl
        # EnableServerless
        self.enable_serverless = enable_serverless
        # The list of endpoints.
        self.endpoints = endpoints
        # The expiration time. This parameter is invalid for pay-as-you-go instances.
        self.expiration_time = expiration_time
        # The number of gateway nodes.
        self.gateway_count = gateway_count
        # The number of CPU cores of the gateway. Unit: core.
        self.gateway_cpu = gateway_cpu
        # The size of memory resources of the gateway. Unit: GB.
        self.gateway_memory = gateway_memory
        # The billing method of the instance.
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
        # The instance name. The instance name must be 2 to 64 characters in length.
        self.instance_name = instance_name
        # The owner of the instance.
        self.instance_owner = instance_owner
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
        # The memory size. Unit: GB.
        self.memory = memory
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # Disaster recovery instance role. 
        # * Active: Primary disaster recovery instance.
        # * Passive: Disaster tolerance instance.
        # * PreActive: Primary disaster recovery instance not yet in final state.
        self.replica_role = replica_role
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The storage type.
        # 
        # *   redundant: 3 copies
        # *   local: single copy
        self.storage_type = storage_type
        # The reason for the suspension.
        # 
        # Valid values:
        # 
        # *   Indebet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance has an overdue payment
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Manual
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance is manually suspended
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Overdue
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance has expired
        # 
        #     <!-- -->
        # 
        #     .
        self.suspend_reason = suspend_reason
        # The instance tag.
        self.tags = tags
        # The instance version.
        self.version = version
        # The ID of the zone where the instance resides.
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
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.compute_node_count is not None:
            result['ComputeNodeCount'] = self.compute_node_count

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.enable_hive_access is not None:
            result['EnableHiveAccess'] = self.enable_hive_access

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.enable_serverless is not None:
            result['EnableServerless'] = self.enable_serverless

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.gateway_count is not None:
            result['GatewayCount'] = self.gateway_count

        if self.gateway_cpu is not None:
            result['GatewayCpu'] = self.gateway_cpu

        if self.gateway_memory is not None:
            result['GatewayMemory'] = self.gateway_memory

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_owner is not None:
            result['InstanceOwner'] = self.instance_owner

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.leader_instance_id is not None:
            result['LeaderInstanceId'] = self.leader_instance_id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_role is not None:
            result['ReplicaRole'] = self.replica_role

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
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ComputeNodeCount') is not None:
            self.compute_node_count = m.get('ComputeNodeCount')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('EnableHiveAccess') is not None:
            self.enable_hive_access = m.get('EnableHiveAccess')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('EnableServerless') is not None:
            self.enable_serverless = m.get('EnableServerless')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.GetInstanceResponseBodyInstanceEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('GatewayCount') is not None:
            self.gateway_count = m.get('GatewayCount')

        if m.get('GatewayCpu') is not None:
            self.gateway_cpu = m.get('GatewayCpu')

        if m.get('GatewayMemory') is not None:
            self.gateway_memory = m.get('GatewayMemory')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceOwner') is not None:
            self.instance_owner = m.get('InstanceOwner')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('LeaderInstanceId') is not None:
            self.leader_instance_id = m.get('LeaderInstanceId')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaRole') is not None:
            self.replica_role = m.get('ReplicaRole')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SuspendReason') is not None:
            self.suspend_reason = m.get('SuspendReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetInstanceResponseBodyInstanceTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetInstanceResponseBodyInstanceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
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

class GetInstanceResponseBodyInstanceEndpoints(DaraModel):
    def __init__(
        self,
        alternative_endpoints: str = None,
        enabled: bool = None,
        endpoint: str = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The endpoint. This parameter is returned if both the AnyTunnel and SingleTunnel modes are enabled for an instance, and the instance is switched from the AnyTunnel mode to the SingleTunnel mode. In this case, two endpoints are returned.
        self.alternative_endpoints = alternative_endpoints
        # Indicates whether the network is enabled.
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
        #     .
        # 
        # *   VPCAnyTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     not supported by new instances
        # 
        #     <!-- -->
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
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the instance belongs.
        self.vpc_id = vpc_id
        # The ID of the instance that is deployed in the VPC.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alternative_endpoints is not None:
            result['AlternativeEndpoints'] = self.alternative_endpoints

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
        if m.get('AlternativeEndpoints') is not None:
            self.alternative_endpoints = m.get('AlternativeEndpoints')

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

