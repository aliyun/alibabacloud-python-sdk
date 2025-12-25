# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstancesResponseBodyInstances] = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.instances = instances
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        ask_cluster_id: str = None,
        charge_type: str = None,
        cluster_status: str = None,
        ha: bool = None,
        ha_resource_spec: main_models.DescribeInstancesResponseBodyInstancesHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_zone_id: str = None,
        host_aliases: List[main_models.DescribeInstancesResponseBodyInstancesHostAliases] = None,
        instance_id: str = None,
        instance_name: str = None,
        monitor_type: str = None,
        order_state: str = None,
        region: str = None,
        resource_create_time: int = None,
        resource_expired_time: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_spec: main_models.DescribeInstancesResponseBodyInstancesResourceSpec = None,
        storage: main_models.DescribeInstancesResponseBodyInstancesStorage = None,
        tags: List[main_models.DescribeInstancesResponseBodyInstancesTags] = None,
        uid: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.ask_cluster_id = ask_cluster_id
        self.charge_type = charge_type
        self.cluster_status = cluster_status
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_zone_id = ha_zone_id
        # This parameter is required.
        self.host_aliases = host_aliases
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.monitor_type = monitor_type
        self.order_state = order_state
        self.region = region
        self.resource_create_time = resource_create_time
        self.resource_expired_time = resource_expired_time
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_spec = resource_spec
        self.storage = storage
        self.tags = tags
        self.uid = uid
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.host_aliases:
            for v1 in self.host_aliases:
                 if v1:
                    v1.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.ask_cluster_id is not None:
            result['AskClusterId'] = self.ask_cluster_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()

        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids

        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id

        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k1 in self.host_aliases:
                result['HostAliases'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type

        if self.order_state is not None:
            result['OrderState'] = self.order_state

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time

        if self.resource_expired_time is not None:
            result['ResourceExpiredTime'] = self.resource_expired_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        if self.storage is not None:
            result['Storage'] = self.storage.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('AskClusterId') is not None:
            self.ask_cluster_id = m.get('AskClusterId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaResourceSpec') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m.get('HaResourceSpec'))

        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')

        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')

        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k1 in m.get('HostAliases'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesHostAliases()
                self.host_aliases.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('OrderState') is not None:
            self.order_state = m.get('OrderState')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')

        if m.get('ResourceExpiredTime') is not None:
            self.resource_expired_time = m.get('ResourceExpiredTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        if m.get('Storage') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesStorage()
            self.storage = temp_model.from_map(m.get('Storage'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesResponseBodyInstancesTags(DaraModel):
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

class DescribeInstancesResponseBodyInstancesStorage(DaraModel):
    def __init__(
        self,
        oss: main_models.DescribeInstancesResponseBodyInstancesStorageOss = None,
    ):
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oss') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesStorageOss()
            self.oss = temp_model.from_map(m.get('Oss'))

        return self

class DescribeInstancesResponseBodyInstancesStorageOss(DaraModel):
    def __init__(
        self,
        bucket: str = None,
    ):
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        return self

class DescribeInstancesResponseBodyInstancesResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

class DescribeInstancesResponseBodyInstancesHostAliases(DaraModel):
    def __init__(
        self,
        host_names: List[str] = None,
        ip: str = None,
    ):
        # This parameter is required.
        self.host_names = host_names
        # This parameter is required.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_names is not None:
            result['HostNames'] = self.host_names

        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostNames') is not None:
            self.host_names = m.get('HostNames')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

class DescribeInstancesResponseBodyInstancesHaResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

