# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstanceAttributeResponseBodyItems = None,
        request_id: str = None,
    ):
        # The queried instance.
        self.items = items
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceAttributeResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance_attribute: List[main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute] = None,
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
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute(DaraModel):
    def __init__(
        self,
        availability_value: str = None,
        cache_storage_size: str = None,
        connection_mode: str = None,
        connection_string: str = None,
        core_version: str = None,
        cpu_cores: int = None,
        cpu_cores_per_node: int = None,
        creation_time: str = None,
        dbinstance_category: str = None,
        dbinstance_class: str = None,
        dbinstance_class_type: str = None,
        dbinstance_cpu_cores: int = None,
        dbinstance_description: str = None,
        dbinstance_disk_mbps: int = None,
        dbinstance_group_count: str = None,
        dbinstance_id: str = None,
        dbinstance_memory: int = None,
        dbinstance_mode: str = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        dbinstance_storage: int = None,
        deploy_mode: str = None,
        encryption_key: str = None,
        encryption_type: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        graph_engine_status: str = None,
        host_type: str = None,
        idle_time: int = None,
        instance_network_type: str = None,
        instance_spec: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        master_aispec: str = None,
        master_cu: int = None,
        master_node_num: int = None,
        max_connections: int = None,
        memory_per_node: int = None,
        memory_size: int = None,
        memory_unit: str = None,
        minor_version: str = None,
        pay_type: str = None,
        port: str = None,
        prod_type: str = None,
        read_delay_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_time: str = None,
        security_iplist: str = None,
        seg_disk_performance_level: str = None,
        seg_node_num: int = None,
        segment_aispec: str = None,
        segment_counts: int = None,
        serverless_mode: str = None,
        serverless_resource: int = None,
        standby_zone_id: str = None,
        start_time: str = None,
        storage_per_node: int = None,
        storage_size: int = None,
        storage_type: str = None,
        storage_unit: str = None,
        support_restore: bool = None,
        tags: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags = None,
        v_switch_id: str = None,
        vector_configuration_status: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Queries the current instance availability status, in percentage (%).
        # 
        # > This parameter is only applicable to instances in the storage reserved mode.
        self.availability_value = availability_value
        self.cache_storage_size = cache_storage_size
        # Access mode, with the following values:
        # 
        # - **Performance**: Standard access mode.
        # - **Safty**: High-security access mode.
        # - **LVS**: LVS link mode.
        self.connection_mode = connection_mode
        # Instance connection address.
        self.connection_string = connection_string
        # Minor version number of the kernel.
        self.core_version = core_version
        # Number of CPU cores for the compute node, unit: Core.
        self.cpu_cores = cpu_cores
        # Number of CPU cores per node.
        # 
        # > This parameter is only applicable to instances in the storage reserved mode.
        self.cpu_cores_per_node = cpu_cores_per_node
        # Instance creation time.
        self.creation_time = creation_time
        # Instance series, with the following values:
        # 
        # - **Basic**: Basic Edition.
        # - **HighAvailability**: High Availability Edition.
        self.dbinstance_category = dbinstance_category
        # Instance specification.
        # 
        # > This parameter is only applicable to reserved storage mode instances.
        self.dbinstance_class = dbinstance_class
        # Instance family, with the following values:
        # 
        # - **s**: Shared type.
        # - **x**: General type.
        # - **d**: Dedicated package.
        # - **h**: Dedicated physical machine.
        self.dbinstance_class_type = dbinstance_class_type
        # Number of CPU cores.
        self.dbinstance_cpu_cores = dbinstance_cpu_cores
        # Instance description.
        self.dbinstance_description = dbinstance_description
        # Maximum BPS (disk throughput) of the compute group, in Mbps.
        # 
        # > This parameter is only applicable to reserved storage mode instances.
        self.dbinstance_disk_mbps = dbinstance_disk_mbps
        # Number of compute groups.
        # 
        # > This parameter is only applicable to reserved storage mode instances.
        self.dbinstance_group_count = dbinstance_group_count
        # Instance ID.
        self.dbinstance_id = dbinstance_id
        # Memory of the compute node.
        # 
        # > The unit for storage-reserved mode is MB; for Serverless and storage-elastic modes, it is GB.
        self.dbinstance_memory = dbinstance_memory
        # Instance resource type, with the following values:
        # 
        # - **Serverless**: Serverless mode.
        # - **StorageElastic**: Storage elastic mode.
        # - **Classic**: Storage reserved mode.
        self.dbinstance_mode = dbinstance_mode
        # This parameter is deprecated and will not return any value.
        self.dbinstance_net_type = dbinstance_net_type
        # Instance status. For more details, see the supplementary explanation of the DBInstanceStatus parameter.
        self.dbinstance_status = dbinstance_status
        # Maximum storage space of a single replica, in GB.
        self.dbinstance_storage = dbinstance_storage
        # The deployment mode.
        self.deploy_mode = deploy_mode
        # Encryption key.
        # 
        # > This parameter is returned only for instances with disk encryption enabled.
        self.encryption_key = encryption_key
        # Encryption type, with the following value:
        # 
        # - **CloudDisk**: Cloud disk encryption.
        # 
        # > This parameter is returned only for instances with cloud disk encryption.
        self.encryption_type = encryption_type
        # Database engine.
        self.engine = engine
        # Database version.
        self.engine_version = engine_version
        # Instance expiration time (in UTC).
        # 
        # > The expiration time for pay-as-you-go instances is `2999-09-08T16:00:00Z`.
        self.expire_time = expire_time
        self.graph_engine_status = graph_engine_status
        # Compute group machine type, with the following values:
        # - **0**: SSD
        # - **1**: HDD
        # 
        # > This parameter applies only to storage-reserved mode instances.
        self.host_type = host_type
        # Idle release waiting time. Unit: seconds.
        # 
        # > This parameter is returned only for instances in the Serverless automatic scheduling mode.
        self.idle_time = idle_time
        # Instance network type, with the following values:
        # 
        # - **Classic**: Classic network.
        # - **VPC**: VPC network.
        self.instance_network_type = instance_network_type
        self.instance_spec = instance_spec
        # Lock mode, with the following values:
        # 
        # - **Unlock**: Normal.
        # - **ManualLock**: Manually triggered lock.
        # - **LockByExpiration**: Automatically locked when the instance expires.
        # - **LockByRestoration**: Automatically locked before the instance rolls back.
        # - **LockByDiskQuota**: Automatically locked when the instance space is full.
        self.lock_mode = lock_mode
        # This parameter is deprecated and will not return any value.
        self.lock_reason = lock_reason
        # Maintenance end time.
        self.maintain_end_time = maintain_end_time
        # Maintenance start time.
        self.maintain_start_time = maintain_start_time
        # The specifications of AI coordinator node resources of the instance. If the coordinator nodes of the instance are not AI nodes, null is returned.
        self.master_aispec = master_aispec
        # Master resources.
        self.master_cu = master_cu
        # Number of Master nodes.
        self.master_node_num = master_node_num
        # Maximum number of concurrent connections for the instance.
        # 
        # > This parameter is only applicable to reserved storage mode instances.
        self.max_connections = max_connections
        # Memory size per replica, see the **MemoryUnit** parameter for the unit.
        # 
        # > This parameter is only applicable to instances in the storage reserved mode.
        self.memory_per_node = memory_per_node
        # Memory size of the compute node.
        # 
        # > The unit is MB for the storage reserved mode; GB for Serverless and storage elastic modes.
        self.memory_size = memory_size
        # Memory unit.
        # 
        # > This parameter is only applicable to reserved storage mode instances.
        self.memory_unit = memory_unit
        # Minor version of the kernel.
        self.minor_version = minor_version
        # Billing type, with the following values:
        # 
        # - **Postpaid**: Pay-as-you-go.
        # - **Prepaid**: Subscription.
        self.pay_type = pay_type
        # Instance port number.
        self.port = port
        # The service type.
        self.prod_type = prod_type
        # This parameter has been deprecated and will not return a value.
        self.read_delay_time = read_delay_time
        # Region ID.
        self.region_id = region_id
        # ID of the resource group where the instance is located.
        self.resource_group_id = resource_group_id
        # Instance running time.
        self.running_time = running_time
        # This parameter is deprecated and will not return any value.
        self.security_iplist = security_iplist
        # Performance Level (PL), currently only **PL1** is supported.
        self.seg_disk_performance_level = seg_disk_performance_level
        # Number of Segment nodes.
        # 
        # > This parameter applies only to instances in the storage elastic mode and Serverless manual scheduling mode.
        self.seg_node_num = seg_node_num
        # The specifications of AI compute node resources of the instance. If the compute nodes of the instance are not AI nodes, null is returned.
        self.segment_aispec = segment_aispec
        # Number of compute groups.
        # 
        # > This parameter applies only to storage-reserved mode instances.
        self.segment_counts = segment_counts
        # The mode of the Serverless instance, with the following values:
        # 
        # - **Manual**: Manual scheduling.
        # - **Auto**: Automatic scheduling.
        # 
        # > This parameter is returned only for Serverless mode instances.
        self.serverless_mode = serverless_mode
        # Compute resource threshold. Unit: ACU.
        # 
        # > This parameter is returned only for instances in the Serverless automatic scheduling mode.
        self.serverless_resource = serverless_resource
        # The secondary zone ID.
        self.standby_zone_id = standby_zone_id
        # The time when the instance started running.
        self.start_time = start_time
        # Storage size per replica, see the **StorageUnit** parameter for units.
        # 
        # > This parameter applies only to storage-reserved mode instances.
        self.storage_per_node = storage_per_node
        # Storage space size, unit: GB.
        self.storage_size = storage_size
        # Storage type, with the following values:
        # 
        # - **cloud_essd**: ESSD cloud disk.
        # - **cloud_efficiency**: Efficient cloud disk.
        # 
        # > This parameter is only applicable to instances in the storage elastic mode.
        self.storage_type = storage_type
        # Storage unit, with the following values:
        # 
        # - **GB SSD**
        # - **TB SSD**
        # - **GB HDD**
        # 
        # > This parameter is only applicable to instances in the storage reserved mode.
        self.storage_unit = storage_unit
        # Indicates whether backup recovery is supported, with the following values:
        # 
        # - **true**: Backup recovery is supported.
        # - **false**: Backup recovery is not supported.
        self.support_restore = support_restore
        # Tag key-value pairs.
        self.tags = tags
        # vSwitch ID.
        self.v_switch_id = v_switch_id
        # Indicates whether vector engine optimization is enabled. The values are as follows:
        # - **enabled**: Indicates that vector engine optimization is enabled.
        # - **disabled**: Indicates that vector engine optimization is disabled.
        self.vector_configuration_status = vector_configuration_status
        # VPC ID.
        self.vpc_id = vpc_id
        # Zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value

        if self.cache_storage_size is not None:
            result['CacheStorageSize'] = self.cache_storage_size

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.core_version is not None:
            result['CoreVersion'] = self.core_version

        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.cpu_cores_per_node is not None:
            result['CpuCoresPerNode'] = self.cpu_cores_per_node

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_class_type is not None:
            result['DBInstanceClassType'] = self.dbinstance_class_type

        if self.dbinstance_cpu_cores is not None:
            result['DBInstanceCpuCores'] = self.dbinstance_cpu_cores

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_disk_mbps is not None:
            result['DBInstanceDiskMBPS'] = self.dbinstance_disk_mbps

        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_memory is not None:
            result['DBInstanceMemory'] = self.dbinstance_memory

        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.graph_engine_status is not None:
            result['GraphEngineStatus'] = self.graph_engine_status

        if self.host_type is not None:
            result['HostType'] = self.host_type

        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.master_aispec is not None:
            result['MasterAISpec'] = self.master_aispec

        if self.master_cu is not None:
            result['MasterCU'] = self.master_cu

        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.memory_per_node is not None:
            result['MemoryPerNode'] = self.memory_per_node

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.memory_unit is not None:
            result['MemoryUnit'] = self.memory_unit

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.prod_type is not None:
            result['ProdType'] = self.prod_type

        if self.read_delay_time is not None:
            result['ReadDelayTime'] = self.read_delay_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.running_time is not None:
            result['RunningTime'] = self.running_time

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level

        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num

        if self.segment_aispec is not None:
            result['SegmentAISpec'] = self.segment_aispec

        if self.segment_counts is not None:
            result['SegmentCounts'] = self.segment_counts

        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode

        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage_per_node is not None:
            result['StoragePerNode'] = self.storage_per_node

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_unit is not None:
            result['StorageUnit'] = self.storage_unit

        if self.support_restore is not None:
            result['SupportRestore'] = self.support_restore

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')

        if m.get('CacheStorageSize') is not None:
            self.cache_storage_size = m.get('CacheStorageSize')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CoreVersion') is not None:
            self.core_version = m.get('CoreVersion')

        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('CpuCoresPerNode') is not None:
            self.cpu_cores_per_node = m.get('CpuCoresPerNode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceClassType') is not None:
            self.dbinstance_class_type = m.get('DBInstanceClassType')

        if m.get('DBInstanceCpuCores') is not None:
            self.dbinstance_cpu_cores = m.get('DBInstanceCpuCores')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceDiskMBPS') is not None:
            self.dbinstance_disk_mbps = m.get('DBInstanceDiskMBPS')

        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceMemory') is not None:
            self.dbinstance_memory = m.get('DBInstanceMemory')

        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GraphEngineStatus') is not None:
            self.graph_engine_status = m.get('GraphEngineStatus')

        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')

        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MasterAISpec') is not None:
            self.master_aispec = m.get('MasterAISpec')

        if m.get('MasterCU') is not None:
            self.master_cu = m.get('MasterCU')

        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MemoryPerNode') is not None:
            self.memory_per_node = m.get('MemoryPerNode')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('MemoryUnit') is not None:
            self.memory_unit = m.get('MemoryUnit')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProdType') is not None:
            self.prod_type = m.get('ProdType')

        if m.get('ReadDelayTime') is not None:
            self.read_delay_time = m.get('ReadDelayTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')

        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')

        if m.get('SegmentAISpec') is not None:
            self.segment_aispec = m.get('SegmentAISpec')

        if m.get('SegmentCounts') is not None:
            self.segment_counts = m.get('SegmentCounts')

        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')

        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StoragePerNode') is not None:
            self.storage_per_node = m.get('StoragePerNode')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUnit') is not None:
            self.storage_unit = m.get('StorageUnit')

        if m.get('SupportRestore') is not None:
            self.support_restore = m.get('SupportRestore')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag] = None,
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
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value.
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

