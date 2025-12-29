# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        dbinstances: main_models.DescribeDBInstanceAttributeResponseBodyDBInstances = None,
        request_id: str = None,
    ):
        # The instance details.
        self.dbinstances = dbinstances
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstances') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstances()
            self.dbinstances = temp_model.from_map(m.get('DBInstances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstances(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance] = None,
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
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance(DaraModel):
    def __init__(
        self,
        bursting_enabled: bool = None,
        capacity_unit: str = None,
        charge_type: str = None,
        configserver_list: main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList = None,
        creation_time: str = None,
        current_kernel_version: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_order_status: str = None,
        dbinstance_release_protection: bool = None,
        dbinstance_status: str = None,
        dbinstance_storage: int = None,
        dbinstance_type: str = None,
        destroy_time: str = None,
        disaster_recovery_info: str = None,
        encrypted: bool = None,
        encryption_key: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        hidden_zone_id: str = None,
        kind_code: str = None,
        last_downgrade_time: str = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        max_connections: int = None,
        max_iops: int = None,
        max_mbps: int = None,
        mongos_list: main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList = None,
        network_type: str = None,
        protocol_type: str = None,
        provisioned_iops: int = None,
        readonly_replicas: str = None,
        region_id: str = None,
        replacate_id: str = None,
        replica_set_name: str = None,
        replica_sets: main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets = None,
        replication_factor: str = None,
        resource_group_id: str = None,
        search_node_class: str = None,
        search_node_count: int = None,
        search_node_storage: int = None,
        secondary_zone_id: str = None,
        shard_list: main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList = None,
        storage_engine: str = None,
        storage_type: str = None,
        sync_percent: str = None,
        tags: main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags = None,
        use_cluster_backup: bool = None,
        vpccloud_instance_ids: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_auth_mode: str = None,
        zone_id: str = None,
    ):
        # Indicates whether performance burst is enabled for the ESSD AutoPL disk.
        self.bursting_enabled = bursting_enabled
        # The read and write throughput consumed by the instance.
        self.capacity_unit = capacity_unit
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The details of the ConfigServer node.
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.configserver_list = configserver_list
        # The time when the instance was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The minor version of the current database in the instance.
        self.current_kernel_version = current_kernel_version
        # The instance type of the instance.
        self.dbinstance_class = dbinstance_class
        # The name of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The status of the orders generated for the instance. Valid values:
        # 
        # *   **all_completed**: All orders are being produced or complete.
        # *   **order_unpaid**: The instance has unpaid orders.
        # *   **order_wait_for_produce**: Orders are being delivered for production.
        # 
        # >  The order production process includes the following steps: place an order, pay for an order, deliver an order for production, produce an order, and complete the production.
        # 
        # *   If an order is in the **order_wait_for_produce** state for a long time, an error occurs when the order is being delivered for production. The system will automatically retry.
        # *   The instance status changes only when the order is in the producing and complete state, such as changing configurations and running.
        self.dbinstance_order_status = dbinstance_order_status
        # Indicates whether release protection is enabled for the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.dbinstance_release_protection = dbinstance_release_protection
        # The status of the instance. For more information, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.dbinstance_status = dbinstance_status
        # The storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage
        # The architecture of the instance. Valid values:
        # 
        # *   **replicate**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.dbinstance_type = dbinstance_type
        # The time when the instance data was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.destroy_time = destroy_time
        self.disaster_recovery_info = disaster_recovery_info
        # Indicates whether disk encryption is enabled.
        self.encrypted = encrypted
        # The Key Management Service (KMS) key used for disk encryption.
        self.encryption_key = encryption_key
        # The database engine of the instance.
        self.engine = engine
        # The database engine version of the instance.
        # 
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        self.engine_version = engine_version
        # The time when the subscription instance expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is returned if the instance is a subscription instance.
        self.expire_time = expire_time
        # The ID of the secondary zone 2 of the instance. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hongkong Zone B
        # *   **cn-hongkong-c**: Hongkong Zone C
        # *   **cn-hongkong-d**: Hongkong Zone D
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
        # > 
        # 
        # *   This parameter is returned if the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses multi-zone deployment.
        # 
        # *   This parameter is returned only if you use the China site (aliyun.com).
        self.hidden_zone_id = hidden_zone_id
        # The kind code of the instance. Valid values:
        # 
        # *   **0**: physical machine
        # *   **1**: Elastic Compute Service (ECS) instance
        # *   **2**: Docker cluster
        # *   **18**: Kubernetes cluster
        self.kind_code = kind_code
        # The date when the last downgrade operation was performed on the instance.
        self.last_downgrade_time = last_downgrade_time
        # The lock status of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before the instance is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked after the storage space is exhausted.
        # *   **Released**: The instance is released.
        self.lock_mode = lock_mode
        # The end time of the maintenance window. The time follows the ISO 8601 standard in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window. The time follows the ISO 8601 standard in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_start_time = maintain_start_time
        # The maximum number of connections to the instance.
        self.max_connections = max_connections
        # The maximum IOPS of the instance.
        self.max_iops = max_iops
        # The maximum MBPS of the instance.
        self.max_mbps = max_mbps
        # The details of the mongos node.
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.mongos_list = mongos_list
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type
        # The access protocol type of the instance. Valid values:
        # 
        # *   **mongodb**
        # *   **dynamodb**
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.protocol_type = protocol_type
        # The provisioned performance of the ESSD AutoPL disk.
        self.provisioned_iops = provisioned_iops
        # The number of read-only nodes in the instance.
        self.readonly_replicas = readonly_replicas
        # The region ID of the instance.
        self.region_id = region_id
        # The logical ID of the replica set instance.
        # 
        # >  ApsaraDB for MongoDB does not support new instances of this type. This parameter applies only to previous-version replica set instances.
        self.replacate_id = replacate_id
        # The name of the replica set instance.
        # 
        # >  This parameter is returned if the instance is a replica set instance.
        self.replica_set_name = replica_set_name
        # The information of the replica set instance.
        # 
        # >  This parameter is returned if the instance is a replica set instance.
        self.replica_sets = replica_sets
        # The number of nodes in the instance.
        # 
        # >  This parameter is returned if the instance is a replica set instance.
        self.replication_factor = replication_factor
        # The ID of the resource group to which the instance belongs.
        # 
        # >  This parameter is returned only if you use the China site (aliyun.com).
        self.resource_group_id = resource_group_id
        self.search_node_class = search_node_class
        self.search_node_count = search_node_count
        self.search_node_storage = search_node_storage
        # The ID of the secondary zone 1 of the instance. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hongkong Zone B
        # *   **cn-hongkong-c**: Hongkong Zone C
        # *   **cn-hongkong-d**: Hongkong Zone D
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
        # > 
        # 
        # *   This parameter is returned if the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses multi-zone deployment.
        # 
        # *   This parameter is returned only if you use the China site (aliyun.com).
        self.secondary_zone_id = secondary_zone_id
        # The details of the shard node.
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.shard_list = shard_list
        # The storage engine of the instance.
        self.storage_engine = storage_engine
        # The storage type of the instance. Valid values:
        # 
        # **cloud_essd1**: ESSD PL1 **cloud_essd2**: ESSD PL2 **cloud_essd3**: ESSD PL3 **local_ssd**: local SSD **cloud_essd_dbfs_s**: DBFS disk
        self.storage_type = storage_type
        # The progress of data synchronization in percentage. When you are changing the configurations of the instance, you must synchronize the data of the instance. You can obtain the data synchronization progress based on the value returned for this parameter.
        self.sync_percent = sync_percent
        # The details of the instance tags.
        self.tags = tags
        # Indicates whether the cluster backup mode is enabled. Valid values:
        # 
        # *   **true**: The cluster backup mode is enabled.
        # *   **false**: The cluster backup mode is disabled.
        self.use_cluster_backup = use_cluster_backup
        # The instance ID.
        # 
        # >  This parameter is returned if the network type of the instance is VPC.
        self.vpccloud_instance_ids = vpccloud_instance_ids
        # The VPC ID of the instance.
        # 
        # >  This parameter is returned if the network type of the instance is VPC.
        self.vpcid = vpcid
        # The vSwitch ID of the instance.
        # 
        # >  This parameter is returned if the network type of the instance is VPC.
        self.v_switch_id = v_switch_id
        # Indicates whether password-free access within the VPC is enabled. Valid values:
        # 
        # *   **Open**: Password-free access within the VPC is enabled.
        # *   **Close**: Password-free access within the VPC is disabled, and you must use a password for access.
        # *   **NotSupport**: Password-free access within the VPC is not supported.
        self.vpc_auth_mode = vpc_auth_mode
        # The ID of the zone in which the instance resides.
        self.zone_id = zone_id

    def validate(self):
        if self.configserver_list:
            self.configserver_list.validate()
        if self.mongos_list:
            self.mongos_list.validate()
        if self.replica_sets:
            self.replica_sets.validate()
        if self.shard_list:
            self.shard_list.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.capacity_unit is not None:
            result['CapacityUnit'] = self.capacity_unit

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.configserver_list is not None:
            result['ConfigserverList'] = self.configserver_list.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_order_status is not None:
            result['DBInstanceOrderStatus'] = self.dbinstance_order_status

        if self.dbinstance_release_protection is not None:
            result['DBInstanceReleaseProtection'] = self.dbinstance_release_protection

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time

        if self.disaster_recovery_info is not None:
            result['DisasterRecoveryInfo'] = self.disaster_recovery_info

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

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

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.max_mbps is not None:
            result['MaxMBPS'] = self.max_mbps

        if self.mongos_list is not None:
            result['MongosList'] = self.mongos_list.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replacate_id is not None:
            result['ReplacateId'] = self.replacate_id

        if self.replica_set_name is not None:
            result['ReplicaSetName'] = self.replica_set_name

        if self.replica_sets is not None:
            result['ReplicaSets'] = self.replica_sets.to_map()

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.search_node_class is not None:
            result['SearchNodeClass'] = self.search_node_class

        if self.search_node_count is not None:
            result['SearchNodeCount'] = self.search_node_count

        if self.search_node_storage is not None:
            result['SearchNodeStorage'] = self.search_node_storage

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.shard_list is not None:
            result['ShardList'] = self.shard_list.to_map()

        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.sync_percent is not None:
            result['SyncPercent'] = self.sync_percent

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.use_cluster_backup is not None:
            result['UseClusterBackup'] = self.use_cluster_backup

        if self.vpccloud_instance_ids is not None:
            result['VPCCloudInstanceIds'] = self.vpccloud_instance_ids

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('CapacityUnit') is not None:
            self.capacity_unit = m.get('CapacityUnit')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ConfigserverList') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList()
            self.configserver_list = temp_model.from_map(m.get('ConfigserverList'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceOrderStatus') is not None:
            self.dbinstance_order_status = m.get('DBInstanceOrderStatus')

        if m.get('DBInstanceReleaseProtection') is not None:
            self.dbinstance_release_protection = m.get('DBInstanceReleaseProtection')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')

        if m.get('DisasterRecoveryInfo') is not None:
            self.disaster_recovery_info = m.get('DisasterRecoveryInfo')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

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

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('MaxMBPS') is not None:
            self.max_mbps = m.get('MaxMBPS')

        if m.get('MongosList') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList()
            self.mongos_list = temp_model.from_map(m.get('MongosList'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplacateId') is not None:
            self.replacate_id = m.get('ReplacateId')

        if m.get('ReplicaSetName') is not None:
            self.replica_set_name = m.get('ReplicaSetName')

        if m.get('ReplicaSets') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets()
            self.replica_sets = temp_model.from_map(m.get('ReplicaSets'))

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SearchNodeClass') is not None:
            self.search_node_class = m.get('SearchNodeClass')

        if m.get('SearchNodeCount') is not None:
            self.search_node_count = m.get('SearchNodeCount')

        if m.get('SearchNodeStorage') is not None:
            self.search_node_storage = m.get('SearchNodeStorage')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('ShardList') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList()
            self.shard_list = temp_model.from_map(m.get('ShardList'))

        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SyncPercent') is not None:
            self.sync_percent = m.get('SyncPercent')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UseClusterBackup') is not None:
            self.use_cluster_backup = m.get('UseClusterBackup')

        if m.get('VPCCloudInstanceIds') is not None:
            self.vpccloud_instance_ids = m.get('VPCCloudInstanceIds')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag] = None,
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
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag(DaraModel):
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

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList(DaraModel):
    def __init__(
        self,
        shard_attribute: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute] = None,
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
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute()
                self.shard_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute(DaraModel):
    def __init__(
        self,
        connect_string: str = None,
        current_kernel_version: str = None,
        lock_mode: str = None,
        max_connections: int = None,
        max_disk_mbps: str = None,
        max_iops: int = None,
        node_class: str = None,
        node_description: str = None,
        node_id: str = None,
        node_storage: int = None,
        port: int = None,
        readonly_replicas: int = None,
        replica_set_name: str = None,
        status: str = None,
    ):
        # The endpoint of the shard node.
        self.connect_string = connect_string
        # The minor version of the current MongoDB kernel.
        self.current_kernel_version = current_kernel_version
        # The lock status of the shard node. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before a rollback.
        # *   **LockByDiskQuota**: The instance is automatically locked because its storage capacity is exhausted and the instance is inaccessible.
        self.lock_mode = lock_mode
        # The maximum number of connections to the shard node.
        self.max_connections = max_connections
        # The maximum MBPS of the shard node.
        self.max_disk_mbps = max_disk_mbps
        # The maximum IOPS of the shard node.
        self.max_iops = max_iops
        # The instance type of the shard node.
        self.node_class = node_class
        # The name of the shard node.
        self.node_description = node_description
        # The ID of the shard node.
        self.node_id = node_id
        # The storage capacity of the shard node. Unit: GB.
        self.node_storage = node_storage
        # The port number that is used to connect to the shard node.
        self.port = port
        # The number of read-only nodes in the shard node. Valid values: **0** to **5**. The value must be an integer.
        self.readonly_replicas = readonly_replicas
        self.replica_set_name = replica_set_name
        # The status of the shard node. For more information, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string

        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_disk_mbps is not None:
            result['MaxDiskMbps'] = self.max_disk_mbps

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_description is not None:
            result['NodeDescription'] = self.node_description

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage

        if self.port is not None:
            result['Port'] = self.port

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        if self.replica_set_name is not None:
            result['ReplicaSetName'] = self.replica_set_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')

        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxDiskMbps') is not None:
            self.max_disk_mbps = m.get('MaxDiskMbps')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        if m.get('ReplicaSetName') is not None:
            self.replica_set_name = m.get('ReplicaSetName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets(DaraModel):
    def __init__(
        self,
        replica_set: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet] = None,
    ):
        self.replica_set = replica_set

    def validate(self):
        if self.replica_set:
            for v1 in self.replica_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReplicaSet'] = []
        if self.replica_set is not None:
            for k1 in self.replica_set:
                result['ReplicaSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.replica_set = []
        if m.get('ReplicaSet') is not None:
            for k1 in m.get('ReplicaSet'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet()
                self.replica_set.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet(DaraModel):
    def __init__(
        self,
        connection_domain: str = None,
        connection_port: str = None,
        network_type: str = None,
        replica_set_role: str = None,
        vpccloud_instance_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The endpoint of the node.
        self.connection_domain = connection_domain
        # The port number that is used to connect to the node.
        self.connection_port = connection_port
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type
        # The role of the node. Valid values:
        # 
        # *   **Primary**
        # *   **Secondary**
        self.replica_set_role = replica_set_role
        # The instance ID.
        # 
        # >  This parameter is returned if the network type of the instance is VPC.
        self.vpccloud_instance_id = vpccloud_instance_id
        # The VPC ID of the instance.
        # 
        # >  This parameter is returned if the network type of the instance is VPC.
        self.vpcid = vpcid
        # The vSwitch ID of the instance.
        # 
        # >  This parameter is returned if the network type of the instance is virtual private cloud (VPC).
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.connection_port is not None:
            result['ConnectionPort'] = self.connection_port

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role

        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('ConnectionPort') is not None:
            self.connection_port = m.get('ConnectionPort')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')

        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList(DaraModel):
    def __init__(
        self,
        mongos_attribute: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute] = None,
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
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute()
                self.mongos_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute(DaraModel):
    def __init__(
        self,
        connect_sting: str = None,
        connect_string: str = None,
        current_kernel_version: str = None,
        lock_mode: str = None,
        max_connections: int = None,
        max_iops: int = None,
        node_class: str = None,
        node_description: str = None,
        node_id: str = None,
        port: int = None,
        status: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_cloud_instance_id: str = None,
    ):
        # The endpoint of the mongos node.
        self.connect_sting = connect_sting
        # The endpoint of the mongos node.
        self.connect_string = connect_string
        # The minor version of the current MongoDB kernel.
        self.current_kernel_version = current_kernel_version
        # The lock status of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before a rollback.
        # *   **LockByDiskQuota**: The instance is automatically locked because its storage capacity is exhausted and the instance is inaccessible.
        self.lock_mode = lock_mode
        # The maximum number of connections to the mongos node.
        self.max_connections = max_connections
        # The maximum IOPS of the mongos node.
        self.max_iops = max_iops
        # The instance type of the mongos node.
        self.node_class = node_class
        # The name of the mongos node.
        self.node_description = node_description
        # The ID of the mongos node.
        self.node_id = node_id
        # The port number that is used to connect to the mongos node.
        self.port = port
        # The status of the mongos node. For more information, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.status = status
        # The VPC ID of the instance.
        # 
        # >  This parameter is returned if the network type of the instance is VPC.
        self.vpcid = vpcid
        # The vSwitch ID of the instance.
        # 
        # >  This parameter is returned if the network type of the instance is VPC.
        self.v_switch_id = v_switch_id
        # The ID of the mongos node.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_sting is not None:
            result['ConnectSting'] = self.connect_sting

        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string

        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_description is not None:
            result['NodeDescription'] = self.node_description

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.port is not None:
            result['Port'] = self.port

        if self.status is not None:
            result['Status'] = self.status

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectSting') is not None:
            self.connect_sting = m.get('ConnectSting')

        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')

        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList(DaraModel):
    def __init__(
        self,
        configserver_attribute: List[main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute] = None,
    ):
        self.configserver_attribute = configserver_attribute

    def validate(self):
        if self.configserver_attribute:
            for v1 in self.configserver_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigserverAttribute'] = []
        if self.configserver_attribute is not None:
            for k1 in self.configserver_attribute:
                result['ConfigserverAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configserver_attribute = []
        if m.get('ConfigserverAttribute') is not None:
            for k1 in m.get('ConfigserverAttribute'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute()
                self.configserver_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute(DaraModel):
    def __init__(
        self,
        connect_string: str = None,
        current_kernel_version: str = None,
        lock_mode: str = None,
        max_connections: int = None,
        max_iops: int = None,
        node_class: str = None,
        node_description: str = None,
        node_id: str = None,
        node_storage: int = None,
        port: int = None,
        status: str = None,
    ):
        # The endpoint of the Configserver node.
        self.connect_string = connect_string
        # The minor version of the current MongoDB kernel.
        self.current_kernel_version = current_kernel_version
        # The lock status of the Configserver node. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before a rollback.
        # *   **LockByDiskQuota**: The instance is automatically locked because its storage capacity is exhausted and the instance is inaccessible.
        self.lock_mode = lock_mode
        # The maximum number of connections to the Configserver node.
        self.max_connections = max_connections
        # The maximum IOPS of the Configserver node.
        self.max_iops = max_iops
        # The instance type of the Configserver node.
        self.node_class = node_class
        # The name of the Configserver node.
        self.node_description = node_description
        # The ID of the Configserver node.
        self.node_id = node_id
        # The storage capacity of the Configserver node. Unit: GB.
        self.node_storage = node_storage
        # The port number that is used to connect to the Configserver node.
        self.port = port
        # The status of the Configserver node. For more information, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string

        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.node_description is not None:
            result['NodeDescription'] = self.node_description

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage

        if self.port is not None:
            result['Port'] = self.port

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')

        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

