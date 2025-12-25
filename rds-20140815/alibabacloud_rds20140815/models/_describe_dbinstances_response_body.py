# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstancesResponseBodyItems = None,
        next_token: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The information about the instances.
        self.items = items
        # The token that is used to display the next page. If the returned entries are displayed on multiple pages, the next page can be displayed when you call this operation again with **NextToken** specified.
        self.next_token = next_token
        # The page number of the returned page.
        # 
        # > If you specify **MaxResults** or **NextToken**, only the value **1** is returned. You can ignore the value 1.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        # 
        # > If you specify **MaxResults** or **NextToken**, only the number of entries on the current page is returned. You can ignore the number.
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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
            temp_model = main_models.DescribeDBInstancesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeDBInstancesResponseBodyItemsDBInstance] = None,
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
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyItemsDBInstance(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        blue_green_deployment_name: str = None,
        blue_instance_name: str = None,
        bpe_enabled: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        cold_data_enabled: bool = None,
        connection_mode: str = None,
        connection_string: str = None,
        create_time: str = None,
        dbinstance_cpu: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_memory: int = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        dbinstance_storage_type: str = None,
        dbinstance_type: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_group_name: str = None,
        dedicated_host_id_for_log: str = None,
        dedicated_host_id_for_master: str = None,
        dedicated_host_id_for_slave: str = None,
        dedicated_host_name_for_log: str = None,
        dedicated_host_name_for_master: str = None,
        dedicated_host_name_for_slave: str = None,
        dedicated_host_zone_id_for_log: str = None,
        dedicated_host_zone_id_for_master: str = None,
        dedicated_host_zone_id_for_slave: str = None,
        deletion_protection: bool = None,
        destroy_time: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        general_group_name: str = None,
        green_instance_name: str = None,
        guard_dbinstance_id: str = None,
        instance_network_type: str = None,
        io_acceleration_enabled: str = None,
        is_analytic_ins: str = None,
        is_analytic_read_only_ins: bool = None,
        lock_mode: str = None,
        lock_reason: str = None,
        master_instance_id: str = None,
        mutri_orsignle: bool = None,
        pay_type: str = None,
        read_only_dbinstance_ids: main_models.DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIds = None,
        region_id: str = None,
        resource_group_id: str = None,
        switch_weight: int = None,
        temp_dbinstance_id: str = None,
        tips: str = None,
        tips_level: int = None,
        v_switch_id: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        zone_id: str = None,
    ):
        self.auto_renewal = auto_renewal
        self.blue_green_deployment_name = blue_green_deployment_name
        self.blue_instance_name = blue_instance_name
        # A deprecated parameter.
        self.bpe_enabled = bpe_enabled
        # Indicates whether the I/O burst feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.bursting_enabled = bursting_enabled
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition
        # *   **HighAvailability**: RDS High-availability Edition
        # *   **Finance**: RDS Enterprise Edition
        # 
        # >  This parameter is returned only when the **InstanceLevel** parameter is set to **1**.
        self.category = category
        # A reserved parameter.
        self.cold_data_enabled = cold_data_enabled
        # The connection mode of the instance. Valid values:
        # 
        # *   **Standard**: standard mode
        # *   **Safe**: database proxy mode
        self.connection_mode = connection_mode
        # The endpoint of the instance.
        self.connection_string = connection_string
        # The creation time of the instance. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The number of CPU instances.
        # 
        # Returns only when the InstanceLevel parameter is 1.
        self.dbinstance_cpu = dbinstance_cpu
        # The instance type of the instance. For information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_class = dbinstance_class
        # The instance description.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The memory size of the node. Unit: MB.
        # 
        # Returns only when the InstanceLevel parameter is 1.
        self.dbinstance_memory = dbinstance_memory
        # The type of the network connection to the instance. Valid values:
        # 
        # *   **Internet**
        # *   **Intranet**
        self.dbinstance_net_type = dbinstance_net_type
        # The instance status. For more information, see [Instance statuses](https://help.aliyun.com/document_detail/26315.html).
        self.dbinstance_status = dbinstance_status
        # The storage type of the instance.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The type of the instance. Valid values:
        # 
        # *   **Primary**: primary instance
        # *   **Readonly**: read-only instance
        # *   **Guard**: disaster recovery instance
        # *   **Temp**: temporary instance
        self.dbinstance_type = dbinstance_type
        # The ID of the dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The name of the dedicated cluster.
        self.dedicated_host_group_name = dedicated_host_group_name
        # The ID of the host on which the logger instance resides.
        self.dedicated_host_id_for_log = dedicated_host_id_for_log
        # The ID of the host on which the primary instance resides.
        self.dedicated_host_id_for_master = dedicated_host_id_for_master
        # The ID of the host on which the secondary instance resides.
        self.dedicated_host_id_for_slave = dedicated_host_id_for_slave
        # The name of the host on which the logger instance resides.
        self.dedicated_host_name_for_log = dedicated_host_name_for_log
        # The name of the host on which the primary instance resides.
        self.dedicated_host_name_for_master = dedicated_host_name_for_master
        # The name of the host on which the secondary instance resides.
        self.dedicated_host_name_for_slave = dedicated_host_name_for_slave
        # The zone ID of the host on which the logger instance resides.
        self.dedicated_host_zone_id_for_log = dedicated_host_zone_id_for_log
        # The zone ID of the host on which the primary instance resides.
        self.dedicated_host_zone_id_for_master = dedicated_host_zone_id_for_master
        # The zone ID of the host on which the secondary instance resides.
        self.dedicated_host_zone_id_for_slave = dedicated_host_zone_id_for_slave
        # Indicates whether the release protection feature is enabled for the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.deletion_protection = deletion_protection
        # The time when the instance was destroyed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.destroy_time = destroy_time
        # The database engine of the instance.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The expiration time of the instance. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # >  Pay-as-you-go instances never expire.
        self.expire_time = expire_time
        # The name of the dedicated cluster to which the instance belongs. This parameter is returned only when the instance is created in an ApsaraDB MyBase cluster that runs MySQL on Standard Edition.
        self.general_group_name = general_group_name
        self.green_instance_name = green_instance_name
        # The ID of the disaster recovery instance. This parameter is returned only when the instance is a primary instance and has a disaster recovery instance attached.
        self.guard_dbinstance_id = guard_dbinstance_id
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**
        # *   **VPC**
        self.instance_network_type = instance_network_type
        # Indicates whether the I/O acceleration feature is enabled. Valid values:
        # 
        # *   1: enabled
        # *   0: disabled
        self.io_acceleration_enabled = io_acceleration_enabled
        self.is_analytic_ins = is_analytic_ins
        self.is_analytic_read_only_ins = is_analytic_read_only_ins
        # The lock mode of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before the instance is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage capacity.
        # *   **Released**: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires a long period of time.
        self.lock_mode = lock_mode
        # The reason why the instance was locked.
        self.lock_reason = lock_reason
        # The ID of the primary instance. If this parameter is null, the instance is a primary instance.
        self.master_instance_id = master_instance_id
        # Indicates whether the multi-zone deployment method is used for the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If the multi-zone deployment method is used for the instance, the zone ID of the instance contains MAZ. Example: `cn-hangzhou-MAZ10(h,i)`.
        self.mutri_orsignle = mutri_orsignle
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # The IDs of the read-only instances. This parameter is returned only when the instance is a primary instance and has the read-only instances attached.
        self.read_only_dbinstance_ids = read_only_dbinstance_ids
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Indicates whether the instance supports weight-based switchovers for high availability. This parameter is returned only when the instance is created in an ApsaraDB MyBase cluster that runs MySQL on Standard Edition. Valid values:
        # 
        # *   **100**: The instance supports weight-based switchovers for high availability.
        # *   **0**: The instance does not support weight-based switchovers for high availability.
        self.switch_weight = switch_weight
        # The ID of the temporary instance. This parameter is returned only when the instance is a primary instance and has a temporary instance attached.
        self.temp_dbinstance_id = temp_dbinstance_id
        # The information about the exception that is detected on the instance. This parameter is returned only when the instance is created in an ApsaraDB MyBase cluster that runs MySQL on Standard Edition.
        self.tips = tips
        # The severity of the exception that is detected on the instance. This parameter is returned only when the instance is created in an ApsaraDB MyBase cluster that runs MySQL on Standard Edition. Valid values:
        # 
        # *   **1**: The instance is normal.
        # *   **2**: The specifications of the read-only instances do not match the specifications of the primary instance, and instance performance may be affected. You must adjust the specifications of these instances based on your business requirements.
        self.tips_level = tips_level
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the instance. This parameter is returned only when the instance resides in a VPC.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.blue_green_deployment_name is not None:
            result['BlueGreenDeploymentName'] = self.blue_green_deployment_name

        if self.blue_instance_name is not None:
            result['BlueInstanceName'] = self.blue_instance_name

        if self.bpe_enabled is not None:
            result['BpeEnabled'] = self.bpe_enabled

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.cold_data_enabled is not None:
            result['ColdDataEnabled'] = self.cold_data_enabled

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_cpu is not None:
            result['DBInstanceCPU'] = self.dbinstance_cpu

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

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

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.dedicated_host_group_name is not None:
            result['DedicatedHostGroupName'] = self.dedicated_host_group_name

        if self.dedicated_host_id_for_log is not None:
            result['DedicatedHostIdForLog'] = self.dedicated_host_id_for_log

        if self.dedicated_host_id_for_master is not None:
            result['DedicatedHostIdForMaster'] = self.dedicated_host_id_for_master

        if self.dedicated_host_id_for_slave is not None:
            result['DedicatedHostIdForSlave'] = self.dedicated_host_id_for_slave

        if self.dedicated_host_name_for_log is not None:
            result['DedicatedHostNameForLog'] = self.dedicated_host_name_for_log

        if self.dedicated_host_name_for_master is not None:
            result['DedicatedHostNameForMaster'] = self.dedicated_host_name_for_master

        if self.dedicated_host_name_for_slave is not None:
            result['DedicatedHostNameForSlave'] = self.dedicated_host_name_for_slave

        if self.dedicated_host_zone_id_for_log is not None:
            result['DedicatedHostZoneIdForLog'] = self.dedicated_host_zone_id_for_log

        if self.dedicated_host_zone_id_for_master is not None:
            result['DedicatedHostZoneIdForMaster'] = self.dedicated_host_zone_id_for_master

        if self.dedicated_host_zone_id_for_slave is not None:
            result['DedicatedHostZoneIdForSlave'] = self.dedicated_host_zone_id_for_slave

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.general_group_name is not None:
            result['GeneralGroupName'] = self.general_group_name

        if self.green_instance_name is not None:
            result['GreenInstanceName'] = self.green_instance_name

        if self.guard_dbinstance_id is not None:
            result['GuardDBInstanceId'] = self.guard_dbinstance_id

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.is_analytic_ins is not None:
            result['IsAnalyticIns'] = self.is_analytic_ins

        if self.is_analytic_read_only_ins is not None:
            result['IsAnalyticReadOnlyIns'] = self.is_analytic_read_only_ins

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.switch_weight is not None:
            result['SwitchWeight'] = self.switch_weight

        if self.temp_dbinstance_id is not None:
            result['TempDBInstanceId'] = self.temp_dbinstance_id

        if self.tips is not None:
            result['Tips'] = self.tips

        if self.tips_level is not None:
            result['TipsLevel'] = self.tips_level

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BlueGreenDeploymentName') is not None:
            self.blue_green_deployment_name = m.get('BlueGreenDeploymentName')

        if m.get('BlueInstanceName') is not None:
            self.blue_instance_name = m.get('BlueInstanceName')

        if m.get('BpeEnabled') is not None:
            self.bpe_enabled = m.get('BpeEnabled')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ColdDataEnabled') is not None:
            self.cold_data_enabled = m.get('ColdDataEnabled')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceCPU') is not None:
            self.dbinstance_cpu = m.get('DBInstanceCPU')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

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

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DedicatedHostGroupName') is not None:
            self.dedicated_host_group_name = m.get('DedicatedHostGroupName')

        if m.get('DedicatedHostIdForLog') is not None:
            self.dedicated_host_id_for_log = m.get('DedicatedHostIdForLog')

        if m.get('DedicatedHostIdForMaster') is not None:
            self.dedicated_host_id_for_master = m.get('DedicatedHostIdForMaster')

        if m.get('DedicatedHostIdForSlave') is not None:
            self.dedicated_host_id_for_slave = m.get('DedicatedHostIdForSlave')

        if m.get('DedicatedHostNameForLog') is not None:
            self.dedicated_host_name_for_log = m.get('DedicatedHostNameForLog')

        if m.get('DedicatedHostNameForMaster') is not None:
            self.dedicated_host_name_for_master = m.get('DedicatedHostNameForMaster')

        if m.get('DedicatedHostNameForSlave') is not None:
            self.dedicated_host_name_for_slave = m.get('DedicatedHostNameForSlave')

        if m.get('DedicatedHostZoneIdForLog') is not None:
            self.dedicated_host_zone_id_for_log = m.get('DedicatedHostZoneIdForLog')

        if m.get('DedicatedHostZoneIdForMaster') is not None:
            self.dedicated_host_zone_id_for_master = m.get('DedicatedHostZoneIdForMaster')

        if m.get('DedicatedHostZoneIdForSlave') is not None:
            self.dedicated_host_zone_id_for_slave = m.get('DedicatedHostZoneIdForSlave')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GeneralGroupName') is not None:
            self.general_group_name = m.get('GeneralGroupName')

        if m.get('GreenInstanceName') is not None:
            self.green_instance_name = m.get('GreenInstanceName')

        if m.get('GuardDBInstanceId') is not None:
            self.guard_dbinstance_id = m.get('GuardDBInstanceId')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('IsAnalyticIns') is not None:
            self.is_analytic_ins = m.get('IsAnalyticIns')

        if m.get('IsAnalyticReadOnlyIns') is not None:
            self.is_analytic_read_only_ins = m.get('IsAnalyticReadOnlyIns')

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
            temp_model = main_models.DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(m.get('ReadOnlyDBInstanceIds'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SwitchWeight') is not None:
            self.switch_weight = m.get('SwitchWeight')

        if m.get('TempDBInstanceId') is not None:
            self.temp_dbinstance_id = m.get('TempDBInstanceId')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('TipsLevel') is not None:
            self.tips_level = m.get('TipsLevel')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIds(DaraModel):
    def __init__(
        self,
        read_only_dbinstance_id: List[main_models.DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId] = None,
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
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The read-only instance ID.
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

