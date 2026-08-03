# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesOverviewResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstancesOverviewResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of instances.
        self.instances = instances
        # The request ID.
        self.request_id = request_id
        # The total number of instances.
        self.total_count = total_count

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstancesOverviewResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesOverviewResponseBodyInstances(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        capacity: int = None,
        charge_type: str = None,
        connection_domain: str = None,
        create_time: str = None,
        end_time: str = None,
        engine_version: str = None,
        global_instance_id: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        network_type: str = None,
        node_type: str = None,
        private_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_zone_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The architecture type. Valid values:
        # * **cluster**: Cluster Edition.
        # * **standard**: Standard Edition.
        # * **rwsplit**: read/write splitting edition.
        self.architecture_type = architecture_type
        # The storage capacity of the instance. Unit: MB.
        self.capacity = capacity
        # The billing method. Valid values:
        # * **PrePaid**: subscription.
        # * **PostPaid**: pay-as-you-go.
        self.charge_type = charge_type
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain
        # The time when the instance was created.
        self.create_time = create_time
        # The time when the subscription instance expires.
        self.end_time = end_time
        # The Redis-compatible engine version of the instance. Valid values: **2.8**, **4.0**, **5.0**, **6.0**, and **7.0**.
        self.engine_version = engine_version
        # The distributed instance ID.
        # > This parameter is returned only when the instance is a child instance of a distributed instance.
        self.global_instance_id = global_instance_id
        # The instance type.
        self.instance_class = instance_class
        # The instance ID.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The instance status. Valid values:
        # * **Normal**: The instance is running.
        # * **Creating**: The instance is being created.
        # * **Changing**: The instance is being modified.
        # * **Inactive**: The instance is disabled.
        # * **Flushing**: The instance is being purged.
        # * **Released**: The instance is released.
        # * **Transforming**: The instance is being transformed.
        # * **Unavailable**: The instance is unavailable.
        # * **Error**: The instance failed to be created.
        # * **Migrating**: The instance is being migrated.
        # * **BackupRecovering**: The instance is being restored from a backup.
        # * **MinorVersionUpgrading**: A minor version upgrade is in progress.
        # * **NetworkModifying**: The network configuration is being modified.
        # * **SSLModifying**: The SSL configuration is being modified.
        # * **MajorVersionUpgrading**: A major engine version upgrade is in progress. The instance can be accessed normally.
        self.instance_status = instance_status
        # The instance type. Valid values:
        # * **Tair**: Tair (Enterprise Edition).
        # * **Redis**: Redis Community Edition.
        # * **Memcache**
        self.instance_type = instance_type
        # The network type. Valid values:
        # * **CLASSIC**: classic network.
        # * **VPC**: virtual private cloud (VPC).
        self.network_type = network_type
        self.node_type = node_type
        # The private IP address of the instance in a VPC. The IP address may change. Use ConnectionDomain (internal endpoint) to connect to the instance.
        # > - This parameter is not returned if the network type of the instance is classic network.
        # > - This parameter is not returned for cloud-native instances.
        self.private_ip = private_ip
        # The region ID.
        self.region_id = region_id
        # The resource group ID to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The secondary zone ID.
        # > This parameter is returned only when the instance has a secondary zone.
        self.secondary_zone_id = secondary_zone_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id

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

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

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

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')

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

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

