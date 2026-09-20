# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        # The page number of the instance list.
        self.page_number = page_number
        # The maximum number of rows displayed per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of instances.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        backup_status: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        cold_storage_status: str = None,
        core_disk_count: str = None,
        core_disk_size: int = None,
        core_disk_type: str = None,
        core_instance_type: str = None,
        core_node_count: int = None,
        created_time: str = None,
        created_time_utc: str = None,
        duration: int = None,
        engine: str = None,
        expire_time: str = None,
        expire_time_utc: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_deletion_protection: bool = None,
        is_ha: bool = None,
        major_version: str = None,
        master_disk_size: int = None,
        master_disk_type: str = None,
        master_instance_type: str = None,
        master_node_count: int = None,
        module_id: int = None,
        module_stack_version: str = None,
        network_type: str = None,
        parent_id: str = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: main_models.DescribeInstancesResponseBodyInstancesInstanceTags = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.auto_renewal = auto_renewal
        self.backup_status = backup_status
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.cold_storage_status = cold_storage_status
        self.core_disk_count = core_disk_count
        self.core_disk_size = core_disk_size
        self.core_disk_type = core_disk_type
        self.core_instance_type = core_instance_type
        self.core_node_count = core_node_count
        self.created_time = created_time
        self.created_time_utc = created_time_utc
        self.duration = duration
        self.engine = engine
        self.expire_time = expire_time
        self.expire_time_utc = expire_time_utc
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.is_deletion_protection = is_deletion_protection
        self.is_ha = is_ha
        self.major_version = major_version
        self.master_disk_size = master_disk_size
        self.master_disk_type = master_disk_type
        self.master_instance_type = master_instance_type
        self.master_node_count = master_node_count
        self.module_id = module_id
        self.module_stack_version = module_stack_version
        self.network_type = network_type
        self.parent_id = parent_id
        self.pay_type = pay_type
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.cold_storage_status is not None:
            result['ColdStorageStatus'] = self.cold_storage_status

        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count

        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size

        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type

        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type

        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection

        if self.is_ha is not None:
            result['IsHa'] = self.is_ha

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size

        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type

        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type

        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('ColdStorageStatus') is not None:
            self.cold_storage_status = m.get('ColdStorageStatus')

        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')

        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')

        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')

        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')

        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')

        if m.get('IsHa') is not None:
            self.is_ha = m.get('IsHa')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')

        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')

        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')

        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesResponseBodyInstancesInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInstancesResponseBodyInstancesInstanceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

