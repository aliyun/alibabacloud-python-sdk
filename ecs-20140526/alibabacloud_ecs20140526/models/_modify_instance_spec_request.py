# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        system_disk: main_models.ModifyInstanceSpecRequestSystemDisk = None,
        temporary: main_models.ModifyInstanceSpecRequestTemporary = None,
        allow_migrate_across_zone: bool = None,
        async_: bool = None,
        client_token: str = None,
        disk: List[main_models.ModifyInstanceSpecRequestDisk] = None,
        dry_run: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        modify_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.system_disk = system_disk
        self.temporary = temporary
        # Specifies whether cross-cluster instance type upgrades are supported.
        self.allow_migrate_across_zone = allow_migrate_across_zone
        # Specifies whether to submit an asynchronous request. Valid values:
        self.async_ = async_
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # > This parameter is not publicly available.
        self.disk = disk
        # Specifies whether to perform only a dry run. Valid values:
        self.dry_run = dry_run
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The target instance type of the instance. For more information, see [Instance family](https://help.aliyun.com/document_detail/25378.html). You can also invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the most recent instance type list.
        self.instance_type = instance_type
        # The maximum inbound public bandwidth. Unit: Mbit/s (Megabit per second). Valid values:
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s (Megabit per second). Valid values: 0 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # > This parameter is not publicly available.
        self.modify_mode = modify_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.temporary:
            self.temporary.validate()
        if self.disk:
            for v1 in self.disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.temporary is not None:
            result['Temporary'] = self.temporary.to_map()

        if self.allow_migrate_across_zone is not None:
            result['AllowMigrateAcrossZone'] = self.allow_migrate_across_zone

        if self.async_ is not None:
            result['Async'] = self.async_

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['Disk'] = []
        if self.disk is not None:
            for k1 in self.disk:
                result['Disk'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = main_models.ModifyInstanceSpecRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Temporary') is not None:
            temp_model = main_models.ModifyInstanceSpecRequestTemporary()
            self.temporary = temp_model.from_map(m.get('Temporary'))

        if m.get('AllowMigrateAcrossZone') is not None:
            self.allow_migrate_across_zone = m.get('AllowMigrateAcrossZone')

        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.disk = []
        if m.get('Disk') is not None:
            for k1 in m.get('Disk'):
                temp_model = main_models.ModifyInstanceSpecRequestDisk()
                self.disk.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyInstanceSpecRequestDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        performance_level: str = None,
    ):
        # > This parameter is not publicly available.
        self.category = category
        # > This parameter is not publicly available.
        self.disk_id = disk_id
        # > This parameter is not publicly available.
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        return self

class ModifyInstanceSpecRequestTemporary(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        internet_max_bandwidth_out: int = None,
        start_time: str = None,
    ):
        # > This parameter is in invitational preview and is not publicly available.
        self.end_time = end_time
        # > This parameter is in invitational preview and is not publicly available.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # > This parameter is in invitational preview and is not publicly available.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ModifyInstanceSpecRequestSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
    ):
        # The new system disk category. Valid values:
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        return self

