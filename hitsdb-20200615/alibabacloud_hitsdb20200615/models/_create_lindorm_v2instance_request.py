# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class CreateLindormV2InstanceRequest(DaraModel):
    def __init__(
        self,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        auto_renew_duration: str = None,
        auto_renewal: bool = None,
        capacity_storage_size: int = None,
        cloud_storage_size: int = None,
        cloud_storage_type: str = None,
        cluster_mode: str = None,
        cluster_pattern: str = None,
        duration: int = None,
        enable_capacity_storage: bool = None,
        engine_list: List[main_models.CreateLindormV2InstanceRequestEngineList] = None,
        instance_alias: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.arbiter_zone_id = arbiter_zone_id
        self.arch_version = arch_version
        self.auto_renew_duration = auto_renew_duration
        self.auto_renewal = auto_renewal
        self.capacity_storage_size = capacity_storage_size
        self.cloud_storage_size = cloud_storage_size
        self.cloud_storage_type = cloud_storage_type
        self.cluster_mode = cluster_mode
        self.cluster_pattern = cluster_pattern
        self.duration = duration
        self.enable_capacity_storage = enable_capacity_storage
        # This parameter is required.
        self.engine_list = engine_list
        self.instance_alias = instance_alias
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.primary_vswitch_id = primary_vswitch_id
        self.primary_zone_id = primary_zone_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_zone_id = standby_zone_id
        # This parameter is required.
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.engine_list:
            for v1 in self.engine_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id

        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id

        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.capacity_storage_size is not None:
            result['CapacityStorageSize'] = self.capacity_storage_size

        if self.cloud_storage_size is not None:
            result['CloudStorageSize'] = self.cloud_storage_size

        if self.cloud_storage_type is not None:
            result['CloudStorageType'] = self.cloud_storage_type

        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_pattern is not None:
            result['ClusterPattern'] = self.cluster_pattern

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.enable_capacity_storage is not None:
            result['EnableCapacityStorage'] = self.enable_capacity_storage

        result['EngineList'] = []
        if self.engine_list is not None:
            for k1 in self.engine_list:
                result['EngineList'].append(k1.to_map() if k1 else None)

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')

        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')

        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('CapacityStorageSize') is not None:
            self.capacity_storage_size = m.get('CapacityStorageSize')

        if m.get('CloudStorageSize') is not None:
            self.cloud_storage_size = m.get('CloudStorageSize')

        if m.get('CloudStorageType') is not None:
            self.cloud_storage_type = m.get('CloudStorageType')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterPattern') is not None:
            self.cluster_pattern = m.get('ClusterPattern')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EnableCapacityStorage') is not None:
            self.enable_capacity_storage = m.get('EnableCapacityStorage')

        self.engine_list = []
        if m.get('EngineList') is not None:
            for k1 in m.get('EngineList'):
                temp_model = main_models.CreateLindormV2InstanceRequestEngineList()
                self.engine_list.append(temp_model.from_map(k1))

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateLindormV2InstanceRequestEngineList(DaraModel):
    def __init__(
        self,
        engine_type: str = None,
        node_group_list: List[main_models.CreateLindormV2InstanceRequestEngineListNodeGroupList] = None,
    ):
        # This parameter is required.
        self.engine_type = engine_type
        self.node_group_list = node_group_list

    def validate(self):
        if self.node_group_list:
            for v1 in self.node_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        result['NodeGroupList'] = []
        if self.node_group_list is not None:
            for k1 in self.node_group_list:
                result['NodeGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        self.node_group_list = []
        if m.get('NodeGroupList') is not None:
            for k1 in m.get('NodeGroupList'):
                temp_model = main_models.CreateLindormV2InstanceRequestEngineListNodeGroupList()
                self.node_group_list.append(temp_model.from_map(k1))

        return self

class CreateLindormV2InstanceRequestEngineListNodeGroupList(DaraModel):
    def __init__(
        self,
        node_count: int = None,
        node_disk_size: int = None,
        node_disk_type: str = None,
        node_spec: str = None,
        resource_group_name: str = None,
    ):
        # This parameter is required.
        self.node_count = node_count
        self.node_disk_size = node_disk_size
        self.node_disk_type = node_disk_type
        # This parameter is required.
        self.node_spec = node_spec
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_disk_size is not None:
            result['NodeDiskSize'] = self.node_disk_size

        if self.node_disk_type is not None:
            result['NodeDiskType'] = self.node_disk_type

        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeDiskSize') is not None:
            self.node_disk_size = m.get('NodeDiskSize')

        if m.get('NodeDiskType') is not None:
            self.node_disk_type = m.get('NodeDiskType')

        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

