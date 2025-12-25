# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20211028 import models as main_models
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
        ansm: bool = None,
        architecture_type: str = None,
        ask_cluster_id: str = None,
        charge_type: str = None,
        cluster_state: main_models.DescribeInstancesResponseBodyInstancesClusterState = None,
        cluster_status: str = None,
        cluster_used_resources: main_models.DescribeInstancesResponseBodyInstancesClusterUsedResources = None,
        cluster_used_storage: main_models.DescribeInstancesResponseBodyInstancesClusterUsedStorage = None,
        elastic: bool = None,
        elastic_instance_id: str = None,
        elastic_order_state: str = None,
        elastic_resource_spec: main_models.DescribeInstancesResponseBodyInstancesElasticResourceSpec = None,
        ha: bool = None,
        ha_resource_spec: main_models.DescribeInstancesResponseBodyInstancesHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_vswitch_info: List[main_models.DescribeInstancesResponseBodyInstancesHaVSwitchInfo] = None,
        ha_zone_id: str = None,
        host_aliases: List[main_models.DescribeInstancesResponseBodyInstancesHostAliases] = None,
        instance_id: str = None,
        instance_name: str = None,
        monitor_type: str = None,
        order_state: str = None,
        oss_info: main_models.DescribeInstancesResponseBodyInstancesOssInfo = None,
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
        v_switch_info: List[main_models.DescribeInstancesResponseBodyInstancesVSwitchInfo] = None,
        vpc_id: str = None,
        vpc_info: main_models.DescribeInstancesResponseBodyInstancesVpcInfo = None,
        zone_id: str = None,
    ):
        self.ansm = ansm
        self.architecture_type = architecture_type
        self.ask_cluster_id = ask_cluster_id
        self.charge_type = charge_type
        self.cluster_state = cluster_state
        self.cluster_status = cluster_status
        self.cluster_used_resources = cluster_used_resources
        self.cluster_used_storage = cluster_used_storage
        self.elastic = elastic
        self.elastic_instance_id = elastic_instance_id
        self.elastic_order_state = elastic_order_state
        self.elastic_resource_spec = elastic_resource_spec
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_vswitch_info = ha_vswitch_info
        self.ha_zone_id = ha_zone_id
        # This parameter is required.
        self.host_aliases = host_aliases
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.monitor_type = monitor_type
        self.order_state = order_state
        self.oss_info = oss_info
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
        self.v_switch_info = v_switch_info
        self.vpc_id = vpc_id
        self.vpc_info = vpc_info
        self.zone_id = zone_id

    def validate(self):
        if self.cluster_state:
            self.cluster_state.validate()
        if self.cluster_used_resources:
            self.cluster_used_resources.validate()
        if self.cluster_used_storage:
            self.cluster_used_storage.validate()
        if self.elastic_resource_spec:
            self.elastic_resource_spec.validate()
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.ha_vswitch_info:
            for v1 in self.ha_vswitch_info:
                 if v1:
                    v1.validate()
        if self.host_aliases:
            for v1 in self.host_aliases:
                 if v1:
                    v1.validate()
        if self.oss_info:
            self.oss_info.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switch_info:
            for v1 in self.v_switch_info:
                 if v1:
                    v1.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ansm is not None:
            result['Ansm'] = self.ansm

        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.ask_cluster_id is not None:
            result['AskClusterId'] = self.ask_cluster_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state.to_map()

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        if self.cluster_used_resources is not None:
            result['ClusterUsedResources'] = self.cluster_used_resources.to_map()

        if self.cluster_used_storage is not None:
            result['ClusterUsedStorage'] = self.cluster_used_storage.to_map()

        if self.elastic is not None:
            result['Elastic'] = self.elastic

        if self.elastic_instance_id is not None:
            result['ElasticInstanceId'] = self.elastic_instance_id

        if self.elastic_order_state is not None:
            result['ElasticOrderState'] = self.elastic_order_state

        if self.elastic_resource_spec is not None:
            result['ElasticResourceSpec'] = self.elastic_resource_spec.to_map()

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()

        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids

        result['HaVSwitchInfo'] = []
        if self.ha_vswitch_info is not None:
            for k1 in self.ha_vswitch_info:
                result['HaVSwitchInfo'].append(k1.to_map() if k1 else None)

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

        if self.oss_info is not None:
            result['OssInfo'] = self.oss_info.to_map()

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

        result['VSwitchInfo'] = []
        if self.v_switch_info is not None:
            for k1 in self.v_switch_info:
                result['VSwitchInfo'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_info is not None:
            result['VpcInfo'] = self.vpc_info.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ansm') is not None:
            self.ansm = m.get('Ansm')

        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('AskClusterId') is not None:
            self.ask_cluster_id = m.get('AskClusterId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterState') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesClusterState()
            self.cluster_state = temp_model.from_map(m.get('ClusterState'))

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        if m.get('ClusterUsedResources') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesClusterUsedResources()
            self.cluster_used_resources = temp_model.from_map(m.get('ClusterUsedResources'))

        if m.get('ClusterUsedStorage') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesClusterUsedStorage()
            self.cluster_used_storage = temp_model.from_map(m.get('ClusterUsedStorage'))

        if m.get('Elastic') is not None:
            self.elastic = m.get('Elastic')

        if m.get('ElasticInstanceId') is not None:
            self.elastic_instance_id = m.get('ElasticInstanceId')

        if m.get('ElasticOrderState') is not None:
            self.elastic_order_state = m.get('ElasticOrderState')

        if m.get('ElasticResourceSpec') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesElasticResourceSpec()
            self.elastic_resource_spec = temp_model.from_map(m.get('ElasticResourceSpec'))

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaResourceSpec') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m.get('HaResourceSpec'))

        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')

        self.ha_vswitch_info = []
        if m.get('HaVSwitchInfo') is not None:
            for k1 in m.get('HaVSwitchInfo'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesHaVSwitchInfo()
                self.ha_vswitch_info.append(temp_model.from_map(k1))

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

        if m.get('OssInfo') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesOssInfo()
            self.oss_info = temp_model.from_map(m.get('OssInfo'))

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

        self.v_switch_info = []
        if m.get('VSwitchInfo') is not None:
            for k1 in m.get('VSwitchInfo'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesVSwitchInfo()
                self.v_switch_info.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcInfo') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesVpcInfo()
            self.vpc_info = temp_model.from_map(m.get('VpcInfo'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesResponseBodyInstancesVpcInfo(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        region_id: str = None,
        status: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.description = description
        self.region_id = region_id
        self.status = status
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeInstancesResponseBodyInstancesVSwitchInfo(DaraModel):
    def __init__(
        self,
        available_ip_address_count: str = None,
        description: str = None,
        region_id: str = None,
        v_switch_cidr: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.available_ip_address_count = available_ip_address_count
        self.description = description
        self.region_id = region_id
        self.v_switch_cidr = v_switch_cidr
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_cidr is not None:
            result['VSwitchCidr'] = self.v_switch_cidr

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchCidr') is not None:
            self.v_switch_cidr = m.get('VSwitchCidr')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

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
        fully_managed: bool = None,
        order_state: str = None,
        oss: main_models.DescribeInstancesResponseBodyInstancesStorageOss = None,
        support_create_fully_managed_storage: bool = None,
        support_migration_progress_detection: bool = None,
    ):
        self.fully_managed = fully_managed
        self.order_state = order_state
        self.oss = oss
        self.support_create_fully_managed_storage = support_create_fully_managed_storage
        self.support_migration_progress_detection = support_migration_progress_detection

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fully_managed is not None:
            result['FullyManaged'] = self.fully_managed

        if self.order_state is not None:
            result['OrderState'] = self.order_state

        if self.oss is not None:
            result['Oss'] = self.oss.to_map()

        if self.support_create_fully_managed_storage is not None:
            result['SupportCreateFullyManagedStorage'] = self.support_create_fully_managed_storage

        if self.support_migration_progress_detection is not None:
            result['SupportMigrationProgressDetection'] = self.support_migration_progress_detection

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullyManaged') is not None:
            self.fully_managed = m.get('FullyManaged')

        if m.get('OrderState') is not None:
            self.order_state = m.get('OrderState')

        if m.get('Oss') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesStorageOss()
            self.oss = temp_model.from_map(m.get('Oss'))

        if m.get('SupportCreateFullyManagedStorage') is not None:
            self.support_create_fully_managed_storage = m.get('SupportCreateFullyManagedStorage')

        if m.get('SupportMigrationProgressDetection') is not None:
            self.support_migration_progress_detection = m.get('SupportMigrationProgressDetection')

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

class DescribeInstancesResponseBodyInstancesOssInfo(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        access_key: str = None,
        bucket: str = None,
        bucket_versioning_status: str = None,
        endpoint: str = None,
    ):
        self.access_id = access_id
        self.access_key = access_key
        self.bucket = bucket
        self.bucket_versioning_status = bucket_versioning_status
        self.endpoint = endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.bucket_versioning_status is not None:
            result['BucketVersioningStatus'] = self.bucket_versioning_status

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BucketVersioningStatus') is not None:
            self.bucket_versioning_status = m.get('BucketVersioningStatus')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

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

class DescribeInstancesResponseBodyInstancesHaVSwitchInfo(DaraModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        description: str = None,
        region_id: str = None,
        v_switch_cidr: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.available_ip_address_count = available_ip_address_count
        self.description = description
        self.region_id = region_id
        self.v_switch_cidr = v_switch_cidr
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_cidr is not None:
            result['VSwitchCidr'] = self.v_switch_cidr

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchCidr') is not None:
            self.v_switch_cidr = m.get('VSwitchCidr')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

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

class DescribeInstancesResponseBodyInstancesElasticResourceSpec(DaraModel):
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

class DescribeInstancesResponseBodyInstancesClusterUsedStorage(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        used_storage: float = None,
    ):
        self.cluster_id = cluster_id
        self.used_storage = used_storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.used_storage is not None:
            result['UsedStorage'] = self.used_storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('UsedStorage') is not None:
            self.used_storage = m.get('UsedStorage')

        return self

class DescribeInstancesResponseBodyInstancesClusterUsedResources(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        elastic_used_cpu: float = None,
        elastic_used_memory: float = None,
        elastic_used_resource: float = None,
        guaranteed_used_cpu: float = None,
        guaranteed_used_memory: float = None,
        guaranteed_used_resource: float = None,
        ha: bool = None,
        ha_used_cpu: float = None,
        ha_used_memory: float = None,
        ha_used_resource: float = None,
        used_cpu: float = None,
        used_memory: float = None,
        used_resource: float = None,
    ):
        self.cluster_id = cluster_id
        self.elastic_used_cpu = elastic_used_cpu
        self.elastic_used_memory = elastic_used_memory
        self.elastic_used_resource = elastic_used_resource
        self.guaranteed_used_cpu = guaranteed_used_cpu
        self.guaranteed_used_memory = guaranteed_used_memory
        self.guaranteed_used_resource = guaranteed_used_resource
        self.ha = ha
        self.ha_used_cpu = ha_used_cpu
        self.ha_used_memory = ha_used_memory
        self.ha_used_resource = ha_used_resource
        self.used_cpu = used_cpu
        self.used_memory = used_memory
        self.used_resource = used_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.elastic_used_cpu is not None:
            result['ElasticUsedCpu'] = self.elastic_used_cpu

        if self.elastic_used_memory is not None:
            result['ElasticUsedMemory'] = self.elastic_used_memory

        if self.elastic_used_resource is not None:
            result['ElasticUsedResource'] = self.elastic_used_resource

        if self.guaranteed_used_cpu is not None:
            result['GuaranteedUsedCpu'] = self.guaranteed_used_cpu

        if self.guaranteed_used_memory is not None:
            result['GuaranteedUsedMemory'] = self.guaranteed_used_memory

        if self.guaranteed_used_resource is not None:
            result['GuaranteedUsedResource'] = self.guaranteed_used_resource

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_used_cpu is not None:
            result['HaUsedCpu'] = self.ha_used_cpu

        if self.ha_used_memory is not None:
            result['HaUsedMemory'] = self.ha_used_memory

        if self.ha_used_resource is not None:
            result['HaUsedResource'] = self.ha_used_resource

        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu

        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory

        if self.used_resource is not None:
            result['UsedResource'] = self.used_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ElasticUsedCpu') is not None:
            self.elastic_used_cpu = m.get('ElasticUsedCpu')

        if m.get('ElasticUsedMemory') is not None:
            self.elastic_used_memory = m.get('ElasticUsedMemory')

        if m.get('ElasticUsedResource') is not None:
            self.elastic_used_resource = m.get('ElasticUsedResource')

        if m.get('GuaranteedUsedCpu') is not None:
            self.guaranteed_used_cpu = m.get('GuaranteedUsedCpu')

        if m.get('GuaranteedUsedMemory') is not None:
            self.guaranteed_used_memory = m.get('GuaranteedUsedMemory')

        if m.get('GuaranteedUsedResource') is not None:
            self.guaranteed_used_resource = m.get('GuaranteedUsedResource')

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaUsedCpu') is not None:
            self.ha_used_cpu = m.get('HaUsedCpu')

        if m.get('HaUsedMemory') is not None:
            self.ha_used_memory = m.get('HaUsedMemory')

        if m.get('HaUsedResource') is not None:
            self.ha_used_resource = m.get('HaUsedResource')

        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')

        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')

        if m.get('UsedResource') is not None:
            self.used_resource = m.get('UsedResource')

        return self

class DescribeInstancesResponseBodyInstancesClusterState(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_stage: main_models.DescribeInstancesResponseBodyInstancesClusterStateClusterStage = None,
        create_timeout: bool = None,
        status: str = None,
        sub_status: str = None,
        url: str = None,
        user_slb_dto: main_models.DescribeInstancesResponseBodyInstancesClusterStateUserSlbDto = None,
        vpc_cidr: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_stage = cluster_stage
        self.create_timeout = create_timeout
        self.status = status
        self.sub_status = sub_status
        self.url = url
        self.user_slb_dto = user_slb_dto
        self.vpc_cidr = vpc_cidr

    def validate(self):
        if self.cluster_stage:
            self.cluster_stage.validate()
        if self.user_slb_dto:
            self.user_slb_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_stage is not None:
            result['ClusterStage'] = self.cluster_stage.to_map()

        if self.create_timeout is not None:
            result['CreateTimeout'] = self.create_timeout

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.url is not None:
            result['Url'] = self.url

        if self.user_slb_dto is not None:
            result['UserSlbDto'] = self.user_slb_dto.to_map()

        if self.vpc_cidr is not None:
            result['VpcCidr'] = self.vpc_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterStage') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesClusterStateClusterStage()
            self.cluster_stage = temp_model.from_map(m.get('ClusterStage'))

        if m.get('CreateTimeout') is not None:
            self.create_timeout = m.get('CreateTimeout')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UserSlbDto') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesClusterStateUserSlbDto()
            self.user_slb_dto = temp_model.from_map(m.get('UserSlbDto'))

        if m.get('VpcCidr') is not None:
            self.vpc_cidr = m.get('VpcCidr')

        return self

class DescribeInstancesResponseBodyInstancesClusterStateUserSlbDto(DaraModel):
    def __init__(
        self,
        exist_slb: bool = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_status: str = None,
        user_slb_listeners: List[main_models.DescribeInstancesResponseBodyInstancesClusterStateUserSlbDtoUserSlbListeners] = None,
    ):
        self.exist_slb = exist_slb
        self.slb_id = slb_id
        self.slb_ip = slb_ip
        self.slb_status = slb_status
        self.user_slb_listeners = user_slb_listeners

    def validate(self):
        if self.user_slb_listeners:
            for v1 in self.user_slb_listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exist_slb is not None:
            result['ExistSlb'] = self.exist_slb

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_status is not None:
            result['SlbStatus'] = self.slb_status

        result['UserSlbListeners'] = []
        if self.user_slb_listeners is not None:
            for k1 in self.user_slb_listeners:
                result['UserSlbListeners'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistSlb') is not None:
            self.exist_slb = m.get('ExistSlb')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbStatus') is not None:
            self.slb_status = m.get('SlbStatus')

        self.user_slb_listeners = []
        if m.get('UserSlbListeners') is not None:
            for k1 in m.get('UserSlbListeners'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesClusterStateUserSlbDtoUserSlbListeners()
                self.user_slb_listeners.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesClusterStateUserSlbDtoUserSlbListeners(DaraModel):
    def __init__(
        self,
        listeners_status: str = None,
        port: str = None,
    ):
        self.listeners_status = listeners_status
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners_status is not None:
            result['ListenersStatus'] = self.listeners_status

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenersStatus') is not None:
            self.listeners_status = m.get('ListenersStatus')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class DescribeInstancesResponseBodyInstancesClusterStateClusterStage(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_stage: int = None,
        message: str = None,
        status: str = None,
        total_stage_with_weight: List[main_models.DescribeInstancesResponseBodyInstancesClusterStateClusterStageTotalStageWithWeight] = None,
    ):
        self.cluster_id = cluster_id
        self.current_stage = current_stage
        self.message = message
        self.status = status
        self.total_stage_with_weight = total_stage_with_weight

    def validate(self):
        if self.total_stage_with_weight:
            for v1 in self.total_stage_with_weight:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        result['TotalStageWithWeight'] = []
        if self.total_stage_with_weight is not None:
            for k1 in self.total_stage_with_weight:
                result['TotalStageWithWeight'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.total_stage_with_weight = []
        if m.get('TotalStageWithWeight') is not None:
            for k1 in m.get('TotalStageWithWeight'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesClusterStateClusterStageTotalStageWithWeight()
                self.total_stage_with_weight.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesClusterStateClusterStageTotalStageWithWeight(DaraModel):
    def __init__(
        self,
        step_index: int = None,
        step_name: str = None,
        weight: int = None,
    ):
        self.step_index = step_index
        self.step_name = step_name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.step_index is not None:
            result['StepIndex'] = self.step_index

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StepIndex') is not None:
            self.step_index = m.get('StepIndex')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

