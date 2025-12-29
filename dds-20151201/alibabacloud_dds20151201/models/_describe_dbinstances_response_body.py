# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesResponseBody(DaraModel):
    def __init__(
        self,
        dbinstances: main_models.DescribeDBInstancesResponseBodyDBInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the instance.
        self.dbinstances = dbinstances
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of instances in the query results.
        self.total_count = total_count

    def validate(self):
        if self.dbinstances:
            self.dbinstances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances.to_map()

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
        if m.get('DBInstances') is not None:
            temp_model = main_models.DescribeDBInstancesResponseBodyDBInstances()
            self.dbinstances = temp_model.from_map(m.get('DBInstances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstancesResponseBodyDBInstances(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstance] = None,
    ):
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            for v1 in self.dbinstance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k1 in self.dbinstance:
                result['DBInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k1 in m.get('DBInstance'):
                temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyDBInstancesDBInstance(DaraModel):
    def __init__(
        self,
        backup_retention_policy: int = None,
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
        hidden_zone_id: str = None,
        kind_code: str = None,
        last_downgrade_time: str = None,
        lock_mode: str = None,
        mongos_list: main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList = None,
        network_type: str = None,
        region_id: str = None,
        release_time: str = None,
        replication_factor: str = None,
        resource_group_id: str = None,
        secondary_zone_id: str = None,
        shard_list: main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList = None,
        storage_type: str = None,
        tags: main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags = None,
        vpc_auth_mode: str = None,
        zone_id: str = None,
    ):
        # The backup retention policy configured for the instance. Valid values:
        # 
        # *   **0**: All backup sets of the instance are immediately deleted when the instance is released.
        # *   **1**: A backup set of the instance is automatically backed up and retained for a long period of time when the instance is released.
        # *   **2**: All backup sets of the instance are automatically backed up and retained for a long period of time when the instance is released.
        self.backup_retention_policy = backup_retention_policy
        # The I/O throughput consumed by the instance.
        # 
        # >  This parameter is required only when the instance is a serverless instance.
        self.capacity_unit = capacity_unit
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid:** pay-as-you-go
        self.charge_type = charge_type
        # The time when the instance was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The instance type of the instance.
        self.dbinstance_class = dbinstance_class
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The status of the instance. For more information, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.dbinstance_status = dbinstance_status
        # The storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage
        # The architecture of the instance.
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.dbinstance_type = dbinstance_type
        # The time when the instance data is destroyed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > *   For a subscription instance, the computing resources of the instance are released on the 16th day after expiration, and the data of the instance is retained for seven days. The data is deleted on the 23th day after expiration and cannot be restored.
        # > *   For a pay-as-you-go instance, the computing resources of the instance are released on the 16th day after the payment becomes overdue, and the data of the instance is retained for seven days. The data is deleted on the 23th day after the payment becomes overdue and cannot be restored.
        self.destroy_time = destroy_time
        # The engine of the instance.
        self.engine = engine
        # The database engine version of the instance. Valid values:
        # 
        # *   **7.0**
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # *   **3.4**
        self.engine_version = engine_version
        # The time when the instance expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.expire_time = expire_time
        # The secondary zone 2 of the instance in the multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hong Kong Zone B
        # *   **cn-hongkong-c**: Hong Kong Zone C
        # *   **cn-hongkong-d**: Hong Kong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > *   This parameter is returned only when the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses the multi-zone deployment.
        # > *   This parameter is returned only if you use the China site (aliyun.com).
        self.hidden_zone_id = hidden_zone_id
        # The kind code of the instance. Valid values:
        # 
        # *   **0**: physical machine
        # *   **1**: Elastic Compute Service (ECS) instance
        # *   **2**: Docker cluster
        # *   **18**: Kubernetes cluster
        self.kind_code = kind_code
        # The date when the last downgrade operation was performed.
        self.last_downgrade_time = last_downgrade_time
        # The lock status of the instance. Valid values:
        # 
        # *   **Unlock**: The cluster is unlocked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before it is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked after the storage space is exhausted.
        # *   **Released**: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires a long period of time.
        self.lock_mode = lock_mode
        # The details of the mongos node.
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.mongos_list = mongos_list
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type
        # The region ID of the instance.
        self.region_id = region_id
        # The time when the instance was released.
        self.release_time = release_time
        # The number of nodes in the instance.
        # 
        # >  This parameter is returned if the instance is a replica set instance.
        self.replication_factor = replication_factor
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The secondary zone 1 of the instance in the multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hong Kong Zone B
        # *   **cn-hongkong-c**: Hong Kong Zone C
        # *   **cn-hongkong-d**: Hong Kong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > *   This parameter is returned only when the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses the multi-zone deployment.
        # > *   This parameter is returned only if you use the China site (aliyun.com).
        self.secondary_zone_id = secondary_zone_id
        # The details of the shard node.
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.shard_list = shard_list
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd**: Enterprise SSD (ESSD)
        # *   **local_ssd**: local SSD
        self.storage_type = storage_type
        # The details of the tag.
        self.tags = tags
        # Indicates whether password-free access over virtual private cloud (VPC) is enabled. Valid values:
        # 
        # *   **Open**: Password-free access over VPC is enabled.
        # *   **Close**: Password-free access over VPC is disabled.
        self.vpc_auth_mode = vpc_auth_mode
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.mongos_list:
            self.mongos_list.validate()
        if self.shard_list:
            self.shard_list.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_retention_policy is not None:
            result['BackupRetentionPolicy'] = self.backup_retention_policy

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

        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id

        if self.kind_code is not None:
            result['KindCode'] = self.kind_code

        if self.last_downgrade_time is not None:
            result['LastDowngradeTime'] = self.last_downgrade_time

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.mongos_list is not None:
            result['MongosList'] = self.mongos_list.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.shard_list is not None:
            result['ShardList'] = self.shard_list.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPolicy') is not None:
            self.backup_retention_policy = m.get('BackupRetentionPolicy')

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

        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')

        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')

        if m.get('LastDowngradeTime') is not None:
            self.last_downgrade_time = m.get('LastDowngradeTime')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MongosList') is not None:
            temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList()
            self.mongos_list = temp_model.from_map(m.get('MongosList'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('ShardList') is not None:
            temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList()
            self.shard_list = temp_model.from_map(m.get('ShardList'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag] = None,
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
                temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList(DaraModel):
    def __init__(
        self,
        shard_attribute: List[main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardListShardAttribute] = None,
    ):
        self.shard_attribute = shard_attribute

    def validate(self):
        if self.shard_attribute:
            for v1 in self.shard_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ShardAttribute'] = []
        if self.shard_attribute is not None:
            for k1 in self.shard_attribute:
                result['ShardAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shard_attribute = []
        if m.get('ShardAttribute') is not None:
            for k1 in m.get('ShardAttribute'):
                temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardListShardAttribute()
                self.shard_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardListShardAttribute(DaraModel):
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
        # The storage capacity of the shard node. Unit: GB.
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

class DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList(DaraModel):
    def __init__(
        self,
        mongos_attribute: List[main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute] = None,
    ):
        self.mongos_attribute = mongos_attribute

    def validate(self):
        if self.mongos_attribute:
            for v1 in self.mongos_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MongosAttribute'] = []
        if self.mongos_attribute is not None:
            for k1 in self.mongos_attribute:
                result['MongosAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mongos_attribute = []
        if m.get('MongosAttribute') is not None:
            for k1 in m.get('MongosAttribute'):
                temp_model = main_models.DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute()
                self.mongos_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute(DaraModel):
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

