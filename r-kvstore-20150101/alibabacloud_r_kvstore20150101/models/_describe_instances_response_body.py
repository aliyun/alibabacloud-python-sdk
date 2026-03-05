# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
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
        kvstore_instance: List[main_models.DescribeInstancesResponseBodyInstancesKVStoreInstance] = None,
    ):
        self.kvstore_instance = kvstore_instance

    def validate(self):
        if self.kvstore_instance:
            for v1 in self.kvstore_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KVStoreInstance'] = []
        if self.kvstore_instance is not None:
            for k1 in self.kvstore_instance:
                result['KVStoreInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kvstore_instance = []
        if m.get('KVStoreInstance') is not None:
            for k1 in m.get('KVStoreInstance'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesKVStoreInstance()
                self.kvstore_instance.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesKVStoreInstance(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        bandwidth: int = None,
        capacity: int = None,
        charge_type: str = None,
        cloud_type: str = None,
        computing_type: str = None,
        config: str = None,
        connection_domain: str = None,
        connection_mode: str = None,
        connections: int = None,
        create_time: str = None,
        destroy_time: str = None,
        edition_type: str = None,
        end_time: str = None,
        engine_version: str = None,
        global_instance_id: str = None,
        has_renew_change_order: bool = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        is_rds: bool = None,
        network_type: str = None,
        node_type: str = None,
        package_type: str = None,
        port: int = None,
        private_ip: str = None,
        qps: int = None,
        read_only_count: str = None,
        region_id: str = None,
        replacate_id: str = None,
        replica_count: int = None,
        resource_group_id: str = None,
        secondary_zone_id: str = None,
        shard_class: str = None,
        shard_count: int = None,
        slave_read_only_count: int = None,
        slave_replica_count: int = None,
        tags: main_models.DescribeInstancesResponseBodyInstancesKVStoreInstanceTags = None,
        user_name: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.bandwidth = bandwidth
        self.capacity = capacity
        self.charge_type = charge_type
        self.cloud_type = cloud_type
        self.computing_type = computing_type
        self.config = config
        self.connection_domain = connection_domain
        self.connection_mode = connection_mode
        self.connections = connections
        self.create_time = create_time
        self.destroy_time = destroy_time
        self.edition_type = edition_type
        self.end_time = end_time
        self.engine_version = engine_version
        self.global_instance_id = global_instance_id
        self.has_renew_change_order = has_renew_change_order
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.is_rds = is_rds
        self.network_type = network_type
        self.node_type = node_type
        self.package_type = package_type
        self.port = port
        self.private_ip = private_ip
        self.qps = qps
        self.read_only_count = read_only_count
        self.region_id = region_id
        self.replacate_id = replacate_id
        self.replica_count = replica_count
        self.resource_group_id = resource_group_id
        self.secondary_zone_id = secondary_zone_id
        self.shard_class = shard_class
        self.shard_count = shard_count
        self.slave_read_only_count = slave_read_only_count
        self.slave_replica_count = slave_replica_count
        self.tags = tags
        self.user_name = user_name
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cloud_type is not None:
            result['CloudType'] = self.cloud_type

        if self.computing_type is not None:
            result['ComputingType'] = self.computing_type

        if self.config is not None:
            result['Config'] = self.config

        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connections is not None:
            result['Connections'] = self.connections

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time

        if self.edition_type is not None:
            result['EditionType'] = self.edition_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id

        if self.has_renew_change_order is not None:
            result['HasRenewChangeOrder'] = self.has_renew_change_order

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_rds is not None:
            result['IsRds'] = self.is_rds

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.qps is not None:
            result['QPS'] = self.qps

        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replacate_id is not None:
            result['ReplacateId'] = self.replacate_id

        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.shard_class is not None:
            result['ShardClass'] = self.shard_class

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.slave_read_only_count is not None:
            result['SlaveReadOnlyCount'] = self.slave_read_only_count

        if self.slave_replica_count is not None:
            result['SlaveReplicaCount'] = self.slave_replica_count

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CloudType') is not None:
            self.cloud_type = m.get('CloudType')

        if m.get('ComputingType') is not None:
            self.computing_type = m.get('ComputingType')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')

        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')

        if m.get('HasRenewChangeOrder') is not None:
            self.has_renew_change_order = m.get('HasRenewChangeOrder')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('QPS') is not None:
            self.qps = m.get('QPS')

        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplacateId') is not None:
            self.replacate_id = m.get('ReplacateId')

        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('ShardClass') is not None:
            self.shard_class = m.get('ShardClass')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('SlaveReadOnlyCount') is not None:
            self.slave_read_only_count = m.get('SlaveReadOnlyCount')

        if m.get('SlaveReplicaCount') is not None:
            self.slave_replica_count = m.get('SlaveReplicaCount')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesKVStoreInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesResponseBodyInstancesKVStoreInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag] = None,
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
                temp_model = main_models.DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag(DaraModel):
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

