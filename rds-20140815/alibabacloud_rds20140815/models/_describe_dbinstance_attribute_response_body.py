# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstanceAttributeResponseBodyItems = None,
        request_id: str = None,
    ):
        self.items = items
        # The ID of the request.
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
        account_max_quantity: int = None,
        advanced_features: str = None,
        auto_upgrade_minor_version: str = None,
        availability_value: str = None,
        babelfish_config: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeBabelfishConfig = None,
        blue_green_deployment_name: str = None,
        blue_instance_name: str = None,
        bpe_enabled: str = None,
        bursting_enabled: bool = None,
        can_temp_upgrade: bool = None,
        category: str = None,
        cold_data_enabled: bool = None,
        collation: str = None,
        compression_mode: str = None,
        compression_ratio: str = None,
        compute_burst_enabled: bool = None,
        connection_mode: str = None,
        connection_string: str = None,
        console_version: str = None,
        creation_time: str = None,
        current_kernel_version: str = None,
        dbcluster_nodes: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeDBClusterNodes = None,
        dbinstance_cpu: str = None,
        dbinstance_class: str = None,
        dbinstance_class_type: str = None,
        dbinstance_description: str = None,
        dbinstance_disk_used: str = None,
        dbinstance_id: str = None,
        dbinstance_memory: int = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dbinstance_type: str = None,
        dbmax_quantity: int = None,
        dedicated_host_group_id: str = None,
        deletion_protection: bool = None,
        disaster_recovery_info: str = None,
        disaster_recovery_instances: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        extra: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeExtra = None,
        general_group_name: str = None,
        green_instance_name: str = None,
        guard_dbinstance_id: str = None,
        iptype: str = None,
        increment_source_dbinstance_id: str = None,
        instance_network_type: str = None,
        instruction_set_arch: str = None,
        io_acceleration_enabled: str = None,
        is_analytic_ins: bool = None,
        is_analytic_read_only_ins: bool = None,
        latest_kernel_version: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_time: str = None,
        master_instance_id: str = None,
        master_zone: str = None,
        max_connections: int = None,
        max_iombps: int = None,
        max_iops: int = None,
        multiple_temp_upgrade: bool = None,
        optimized_writes_info: str = None,
        pgbouncer_enabled: str = None,
        pay_type: str = None,
        port: str = None,
        proxy_type: int = None,
        read_only_dbinstance_ids: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeReadOnlyDBInstanceIds = None,
        read_only_status: str = None,
        readonly_instance_sqldelayed_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_iplist: str = None,
        security_ipmode: str = None,
        serverless_config: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeServerlessConfig = None,
        slave_zones: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeSlaveZones = None,
        super_permission_mode: str = None,
        support_compression: bool = None,
        temp_dbinstance_id: str = None,
        temp_upgrade_time_end: str = None,
        temp_upgrade_time_start: str = None,
        time_zone: str = None,
        tips: str = None,
        tips_level: int = None,
        v_switch_id: str = None,
        vector_support_status: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
        kind_code: str = None,
    ):
        self.account_max_quantity = account_max_quantity
        self.advanced_features = advanced_features
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.availability_value = availability_value
        self.babelfish_config = babelfish_config
        self.blue_green_deployment_name = blue_green_deployment_name
        self.blue_instance_name = blue_instance_name
        self.bpe_enabled = bpe_enabled
        self.bursting_enabled = bursting_enabled
        self.can_temp_upgrade = can_temp_upgrade
        self.category = category
        self.cold_data_enabled = cold_data_enabled
        self.collation = collation
        self.compression_mode = compression_mode
        self.compression_ratio = compression_ratio
        self.compute_burst_enabled = compute_burst_enabled
        self.connection_mode = connection_mode
        self.connection_string = connection_string
        self.console_version = console_version
        self.creation_time = creation_time
        self.current_kernel_version = current_kernel_version
        self.dbcluster_nodes = dbcluster_nodes
        self.dbinstance_cpu = dbinstance_cpu
        self.dbinstance_class = dbinstance_class
        self.dbinstance_class_type = dbinstance_class_type
        self.dbinstance_description = dbinstance_description
        self.dbinstance_disk_used = dbinstance_disk_used
        self.dbinstance_id = dbinstance_id
        self.dbinstance_memory = dbinstance_memory
        self.dbinstance_net_type = dbinstance_net_type
        self.dbinstance_status = dbinstance_status
        self.dbinstance_storage = dbinstance_storage
        self.dbinstance_storage_type = dbinstance_storage_type
        self.dbinstance_type = dbinstance_type
        self.dbmax_quantity = dbmax_quantity
        self.dedicated_host_group_id = dedicated_host_group_id
        self.deletion_protection = deletion_protection
        self.disaster_recovery_info = disaster_recovery_info
        self.disaster_recovery_instances = disaster_recovery_instances
        self.engine = engine
        self.engine_version = engine_version
        self.expire_time = expire_time
        self.extra = extra
        self.general_group_name = general_group_name
        self.green_instance_name = green_instance_name
        self.guard_dbinstance_id = guard_dbinstance_id
        self.iptype = iptype
        self.increment_source_dbinstance_id = increment_source_dbinstance_id
        self.instance_network_type = instance_network_type
        self.instruction_set_arch = instruction_set_arch
        self.io_acceleration_enabled = io_acceleration_enabled
        self.is_analytic_ins = is_analytic_ins
        self.is_analytic_read_only_ins = is_analytic_read_only_ins
        self.latest_kernel_version = latest_kernel_version
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.maintain_time = maintain_time
        self.master_instance_id = master_instance_id
        self.master_zone = master_zone
        self.max_connections = max_connections
        self.max_iombps = max_iombps
        self.max_iops = max_iops
        self.multiple_temp_upgrade = multiple_temp_upgrade
        self.optimized_writes_info = optimized_writes_info
        self.pgbouncer_enabled = pgbouncer_enabled
        self.pay_type = pay_type
        self.port = port
        self.proxy_type = proxy_type
        self.read_only_dbinstance_ids = read_only_dbinstance_ids
        self.read_only_status = read_only_status
        self.readonly_instance_sqldelayed_time = readonly_instance_sqldelayed_time
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_iplist = security_iplist
        self.security_ipmode = security_ipmode
        self.serverless_config = serverless_config
        self.slave_zones = slave_zones
        self.super_permission_mode = super_permission_mode
        self.support_compression = support_compression
        self.temp_dbinstance_id = temp_dbinstance_id
        self.temp_upgrade_time_end = temp_upgrade_time_end
        self.temp_upgrade_time_start = temp_upgrade_time_start
        self.time_zone = time_zone
        self.tips = tips
        self.tips_level = tips_level
        self.v_switch_id = v_switch_id
        self.vector_support_status = vector_support_status
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id
        self.kind_code = kind_code

    def validate(self):
        if self.babelfish_config:
            self.babelfish_config.validate()
        if self.dbcluster_nodes:
            self.dbcluster_nodes.validate()
        if self.extra:
            self.extra.validate()
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()
        if self.serverless_config:
            self.serverless_config.validate()
        if self.slave_zones:
            self.slave_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_max_quantity is not None:
            result['AccountMaxQuantity'] = self.account_max_quantity

        if self.advanced_features is not None:
            result['AdvancedFeatures'] = self.advanced_features

        if self.auto_upgrade_minor_version is not None:
            result['AutoUpgradeMinorVersion'] = self.auto_upgrade_minor_version

        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value

        if self.babelfish_config is not None:
            result['BabelfishConfig'] = self.babelfish_config.to_map()

        if self.blue_green_deployment_name is not None:
            result['BlueGreenDeploymentName'] = self.blue_green_deployment_name

        if self.blue_instance_name is not None:
            result['BlueInstanceName'] = self.blue_instance_name

        if self.bpe_enabled is not None:
            result['BpeEnabled'] = self.bpe_enabled

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.can_temp_upgrade is not None:
            result['CanTempUpgrade'] = self.can_temp_upgrade

        if self.category is not None:
            result['Category'] = self.category

        if self.cold_data_enabled is not None:
            result['ColdDataEnabled'] = self.cold_data_enabled

        if self.collation is not None:
            result['Collation'] = self.collation

        if self.compression_mode is not None:
            result['CompressionMode'] = self.compression_mode

        if self.compression_ratio is not None:
            result['CompressionRatio'] = self.compression_ratio

        if self.compute_burst_enabled is not None:
            result['ComputeBurstEnabled'] = self.compute_burst_enabled

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.console_version is not None:
            result['ConsoleVersion'] = self.console_version

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version

        if self.dbcluster_nodes is not None:
            result['DBClusterNodes'] = self.dbcluster_nodes.to_map()

        if self.dbinstance_cpu is not None:
            result['DBInstanceCPU'] = self.dbinstance_cpu

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_class_type is not None:
            result['DBInstanceClassType'] = self.dbinstance_class_type

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_disk_used is not None:
            result['DBInstanceDiskUsed'] = self.dbinstance_disk_used

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_memory is not None:
            result['DBInstanceMemory'] = self.dbinstance_memory

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.dbmax_quantity is not None:
            result['DBMaxQuantity'] = self.dbmax_quantity

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.disaster_recovery_info is not None:
            result['DisasterRecoveryInfo'] = self.disaster_recovery_info

        if self.disaster_recovery_instances is not None:
            result['DisasterRecoveryInstances'] = self.disaster_recovery_instances

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.extra is not None:
            result['Extra'] = self.extra.to_map()

        if self.general_group_name is not None:
            result['GeneralGroupName'] = self.general_group_name

        if self.green_instance_name is not None:
            result['GreenInstanceName'] = self.green_instance_name

        if self.guard_dbinstance_id is not None:
            result['GuardDBInstanceId'] = self.guard_dbinstance_id

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.increment_source_dbinstance_id is not None:
            result['IncrementSourceDBInstanceId'] = self.increment_source_dbinstance_id

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instruction_set_arch is not None:
            result['InstructionSetArch'] = self.instruction_set_arch

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.is_analytic_ins is not None:
            result['IsAnalyticIns'] = self.is_analytic_ins

        if self.is_analytic_read_only_ins is not None:
            result['IsAnalyticReadOnlyIns'] = self.is_analytic_read_only_ins

        if self.latest_kernel_version is not None:
            result['LatestKernelVersion'] = self.latest_kernel_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time

        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id

        if self.master_zone is not None:
            result['MasterZone'] = self.master_zone

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iombps is not None:
            result['MaxIOMBPS'] = self.max_iombps

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.multiple_temp_upgrade is not None:
            result['MultipleTempUpgrade'] = self.multiple_temp_upgrade

        if self.optimized_writes_info is not None:
            result['OptimizedWritesInfo'] = self.optimized_writes_info

        if self.pgbouncer_enabled is not None:
            result['PGBouncerEnabled'] = self.pgbouncer_enabled

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.read_only_dbinstance_ids is not None:
            result['ReadOnlyDBInstanceIds'] = self.read_only_dbinstance_ids.to_map()

        if self.read_only_status is not None:
            result['ReadOnlyStatus'] = self.read_only_status

        if self.readonly_instance_sqldelayed_time is not None:
            result['ReadonlyInstanceSQLDelayedTime'] = self.readonly_instance_sqldelayed_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_ipmode is not None:
            result['SecurityIPMode'] = self.security_ipmode

        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()

        if self.slave_zones is not None:
            result['SlaveZones'] = self.slave_zones.to_map()

        if self.super_permission_mode is not None:
            result['SuperPermissionMode'] = self.super_permission_mode

        if self.support_compression is not None:
            result['SupportCompression'] = self.support_compression

        if self.temp_dbinstance_id is not None:
            result['TempDBInstanceId'] = self.temp_dbinstance_id

        if self.temp_upgrade_time_end is not None:
            result['TempUpgradeTimeEnd'] = self.temp_upgrade_time_end

        if self.temp_upgrade_time_start is not None:
            result['TempUpgradeTimeStart'] = self.temp_upgrade_time_start

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.tips is not None:
            result['Tips'] = self.tips

        if self.tips_level is not None:
            result['TipsLevel'] = self.tips_level

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vector_support_status is not None:
            result['VectorSupportStatus'] = self.vector_support_status

        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.kind_code is not None:
            result['kindCode'] = self.kind_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountMaxQuantity') is not None:
            self.account_max_quantity = m.get('AccountMaxQuantity')

        if m.get('AdvancedFeatures') is not None:
            self.advanced_features = m.get('AdvancedFeatures')

        if m.get('AutoUpgradeMinorVersion') is not None:
            self.auto_upgrade_minor_version = m.get('AutoUpgradeMinorVersion')

        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')

        if m.get('BabelfishConfig') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeBabelfishConfig()
            self.babelfish_config = temp_model.from_map(m.get('BabelfishConfig'))

        if m.get('BlueGreenDeploymentName') is not None:
            self.blue_green_deployment_name = m.get('BlueGreenDeploymentName')

        if m.get('BlueInstanceName') is not None:
            self.blue_instance_name = m.get('BlueInstanceName')

        if m.get('BpeEnabled') is not None:
            self.bpe_enabled = m.get('BpeEnabled')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('CanTempUpgrade') is not None:
            self.can_temp_upgrade = m.get('CanTempUpgrade')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ColdDataEnabled') is not None:
            self.cold_data_enabled = m.get('ColdDataEnabled')

        if m.get('Collation') is not None:
            self.collation = m.get('Collation')

        if m.get('CompressionMode') is not None:
            self.compression_mode = m.get('CompressionMode')

        if m.get('CompressionRatio') is not None:
            self.compression_ratio = m.get('CompressionRatio')

        if m.get('ComputeBurstEnabled') is not None:
            self.compute_burst_enabled = m.get('ComputeBurstEnabled')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ConsoleVersion') is not None:
            self.console_version = m.get('ConsoleVersion')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')

        if m.get('DBClusterNodes') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeDBClusterNodes()
            self.dbcluster_nodes = temp_model.from_map(m.get('DBClusterNodes'))

        if m.get('DBInstanceCPU') is not None:
            self.dbinstance_cpu = m.get('DBInstanceCPU')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceClassType') is not None:
            self.dbinstance_class_type = m.get('DBInstanceClassType')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceDiskUsed') is not None:
            self.dbinstance_disk_used = m.get('DBInstanceDiskUsed')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceMemory') is not None:
            self.dbinstance_memory = m.get('DBInstanceMemory')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DBMaxQuantity') is not None:
            self.dbmax_quantity = m.get('DBMaxQuantity')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DisasterRecoveryInfo') is not None:
            self.disaster_recovery_info = m.get('DisasterRecoveryInfo')

        if m.get('DisasterRecoveryInstances') is not None:
            self.disaster_recovery_instances = m.get('DisasterRecoveryInstances')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Extra') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeExtra()
            self.extra = temp_model.from_map(m.get('Extra'))

        if m.get('GeneralGroupName') is not None:
            self.general_group_name = m.get('GeneralGroupName')

        if m.get('GreenInstanceName') is not None:
            self.green_instance_name = m.get('GreenInstanceName')

        if m.get('GuardDBInstanceId') is not None:
            self.guard_dbinstance_id = m.get('GuardDBInstanceId')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('IncrementSourceDBInstanceId') is not None:
            self.increment_source_dbinstance_id = m.get('IncrementSourceDBInstanceId')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstructionSetArch') is not None:
            self.instruction_set_arch = m.get('InstructionSetArch')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('IsAnalyticIns') is not None:
            self.is_analytic_ins = m.get('IsAnalyticIns')

        if m.get('IsAnalyticReadOnlyIns') is not None:
            self.is_analytic_read_only_ins = m.get('IsAnalyticReadOnlyIns')

        if m.get('LatestKernelVersion') is not None:
            self.latest_kernel_version = m.get('LatestKernelVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')

        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')

        if m.get('MasterZone') is not None:
            self.master_zone = m.get('MasterZone')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOMBPS') is not None:
            self.max_iombps = m.get('MaxIOMBPS')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('MultipleTempUpgrade') is not None:
            self.multiple_temp_upgrade = m.get('MultipleTempUpgrade')

        if m.get('OptimizedWritesInfo') is not None:
            self.optimized_writes_info = m.get('OptimizedWritesInfo')

        if m.get('PGBouncerEnabled') is not None:
            self.pgbouncer_enabled = m.get('PGBouncerEnabled')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('ReadOnlyDBInstanceIds') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(m.get('ReadOnlyDBInstanceIds'))

        if m.get('ReadOnlyStatus') is not None:
            self.read_only_status = m.get('ReadOnlyStatus')

        if m.get('ReadonlyInstanceSQLDelayedTime') is not None:
            self.readonly_instance_sqldelayed_time = m.get('ReadonlyInstanceSQLDelayedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPMode') is not None:
            self.security_ipmode = m.get('SecurityIPMode')

        if m.get('ServerlessConfig') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeServerlessConfig()
            self.serverless_config = temp_model.from_map(m.get('ServerlessConfig'))

        if m.get('SlaveZones') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeSlaveZones()
            self.slave_zones = temp_model.from_map(m.get('SlaveZones'))

        if m.get('SuperPermissionMode') is not None:
            self.super_permission_mode = m.get('SuperPermissionMode')

        if m.get('SupportCompression') is not None:
            self.support_compression = m.get('SupportCompression')

        if m.get('TempDBInstanceId') is not None:
            self.temp_dbinstance_id = m.get('TempDBInstanceId')

        if m.get('TempUpgradeTimeEnd') is not None:
            self.temp_upgrade_time_end = m.get('TempUpgradeTimeEnd')

        if m.get('TempUpgradeTimeStart') is not None:
            self.temp_upgrade_time_start = m.get('TempUpgradeTimeStart')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('TipsLevel') is not None:
            self.tips_level = m.get('TipsLevel')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VectorSupportStatus') is not None:
            self.vector_support_status = m.get('VectorSupportStatus')

        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('kindCode') is not None:
            self.kind_code = m.get('kindCode')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeSlaveZones(DaraModel):
    def __init__(
        self,
        slave_zone: List[main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeSlaveZonesSlaveZone] = None,
    ):
        self.slave_zone = slave_zone

    def validate(self):
        if self.slave_zone:
            for v1 in self.slave_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlaveZone'] = []
        if self.slave_zone is not None:
            for k1 in self.slave_zone:
                result['SlaveZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slave_zone = []
        if m.get('SlaveZone') is not None:
            for k1 in m.get('SlaveZone'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeSlaveZonesSlaveZone()
                self.slave_zone.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeSlaveZonesSlaveZone(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeServerlessConfig(DaraModel):
    def __init__(
        self,
        auto_pause: bool = None,
        scale_max: float = None,
        scale_min: float = None,
        switch_force: bool = None,
    ):
        self.auto_pause = auto_pause
        self.scale_max = scale_max
        self.scale_min = scale_min
        self.switch_force = switch_force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pause is not None:
            result['AutoPause'] = self.auto_pause

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.switch_force is not None:
            result['SwitchForce'] = self.switch_force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPause') is not None:
            self.auto_pause = m.get('AutoPause')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('SwitchForce') is not None:
            self.switch_force = m.get('SwitchForce')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeReadOnlyDBInstanceIds(DaraModel):
    def __init__(
        self,
        read_only_dbinstance_id: List[main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeReadOnlyDBInstanceIdsReadOnlyDBInstanceId] = None,
    ):
        self.read_only_dbinstance_id = read_only_dbinstance_id

    def validate(self):
        if self.read_only_dbinstance_id:
            for v1 in self.read_only_dbinstance_id:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReadOnlyDBInstanceId'] = []
        if self.read_only_dbinstance_id is not None:
            for k1 in self.read_only_dbinstance_id:
                result['ReadOnlyDBInstanceId'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.read_only_dbinstance_id = []
        if m.get('ReadOnlyDBInstanceId') is not None:
            for k1 in m.get('ReadOnlyDBInstanceId'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeReadOnlyDBInstanceIdsReadOnlyDBInstanceId(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeExtra(DaraModel):
    def __init__(
        self,
        account_security_policy: str = None,
        dbinstance_ids: main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeExtraDBInstanceIds = None,
        recovery_model: str = None,
    ):
        self.account_security_policy = account_security_policy
        self.dbinstance_ids = dbinstance_ids
        self.recovery_model = recovery_model

    def validate(self):
        if self.dbinstance_ids:
            self.dbinstance_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_security_policy is not None:
            result['AccountSecurityPolicy'] = self.account_security_policy

        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids.to_map()

        if self.recovery_model is not None:
            result['RecoveryModel'] = self.recovery_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSecurityPolicy') is not None:
            self.account_security_policy = m.get('AccountSecurityPolicy')

        if m.get('DBInstanceIds') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeExtraDBInstanceIds()
            self.dbinstance_ids = temp_model.from_map(m.get('DBInstanceIds'))

        if m.get('RecoveryModel') is not None:
            self.recovery_model = m.get('RecoveryModel')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeExtraDBInstanceIds(DaraModel):
    def __init__(
        self,
        dbinstance_id: List[str] = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeDBClusterNodes(DaraModel):
    def __init__(
        self,
        dbcluster_node: List[main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeDBClusterNodesDBClusterNode] = None,
    ):
        self.dbcluster_node = dbcluster_node

    def validate(self):
        if self.dbcluster_node:
            for v1 in self.dbcluster_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBClusterNode'] = []
        if self.dbcluster_node is not None:
            for k1 in self.dbcluster_node:
                result['DBClusterNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster_node = []
        if m.get('DBClusterNode') is not None:
            for k1 in m.get('DBClusterNode'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeDBClusterNodesDBClusterNode()
                self.dbcluster_node.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeDBClusterNodesDBClusterNode(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        class_type: str = None,
        cpu: str = None,
        disaster_recovery_node: bool = None,
        memory: str = None,
        node_id: str = None,
        node_region_id: str = None,
        node_role: str = None,
        node_zone_id: str = None,
        status: str = None,
    ):
        self.class_code = class_code
        self.class_type = class_type
        self.cpu = cpu
        self.disaster_recovery_node = disaster_recovery_node
        self.memory = memory
        self.node_id = node_id
        self.node_region_id = node_region_id
        self.node_role = node_role
        self.node_zone_id = node_zone_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.class_type is not None:
            result['ClassType'] = self.class_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.disaster_recovery_node is not None:
            result['DisasterRecoveryNode'] = self.disaster_recovery_node

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_region_id is not None:
            result['NodeRegionId'] = self.node_region_id

        if self.node_role is not None:
            result['NodeRole'] = self.node_role

        if self.node_zone_id is not None:
            result['NodeZoneId'] = self.node_zone_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('ClassType') is not None:
            self.class_type = m.get('ClassType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DisasterRecoveryNode') is not None:
            self.disaster_recovery_node = m.get('DisasterRecoveryNode')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeRegionId') is not None:
            self.node_region_id = m.get('NodeRegionId')

        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')

        if m.get('NodeZoneId') is not None:
            self.node_zone_id = m.get('NodeZoneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeBabelfishConfig(DaraModel):
    def __init__(
        self,
        babelfish_enabled: str = None,
        migration_mode: str = None,
    ):
        self.babelfish_enabled = babelfish_enabled
        self.migration_mode = migration_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.babelfish_enabled is not None:
            result['BabelfishEnabled'] = self.babelfish_enabled

        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BabelfishEnabled') is not None:
            self.babelfish_enabled = m.get('BabelfishEnabled')

        if m.get('MigrationMode') is not None:
            self.migration_mode = m.get('MigrationMode')

        return self

