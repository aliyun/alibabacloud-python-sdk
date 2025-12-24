# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormV2InstanceResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        auto_renew: bool = None,
        cloud_storage_size: int = None,
        cold_storage: int = None,
        create_milliseconds: int = None,
        deletion_protection: str = None,
        disk_category: str = None,
        disk_threshold: str = None,
        disk_usage: str = None,
        enable_compute: bool = None,
        engine_list: List[main_models.GetLindormV2InstanceResponseBodyEngineList] = None,
        expired_milliseconds: int = None,
        initial_root_password: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_type: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        network_type: str = None,
        pay_type: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        storage_usage: main_models.GetLindormV2InstanceResponseBodyStorageUsage = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        white_ip_list: List[main_models.GetLindormV2InstanceResponseBodyWhiteIpList] = None,
        zone_engine_info_map: Dict[str, Any] = None,
        zone_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.arbiter_zone_id = arbiter_zone_id
        self.auto_renew = auto_renew
        self.cloud_storage_size = cloud_storage_size
        self.cold_storage = cold_storage
        self.create_milliseconds = create_milliseconds
        self.deletion_protection = deletion_protection
        self.disk_category = disk_category
        self.disk_threshold = disk_threshold
        self.disk_usage = disk_usage
        self.enable_compute = enable_compute
        self.engine_list = engine_list
        self.expired_milliseconds = expired_milliseconds
        self.initial_root_password = initial_root_password
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.network_type = network_type
        self.pay_type = pay_type
        self.primary_vswitch_id = primary_vswitch_id
        self.primary_zone_id = primary_zone_id
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.service_type = service_type
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_zone_id = standby_zone_id
        self.storage_usage = storage_usage
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.white_ip_list = white_ip_list
        self.zone_engine_info_map = zone_engine_info_map
        self.zone_id = zone_id

    def validate(self):
        if self.engine_list:
            for v1 in self.engine_list:
                 if v1:
                    v1.validate()
        if self.storage_usage:
            self.storage_usage.validate()
        if self.white_ip_list:
            for v1 in self.white_ip_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id

        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cloud_storage_size is not None:
            result['CloudStorageSize'] = self.cloud_storage_size

        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage

        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_threshold is not None:
            result['DiskThreshold'] = self.disk_threshold

        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage

        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute

        result['EngineList'] = []
        if self.engine_list is not None:
            for k1 in self.engine_list:
                result['EngineList'].append(k1.to_map() if k1 else None)

        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds

        if self.initial_root_password is not None:
            result['InitialRootPassword'] = self.initial_root_password

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.storage_usage is not None:
            result['StorageUsage'] = self.storage_usage.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        result['WhiteIpList'] = []
        if self.white_ip_list is not None:
            for k1 in self.white_ip_list:
                result['WhiteIpList'].append(k1.to_map() if k1 else None)

        if self.zone_engine_info_map is not None:
            result['ZoneEngineInfoMap'] = self.zone_engine_info_map

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')

        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('CloudStorageSize') is not None:
            self.cloud_storage_size = m.get('CloudStorageSize')

        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')

        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskThreshold') is not None:
            self.disk_threshold = m.get('DiskThreshold')

        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')

        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')

        self.engine_list = []
        if m.get('EngineList') is not None:
            for k1 in m.get('EngineList'):
                temp_model = main_models.GetLindormV2InstanceResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k1))

        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')

        if m.get('InitialRootPassword') is not None:
            self.initial_root_password = m.get('InitialRootPassword')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('StorageUsage') is not None:
            temp_model = main_models.GetLindormV2InstanceResponseBodyStorageUsage()
            self.storage_usage = temp_model.from_map(m.get('StorageUsage'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        self.white_ip_list = []
        if m.get('WhiteIpList') is not None:
            for k1 in m.get('WhiteIpList'):
                temp_model = main_models.GetLindormV2InstanceResponseBodyWhiteIpList()
                self.white_ip_list.append(temp_model.from_map(k1))

        if m.get('ZoneEngineInfoMap') is not None:
            self.zone_engine_info_map = m.get('ZoneEngineInfoMap')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetLindormV2InstanceResponseBodyWhiteIpList(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ip_list: str = None,
    ):
        self.group_name = group_name
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        return self

class GetLindormV2InstanceResponseBodyStorageUsage(DaraModel):
    def __init__(
        self,
        capacity_by_disk_category: List[Dict[str, Any]] = None,
        engine_usage: Dict[str, Any] = None,
    ):
        self.capacity_by_disk_category = capacity_by_disk_category
        self.engine_usage = engine_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_by_disk_category is not None:
            result['CapacityByDiskCategory'] = self.capacity_by_disk_category

        if self.engine_usage is not None:
            result['EngineUsage'] = self.engine_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityByDiskCategory') is not None:
            self.capacity_by_disk_category = m.get('CapacityByDiskCategory')

        if m.get('EngineUsage') is not None:
            self.engine_usage = m.get('EngineUsage')

        return self

class GetLindormV2InstanceResponseBodyEngineList(DaraModel):
    def __init__(
        self,
        connect_address_list: List[main_models.GetLindormV2InstanceResponseBodyEngineListConnectAddressList] = None,
        enable_backup: str = None,
        enable_cdc: str = None,
        engine: str = None,
        is_last_version: bool = None,
        latest_version: str = None,
        node_group: List[main_models.GetLindormV2InstanceResponseBodyEngineListNodeGroup] = None,
        version: str = None,
    ):
        self.connect_address_list = connect_address_list
        self.enable_backup = enable_backup
        self.enable_cdc = enable_cdc
        self.engine = engine
        self.is_last_version = is_last_version
        self.latest_version = latest_version
        self.node_group = node_group
        self.version = version

    def validate(self):
        if self.connect_address_list:
            for v1 in self.connect_address_list:
                 if v1:
                    v1.validate()
        if self.node_group:
            for v1 in self.node_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnectAddressList'] = []
        if self.connect_address_list is not None:
            for k1 in self.connect_address_list:
                result['ConnectAddressList'].append(k1.to_map() if k1 else None)

        if self.enable_backup is not None:
            result['EnableBackup'] = self.enable_backup

        if self.enable_cdc is not None:
            result['EnableCDC'] = self.enable_cdc

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.is_last_version is not None:
            result['IsLastVersion'] = self.is_last_version

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        result['NodeGroup'] = []
        if self.node_group is not None:
            for k1 in self.node_group:
                result['NodeGroup'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connect_address_list = []
        if m.get('ConnectAddressList') is not None:
            for k1 in m.get('ConnectAddressList'):
                temp_model = main_models.GetLindormV2InstanceResponseBodyEngineListConnectAddressList()
                self.connect_address_list.append(temp_model.from_map(k1))

        if m.get('EnableBackup') is not None:
            self.enable_backup = m.get('EnableBackup')

        if m.get('EnableCDC') is not None:
            self.enable_cdc = m.get('EnableCDC')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('IsLastVersion') is not None:
            self.is_last_version = m.get('IsLastVersion')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        self.node_group = []
        if m.get('NodeGroup') is not None:
            for k1 in m.get('NodeGroup'):
                temp_model = main_models.GetLindormV2InstanceResponseBodyEngineListNodeGroup()
                self.node_group.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetLindormV2InstanceResponseBodyEngineListNodeGroup(DaraModel):
    def __init__(
        self,
        category: str = None,
        cpu_core_count: int = None,
        enable_attach_local_disk: bool = None,
        is_scale_spec_group: bool = None,
        local_disk_capacity: int = None,
        local_disk_category: str = None,
        memory_size_gi_b: int = None,
        node_spec: str = None,
        quantity: int = None,
        resource_group_name: str = None,
        spec_id: str = None,
        status: str = None,
    ):
        self.category = category
        self.cpu_core_count = cpu_core_count
        self.enable_attach_local_disk = enable_attach_local_disk
        self.is_scale_spec_group = is_scale_spec_group
        self.local_disk_capacity = local_disk_capacity
        self.local_disk_category = local_disk_category
        self.memory_size_gi_b = memory_size_gi_b
        self.node_spec = node_spec
        self.quantity = quantity
        self.resource_group_name = resource_group_name
        self.spec_id = spec_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count

        if self.enable_attach_local_disk is not None:
            result['EnableAttachLocalDisk'] = self.enable_attach_local_disk

        if self.is_scale_spec_group is not None:
            result['IsScaleSpecGroup'] = self.is_scale_spec_group

        if self.local_disk_capacity is not None:
            result['LocalDiskCapacity'] = self.local_disk_capacity

        if self.local_disk_category is not None:
            result['LocalDiskCategory'] = self.local_disk_category

        if self.memory_size_gi_b is not None:
            result['MemorySizeGiB'] = self.memory_size_gi_b

        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')

        if m.get('EnableAttachLocalDisk') is not None:
            self.enable_attach_local_disk = m.get('EnableAttachLocalDisk')

        if m.get('IsScaleSpecGroup') is not None:
            self.is_scale_spec_group = m.get('IsScaleSpecGroup')

        if m.get('LocalDiskCapacity') is not None:
            self.local_disk_capacity = m.get('LocalDiskCapacity')

        if m.get('LocalDiskCategory') is not None:
            self.local_disk_category = m.get('LocalDiskCategory')

        if m.get('MemorySizeGiB') is not None:
            self.memory_size_gi_b = m.get('MemorySizeGiB')

        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetLindormV2InstanceResponseBodyEngineListConnectAddressList(DaraModel):
    def __init__(
        self,
        address: str = None,
        port: str = None,
        type: str = None,
    ):
        self.address = address
        self.port = port
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.port is not None:
            result['Port'] = self.port

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

