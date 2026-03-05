# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeInstanceAttributeResponseBodyInstances = None,
        request_id: str = None,
    ):
        self.instances = instances
        # The ID of the request.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceAttributeResponseBodyInstances(DaraModel):
    def __init__(
        self,
        dbinstance_attribute: List[main_models.DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute] = None,
    ):
        self.dbinstance_attribute = dbinstance_attribute

    def validate(self):
        if self.dbinstance_attribute:
            for v1 in self.dbinstance_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k1 in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_attribute = []
        if m.get('DBInstanceAttribute') is not None:
            for k1 in m.get('DBInstanceAttribute'):
                temp_model = main_models.DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k1))

        return self

class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        audit_log_retention: str = None,
        auto_secondary_zone: bool = None,
        availability_value: str = None,
        backup_log_start_time: str = None,
        bandwidth: int = None,
        capacity: int = None,
        charge_type: str = None,
        cloud_type: str = None,
        computing_type: str = None,
        config: str = None,
        connection_domain: str = None,
        connections: int = None,
        create_time: str = None,
        end_time: str = None,
        engine: str = None,
        engine_version: str = None,
        global_instance_id: str = None,
        has_renew_change_order: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_release_protection: bool = None,
        instance_status: str = None,
        instance_type: str = None,
        is_order_completed: bool = None,
        is_rds: bool = None,
        is_support_tde: bool = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        network_type: str = None,
        node_type: str = None,
        package_type: str = None,
        port: int = None,
        private_ip: str = None,
        qps: int = None,
        read_only_count: int = None,
        real_instance_class: str = None,
        region_id: str = None,
        replica_count: int = None,
        replica_id: str = None,
        replication_mode: str = None,
        resource_group_id: str = None,
        secondary_zone_id: str = None,
        security_iplist: str = None,
        shard_count: int = None,
        slave_read_only_count: int = None,
        slave_replica_count: int = None,
        storage: str = None,
        storage_type: str = None,
        tags: main_models.DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags = None,
        v_switch_id: str = None,
        vpc_auth_mode: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
        zone_type: str = None,
    ):
        self.architecture_type = architecture_type
        self.audit_log_retention = audit_log_retention
        self.auto_secondary_zone = auto_secondary_zone
        self.availability_value = availability_value
        self.backup_log_start_time = backup_log_start_time
        self.bandwidth = bandwidth
        self.capacity = capacity
        self.charge_type = charge_type
        self.cloud_type = cloud_type
        self.computing_type = computing_type
        self.config = config
        self.connection_domain = connection_domain
        self.connections = connections
        self.create_time = create_time
        self.end_time = end_time
        self.engine = engine
        self.engine_version = engine_version
        self.global_instance_id = global_instance_id
        self.has_renew_change_order = has_renew_change_order
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_release_protection = instance_release_protection
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.is_order_completed = is_order_completed
        self.is_rds = is_rds
        self.is_support_tde = is_support_tde
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.network_type = network_type
        self.node_type = node_type
        self.package_type = package_type
        self.port = port
        self.private_ip = private_ip
        self.qps = qps
        self.read_only_count = read_only_count
        self.real_instance_class = real_instance_class
        self.region_id = region_id
        self.replica_count = replica_count
        self.replica_id = replica_id
        self.replication_mode = replication_mode
        self.resource_group_id = resource_group_id
        self.secondary_zone_id = secondary_zone_id
        self.security_iplist = security_iplist
        self.shard_count = shard_count
        self.slave_read_only_count = slave_read_only_count
        self.slave_replica_count = slave_replica_count
        self.storage = storage
        self.storage_type = storage_type
        self.tags = tags
        self.v_switch_id = v_switch_id
        self.vpc_auth_mode = vpc_auth_mode
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id
        self.zone_type = zone_type

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

        if self.audit_log_retention is not None:
            result['AuditLogRetention'] = self.audit_log_retention

        if self.auto_secondary_zone is not None:
            result['AutoSecondaryZone'] = self.auto_secondary_zone

        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value

        if self.backup_log_start_time is not None:
            result['BackupLogStartTime'] = self.backup_log_start_time

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

        if self.connections is not None:
            result['Connections'] = self.connections

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine is not None:
            result['Engine'] = self.engine

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

        if self.instance_release_protection is not None:
            result['InstanceReleaseProtection'] = self.instance_release_protection

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_order_completed is not None:
            result['IsOrderCompleted'] = self.is_order_completed

        if self.is_rds is not None:
            result['IsRds'] = self.is_rds

        if self.is_support_tde is not None:
            result['IsSupportTDE'] = self.is_support_tde

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

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

        if self.real_instance_class is not None:
            result['RealInstanceClass'] = self.real_instance_class

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

        if self.replica_id is not None:
            result['ReplicaId'] = self.replica_id

        if self.replication_mode is not None:
            result['ReplicationMode'] = self.replication_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.slave_read_only_count is not None:
            result['SlaveReadOnlyCount'] = self.slave_read_only_count

        if self.slave_replica_count is not None:
            result['SlaveReplicaCount'] = self.slave_replica_count

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode

        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('AuditLogRetention') is not None:
            self.audit_log_retention = m.get('AuditLogRetention')

        if m.get('AutoSecondaryZone') is not None:
            self.auto_secondary_zone = m.get('AutoSecondaryZone')

        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')

        if m.get('BackupLogStartTime') is not None:
            self.backup_log_start_time = m.get('BackupLogStartTime')

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

        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

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

        if m.get('InstanceReleaseProtection') is not None:
            self.instance_release_protection = m.get('InstanceReleaseProtection')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsOrderCompleted') is not None:
            self.is_order_completed = m.get('IsOrderCompleted')

        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')

        if m.get('IsSupportTDE') is not None:
            self.is_support_tde = m.get('IsSupportTDE')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

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

        if m.get('RealInstanceClass') is not None:
            self.real_instance_class = m.get('RealInstanceClass')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

        if m.get('ReplicaId') is not None:
            self.replica_id = m.get('ReplicaId')

        if m.get('ReplicationMode') is not None:
            self.replication_mode = m.get('ReplicationMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('SlaveReadOnlyCount') is not None:
            self.slave_read_only_count = m.get('SlaveReadOnlyCount')

        if m.get('SlaveReplicaCount') is not None:
            self.slave_replica_count = m.get('SlaveReplicaCount')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')

        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag] = None,
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
                temp_model = main_models.DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag(DaraModel):
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

