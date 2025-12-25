# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesAsCsvResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstancesAsCsvResponseBodyItems = None,
        request_id: str = None,
    ):
        # An array that consists of the fields in **DBInstanceAttribute**.
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
            temp_model = main_models.DescribeDBInstancesAsCsvResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstancesAsCsvResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance_attribute: List[main_models.DescribeDBInstancesAsCsvResponseBodyItemsDBInstanceAttribute] = None,
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
                temp_model = main_models.DescribeDBInstancesAsCsvResponseBodyItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesAsCsvResponseBodyItemsDBInstanceAttribute(DaraModel):
    def __init__(
        self,
        account_max_quantity: int = None,
        account_type: str = None,
        availability_value: str = None,
        category: str = None,
        connection_mode: str = None,
        connection_string: str = None,
        creation_time: str = None,
        dbinstance_cpu: str = None,
        dbinstance_class: str = None,
        dbinstance_class_type: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_memory: int = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dbinstance_type: str = None,
        dbmax_quantity: int = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        export_key: str = None,
        guard_dbinstance_id: str = None,
        increment_source_dbinstance_id: str = None,
        instance_network_type: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_time: str = None,
        master_instance_id: str = None,
        max_connections: int = None,
        max_iops: int = None,
        pay_type: str = None,
        port: str = None,
        read_delay_time: str = None,
        region_id: str = None,
        security_iplist: str = None,
        slave_zones: main_models.DescribeDBInstancesAsCsvResponseBodyItemsDBInstanceAttributeSlaveZones = None,
        support_upgrade_account_type: str = None,
        tags: str = None,
        temp_dbinstance_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The maximum number of accounts.
        self.account_max_quantity = account_max_quantity
        # The type of the account.
        self.account_type = account_type
        # The service availability of the instance in percentage.
        self.availability_value = availability_value
        # The category of the instance.
        self.category = category
        # The connection mode of the instance. Valid values:
        # 
        # *   **Performance**: standard mode.
        # *   **Safety**: enhanced mode
        self.connection_mode = connection_mode
        # The internal endpoint.
        self.connection_string = connection_string
        # The creation time.
        self.creation_time = creation_time
        # The number of CPU cores.
        self.dbinstance_cpu = dbinstance_cpu
        # The instance type of the instance.
        self.dbinstance_class = dbinstance_class
        # The instance family.
        self.dbinstance_class_type = dbinstance_class_type
        # The instance description.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The memory capacity of the instance. Unit: MB.
        self.dbinstance_memory = dbinstance_memory
        # The network type of the instance. Valid values:
        # 
        # *   **Internet**
        # *   **Intranet**
        self.dbinstance_net_type = dbinstance_net_type
        # The instance status.
        self.dbinstance_status = dbinstance_status
        # The storage capacity of the instance. Unit: GB.
        self.dbinstance_storage = dbinstance_storage
        self.dbinstance_storage_type = dbinstance_storage_type
        # The instance type. Valid values:
        # 
        # *   **Primary**: primary instance
        # *   **ReadOnly**: read-only instance
        # *   **Guard**: disaster recovery instance
        # *   **Temp**: temporary instance
        self.dbinstance_type = dbinstance_type
        # The maximum number of databases that can be created on the instance.
        self.dbmax_quantity = dbmax_quantity
        # The database engine of the instance.
        self.engine = engine
        # The engine version.
        self.engine_version = engine_version
        # The expiration time.
        self.expire_time = expire_time
        # A deprecated parameter. You do not need to specify this parameter.
        self.export_key = export_key
        # The ID of the disaster recovery instance that is attached to the primary instance.
        self.guard_dbinstance_id = guard_dbinstance_id
        # The ID of the instance from which incremental data comes. The incremental data of a disaster recovery instance comes from its primary instance. The incremental data of a read-only instance comes from its primary instance. If this parameter is not returned, the instance is a primary instance.
        self.increment_source_dbinstance_id = increment_source_dbinstance_id
        # The network type.
        self.instance_network_type = instance_network_type
        # The lock mode of the instance.
        self.lock_mode = lock_mode
        # The reason why the instance was locked.
        self.lock_reason = lock_reason
        # The maintenance window of the instance. The time follows the ISO 8601 standard and is displayed in UTC. In the ApsaraDB RDS console, the maintenance window is displayed in UTC+8.
        self.maintain_time = maintain_time
        # The primary instance ID.
        self.master_instance_id = master_instance_id
        # The maximum number of concurrent connections.
        self.max_connections = max_connections
        # The maximum number of I/O requests per second.
        self.max_iops = max_iops
        # The billing method of the instance.
        self.pay_type = pay_type
        # The port that is used to connect to the instance over an internal network.
        self.port = port
        # The latency of data replication from the primary instance to the read-only instance. This parameter is valid for read-only instances.
        self.read_delay_time = read_delay_time
        # The region ID.
        self.region_id = region_id
        # The IP addresses in the whitelist.
        self.security_iplist = security_iplist
        # A deprecated parameter. You do not need to specify this parameter.
        self.slave_zones = slave_zones
        # N/A.
        self.support_upgrade_account_type = support_upgrade_account_type
        # The tags.
        self.tags = tags
        # The ID of the temporary instance that is attached to the primary instance.
        self.temp_dbinstance_id = temp_dbinstance_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.slave_zones:
            self.slave_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_max_quantity is not None:
            result['AccountMaxQuantity'] = self.account_max_quantity

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value

        if self.category is not None:
            result['Category'] = self.category

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbinstance_cpu is not None:
            result['DBInstanceCPU'] = self.dbinstance_cpu

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_class_type is not None:
            result['DBInstanceClassType'] = self.dbinstance_class_type

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

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

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.export_key is not None:
            result['ExportKey'] = self.export_key

        if self.guard_dbinstance_id is not None:
            result['GuardDBInstanceId'] = self.guard_dbinstance_id

        if self.increment_source_dbinstance_id is not None:
            result['IncrementSourceDBInstanceId'] = self.increment_source_dbinstance_id

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time

        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.read_delay_time is not None:
            result['ReadDelayTime'] = self.read_delay_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.slave_zones is not None:
            result['SlaveZones'] = self.slave_zones.to_map()

        if self.support_upgrade_account_type is not None:
            result['SupportUpgradeAccountType'] = self.support_upgrade_account_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.temp_dbinstance_id is not None:
            result['TempDBInstanceId'] = self.temp_dbinstance_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountMaxQuantity') is not None:
            self.account_max_quantity = m.get('AccountMaxQuantity')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBInstanceCPU') is not None:
            self.dbinstance_cpu = m.get('DBInstanceCPU')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceClassType') is not None:
            self.dbinstance_class_type = m.get('DBInstanceClassType')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

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

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExportKey') is not None:
            self.export_key = m.get('ExportKey')

        if m.get('GuardDBInstanceId') is not None:
            self.guard_dbinstance_id = m.get('GuardDBInstanceId')

        if m.get('IncrementSourceDBInstanceId') is not None:
            self.increment_source_dbinstance_id = m.get('IncrementSourceDBInstanceId')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')

        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ReadDelayTime') is not None:
            self.read_delay_time = m.get('ReadDelayTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SlaveZones') is not None:
            temp_model = main_models.DescribeDBInstancesAsCsvResponseBodyItemsDBInstanceAttributeSlaveZones()
            self.slave_zones = temp_model.from_map(m.get('SlaveZones'))

        if m.get('SupportUpgradeAccountType') is not None:
            self.support_upgrade_account_type = m.get('SupportUpgradeAccountType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TempDBInstanceId') is not None:
            self.temp_dbinstance_id = m.get('TempDBInstanceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesAsCsvResponseBodyItemsDBInstanceAttributeSlaveZones(DaraModel):
    def __init__(
        self,
        slave_region: List[str] = None,
    ):
        self.slave_region = slave_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slave_region is not None:
            result['slaveRegion'] = self.slave_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('slaveRegion') is not None:
            self.slave_region = m.get('slaveRegion')

        return self

