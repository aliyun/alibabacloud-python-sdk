# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesForCloneResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstancesForCloneResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # An array that consists of the details about the instances.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstancesForCloneResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancesForCloneResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeDBInstancesForCloneResponseBodyItemsDBInstance] = None,
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
                temp_model = main_models.DescribeDBInstancesForCloneResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesForCloneResponseBodyItemsDBInstance(DaraModel):
    def __init__(
        self,
        category: str = None,
        connection_mode: str = None,
        create_time: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        dbinstance_storage_type: str = None,
        dbinstance_type: str = None,
        destroy_time: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        guard_dbinstance_id: str = None,
        ins_id: int = None,
        instance_network_type: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        master_instance_id: str = None,
        mutri_orsignle: bool = None,
        pay_type: str = None,
        read_only_dbinstance_ids: main_models.DescribeDBInstancesForCloneResponseBodyItemsDBInstanceReadOnlyDBInstanceIds = None,
        region_id: str = None,
        replicate_id: str = None,
        resource_group_id: str = None,
        temp_dbinstance_id: str = None,
        v_switch_id: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition
        # *   **HighAvailability**: RDS High-availability Edition
        # *   **Finance**: RDS Enterprise Edition
        self.category = category
        # The connection mode of the instance. Valid values:
        # 
        # *   **Standard**: standard mode
        # *   **Safe**: database proxy mode
        self.connection_mode = connection_mode
        # The time when the instance was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The instance type of the instance. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_class = dbinstance_class
        # The name of the instance. It must be 2 to 256 characters in length. The value can contain letters, digits, underscores (_), and hyphens (-). The value must start with a letter.
        # 
        # > The value cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The network connection type of the instance. Valid values:
        # 
        # *   **Internet**
        # *   **Intranet**
        self.dbinstance_net_type = dbinstance_net_type
        # The status of the instance. For more information, see [Instance state table](https://help.aliyun.com/document_detail/26315.html).
        self.dbinstance_status = dbinstance_status
        # The storage type of the instance. Valid values:
        # 
        # *   **local_ssd/ephemeral_ssd**: local SSD
        # *   **cloud_ssd**: standard SSD.
        # *   **cloud_essd**: enhanced SSD (ESSD)
        self.dbinstance_storage_type = dbinstance_storage_type
        # The role of the instance. Valid values:
        # 
        # *   **Primary**: primary instance
        # *   **Readonly**: read-only instance
        # *   **Guard**: disaster recovery instance
        # *   **Temp**: temporary instance
        self.dbinstance_type = dbinstance_type
        # The time when the instance was destroyed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.destroy_time = destroy_time
        # The database engine of the instance. Valid values:
        # 
        # *   MySQL
        # *   SQLServer
        # *   PostgreSQL
        # *   PPAS
        # *   MariaDB
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The time when the instance expired. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the disaster recovery instance. This parameter is returned only when the instance is a primary instance and has a disaster recovery instance.
        self.guard_dbinstance_id = guard_dbinstance_id
        # The ID of the instance role.
        self.ins_id = ins_id
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**
        # *   **VPC**
        self.instance_network_type = instance_network_type
        # The lock method of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked after it expires.
        # *   **LockByRestoration**: The instance is automatically locked before a rollback.
        # *   **LockByDiskQuota**: The instance is automatically locked because its storage capacity is exhausted and the instance is inaccessible.
        self.lock_mode = lock_mode
        # The reason why the instance was locked.
        self.lock_reason = lock_reason
        # The ID of the primary instance. If the value of this parameter is null, the instance is a primary instance.
        self.master_instance_id = master_instance_id
        # Indicates whether multi-region deployment is used. Valid values:
        # 
        # *   **true**: Multi-region deployment is used.
        # *   **false**: Multi-region deployment is not used.
        self.mutri_orsignle = mutri_orsignle
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # An array consisting of the IDs of the read-only instances that are attached to the primary instance.
        self.read_only_dbinstance_ids = read_only_dbinstance_ids
        # The region ID of the instance.
        self.region_id = region_id
        # None.
        self.replicate_id = replicate_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the temporary instance.
        self.temp_dbinstance_id = temp_dbinstance_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the instance in the VPC.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

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

        if self.guard_dbinstance_id is not None:
            result['GuardDBInstanceId'] = self.guard_dbinstance_id

        if self.ins_id is not None:
            result['InsId'] = self.ins_id

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id

        if self.mutri_orsignle is not None:
            result['MutriORsignle'] = self.mutri_orsignle

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.read_only_dbinstance_ids is not None:
            result['ReadOnlyDBInstanceIds'] = self.read_only_dbinstance_ids.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replicate_id is not None:
            result['ReplicateId'] = self.replicate_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.temp_dbinstance_id is not None:
            result['TempDBInstanceId'] = self.temp_dbinstance_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

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

        if m.get('GuardDBInstanceId') is not None:
            self.guard_dbinstance_id = m.get('GuardDBInstanceId')

        if m.get('InsId') is not None:
            self.ins_id = m.get('InsId')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')

        if m.get('MutriORsignle') is not None:
            self.mutri_orsignle = m.get('MutriORsignle')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ReadOnlyDBInstanceIds') is not None:
            temp_model = main_models.DescribeDBInstancesForCloneResponseBodyItemsDBInstanceReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(m.get('ReadOnlyDBInstanceIds'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicateId') is not None:
            self.replicate_id = m.get('ReplicateId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TempDBInstanceId') is not None:
            self.temp_dbinstance_id = m.get('TempDBInstanceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesForCloneResponseBodyItemsDBInstanceReadOnlyDBInstanceIds(DaraModel):
    def __init__(
        self,
        read_only_dbinstance_id: List[main_models.DescribeDBInstancesForCloneResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId] = None,
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
                temp_model = main_models.DescribeDBInstancesForCloneResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesForCloneResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The ID of the read-only instance.
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

