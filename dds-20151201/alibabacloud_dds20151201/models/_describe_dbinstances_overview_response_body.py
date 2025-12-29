# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesOverviewResponseBody(DaraModel):
    def __init__(
        self,
        dbinstances: List[main_models.DescribeDBInstancesOverviewResponseBodyDBInstances] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The information of instances.
        self.dbinstances = dbinstances
        # The request ID.
        self.request_id = request_id
        # The number of instances in the query results.
        self.total_count = total_count

    def validate(self):
        if self.dbinstances:
            for v1 in self.dbinstances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k1 in self.dbinstances:
                result['DBInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k1 in m.get('DBInstances'):
                temp_model = main_models.DescribeDBInstancesOverviewResponseBodyDBInstances()
                self.dbinstances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstancesOverviewResponseBodyDBInstances(DaraModel):
    def __init__(
        self,
        capacity_unit: str = None,
        charge_type: str = None,
        creation_time: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        dbinstance_storage: int = None,
        dbinstance_type: str = None,
        destroy_time: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        kind_code: str = None,
        last_downgrade_time: str = None,
        lock_mode: str = None,
        mongos_list: List[main_models.DescribeDBInstancesOverviewResponseBodyDBInstancesMongosList] = None,
        network_type: str = None,
        region_id: str = None,
        replication_factor: str = None,
        resource_group_id: str = None,
        shard_list: List[main_models.DescribeDBInstancesOverviewResponseBodyDBInstancesShardList] = None,
        tags: List[main_models.DescribeDBInstancesOverviewResponseBodyDBInstancesTags] = None,
        vpc_auth_mode: str = None,
        zone_id: str = None,
    ):
        # The read and write throughput consumed by the instance.
        # 
        # > 
        # 
        # *   This parameter is returned when the instance is a serverless instance.
        # 
        # *   Serverless instances are available only in the China site (aliyun.com).
        self.capacity_unit = capacity_unit
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The time when the instance was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The instance type. The instance type varies based on the instance architecture. For more information about instance types supported by different instance architectures, see the following references:
        # 
        # *   [Standalone instance types](https://help.aliyun.com/document_detail/311407.html)
        # *   [Replica set instance types](https://help.aliyun.com/document_detail/311410.html)
        # *   [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html)
        self.dbinstance_class = dbinstance_class
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The state of the instance. For more information about valid values, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.dbinstance_status = dbinstance_status
        # The storage space of the instance. Unit: GB.
        self.dbinstance_storage = dbinstance_storage
        # The architecture of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.dbinstance_type = dbinstance_type
        # The time when the instance data was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.destroy_time = destroy_time
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The time when the instance expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.expire_time = expire_time
        # The kind code of the instance. Valid values:
        # 
        # *   **0**: physical machine
        # *   **1**: Elastic Compute Service (ECS) instance
        # *   **2**: Docker cluster
        # *   **18**: Kubernetes cluster
        self.kind_code = kind_code
        # The date when the last downgrade operation was performed.
        self.last_downgrade_time = last_downgrade_time
        # Indicates whether the instance is locked. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before it is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked after the storage space is exhausted.
        # *   **Released**: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires a long period of time.
        self.lock_mode = lock_mode
        # The details of the mongos nodes.
        # 
        # >  This parameter is returned when the instance is a sharded cluster instance.
        self.mongos_list = mongos_list
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**
        # *   **VPC**
        self.network_type = network_type
        # The region ID of the instance.
        self.region_id = region_id
        # The number of nodes in the instance.
        # 
        # >  This parameter is returned when the instance is a replica set instance.
        self.replication_factor = replication_factor
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The details of the shard nodes.
        # 
        # >  This parameter is returned when the instance is a sharded cluster instance.
        self.shard_list = shard_list
        # The tags to add to the instance.
        self.tags = tags
        # Indicates whether password-free access over VPC is enabled. Valid values:
        # 
        # *   **Open**: Password-free access over VPC is enabled.
        # *   **Close**: Password-free access over VPC is disabled.
        self.vpc_auth_mode = vpc_auth_mode
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.mongos_list:
            for v1 in self.mongos_list:
                 if v1:
                    v1.validate()
        if self.shard_list:
            for v1 in self.shard_list:
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
        if self.capacity_unit is not None:
            result['CapacityUnit'] = self.capacity_unit

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.kind_code is not None:
            result['KindCode'] = self.kind_code

        if self.last_downgrade_time is not None:
            result['LastDowngradeTime'] = self.last_downgrade_time

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        result['MongosList'] = []
        if self.mongos_list is not None:
            for k1 in self.mongos_list:
                result['MongosList'].append(k1.to_map() if k1 else None)

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['ShardList'] = []
        if self.shard_list is not None:
            for k1 in self.shard_list:
                result['ShardList'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityUnit') is not None:
            self.capacity_unit = m.get('CapacityUnit')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')

        if m.get('LastDowngradeTime') is not None:
            self.last_downgrade_time = m.get('LastDowngradeTime')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        self.mongos_list = []
        if m.get('MongosList') is not None:
            for k1 in m.get('MongosList'):
                temp_model = main_models.DescribeDBInstancesOverviewResponseBodyDBInstancesMongosList()
                self.mongos_list.append(temp_model.from_map(k1))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.shard_list = []
        if m.get('ShardList') is not None:
            for k1 in m.get('ShardList'):
                temp_model = main_models.DescribeDBInstancesOverviewResponseBodyDBInstancesShardList()
                self.shard_list.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDBInstancesOverviewResponseBodyDBInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesOverviewResponseBodyDBInstancesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Valid values of N: **1** to **20**.
        # 
        # *   The key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   It can be up to 64 characters in length.
        # *   It cannot be an empty string.
        self.key = key
        # The tag value. Valid values of N: **1** to **20**.
        # 
        # *   The value cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   The value can be up to 128 characters in length.
        # *   The value can be an empty string.
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

class DescribeDBInstancesOverviewResponseBodyDBInstancesShardList(DaraModel):
    def __init__(
        self,
        node_class: str = None,
        node_description: str = None,
        node_id: str = None,
        node_storage: int = None,
        readonly_replicas: int = None,
    ):
        # The instance type of the shard node.
        self.node_class = node_class
        # The description of the shard node.
        self.node_description = node_description
        # The ID of the shard node.
        self.node_id = node_id
        # The storage space of the shard node. Unit: GB.
        self.node_storage = node_storage
        # The number of read-only nodes in the shard node. Valid values: **0** to **5**.
        self.readonly_replicas = readonly_replicas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_description is not None:
            result['NodeDescription'] = self.node_description

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        return self

class DescribeDBInstancesOverviewResponseBodyDBInstancesMongosList(DaraModel):
    def __init__(
        self,
        node_class: str = None,
        node_description: str = None,
        node_id: str = None,
    ):
        # The instance type of the mongos node.
        self.node_class = node_class
        # The description of the mongos node.
        self.node_description = node_description
        # The ID of the mongos node.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_description is not None:
            result['NodeDescription'] = self.node_description

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

