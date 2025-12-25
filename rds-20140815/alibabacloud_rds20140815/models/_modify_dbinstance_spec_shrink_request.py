# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSpecShrinkRequest(DaraModel):
    def __init__(
        self,
        allow_major_version_upgrade: bool = None,
        auto_use_coupon: bool = None,
        bursting_enabled: bool = None,
        category: str = None,
        cold_data_enabled: bool = None,
        compression_mode: str = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dedicated_host_group_id: str = None,
        direction: str = None,
        effective_time: str = None,
        engine_version: str = None,
        io_acceleration_enabled: str = None,
        optimized_writes: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        promotion_code: str = None,
        read_only_dbinstance_class: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        serverless_configuration_shrink: str = None,
        source_biz: str = None,
        switch_time: str = None,
        target_minor_version: str = None,
        used_time: int = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
    ):
        # Specifies whether to upgrade the major engine version of an ApsaraDB RDS for SQL Server instance. For more information, see [Upgrade the major engine version](https://help.aliyun.com/document_detail/127458.html). Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > *   When you upgrade the major engine version, you must also specify the required parameters such as DBInstanceId, EngineVersion, DBInstanceClass, Category, ZoneId, and VSwitchId.
        # > *   If you want to upgrade the instance edition to RDS High-availability Edition or RDS Cluster Edition, you must specify ZoneIdSlave1.
        self.allow_major_version_upgrade = allow_major_version_upgrade
        # Specifies whether to use vouchers to offset fees. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.auto_use_coupon = auto_use_coupon
        # An invalid parameter. You do not need to specify this parameter.
        self.bursting_enabled = bursting_enabled
        # The RDS edition of the instance. Valid values:
        # 
        # >  If you set **EngineVersion** to an SQL Server version number, you must also specify this parameter.
        # 
        # **Regular RDS instances**
        # 
        # *   **Basic**: RDS Basic Edition.
        # *   **HighAvailability**: RDS High-availability Edition.
        # *   **AlwaysOn**: RDS Cluster Edition for ApsaraDB RDS for SQL Server.
        # *   **Cluster**: RDS Cluster Edition for ApsaraDB RDS for MySQL.
        # 
        # **Serverless instances. ApsaraDB RDS for MariaDB does not support serverless instances.**
        # 
        # *   **serverless_basic**: RDS Basic Edition. This edition is available only for serverless instances that run MySQL and PostgreSQL.
        # *   **serverless_standard**: RDS High-availability Edition. This edition is available only for serverless instances that run MySQL and PostgreSQL.
        # *   **serverless_ha**: RDS High-availability Edition for serverless instances. This edition is available only for instances that run SQL Server.
        self.category = category
        # A reserved parameter.
        self.cold_data_enabled = cold_data_enabled
        # Specifies whether to enable the storage compression feature for the ApsaraDB RDS for MySQL instance. For more information, see [Use the storage compression feature](https://help.aliyun.com/document_detail/2861985.html). Valid values:
        # 
        # *   **on**
        # *   **off**
        self.compression_mode = compression_mode
        # The instance type of the new instance. For more information, see [Specifications](https://help.aliyun.com/document_detail/26312.html). You can call the [DescribeAvailableClasses](https://help.aliyun.com/document_detail/610393.html) operation to query the instance types.
        # 
        # > *   You must specify at least one of DBInstanceClass and **DBInstanceStorage**.
        # > *   You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/610394.html) operation to query the current instance type of the instance.
        self.dbinstance_class = dbinstance_class
        # The instance ID. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) operation to query the instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The storage capacity of the new instance. Unit: GB. For more information, see [Storage types](https://help.aliyun.com/document_detail/26312.html). You can call the [DescribeAvailableClasses](https://help.aliyun.com/document_detail/610393.html) operation to query the storage capacity range that is supported by the new instance type.
        # 
        # > *   You must specify at least one of DBInstanceStorage and **DBInstanceClass**.
        # > *   You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/610394.html) operation to query the current storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the new instance. Valid values:
        # 
        # *   **local_ssd**: local SSD.
        # *   **cloud_ssd**: SSD cloud disks. This storage medium is not recommended and is unavailable in specific Alibaba Cloud regions.
        # *   **cloud_essd**: performance level 1 (PL1) Enterprise SSD (ESSD).
        # *   **cloud_essd2**: PL2 ESSD.
        # *   **cloud_essd3**: PL3 ESSD.
        # 
        # To change the storage type, take note of the following items:
        # 
        # If the instance runs PostgreSQL, you can upgrade the storage type of the instance from standard SSDs to ESSDs. However, you cannot downgrade the storage type of the instance from ESSDs to standard SSDs. ESSDs provide the following PLs: ESSDs of PL1, ESSDs of PL2, and ESSDs of PL3. You can upgrade or downgrade the storage type between ESSD of PL1, ESSD of PL2, and ESSD of PL3. For more information, see [Configuration items](https://help.aliyun.com/document_detail/96750.html).
        self.dbinstance_storage_type = dbinstance_storage_type
        # The ID of the dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The type of change that you want to perform on the instance. Valid values:
        # 
        # *   **Up** (default): upgrades a subscription instance, or upgrades or downgrades a pay-as-you-go instance.
        # *   **Down**: downgrades a subscription instance.
        # *   **TempUpgrade**: performs auto scaling on a subscription instance that runs SQL Server. This value is required for auto scaling.
        # *   **Serverless**: modifies the auto scaling settings of a serverless instance.
        # 
        # >  If you specify only **DBInstanceStorageType**, you can leave Direction empty. For example, if you want to change only the storage type of the instance from standard SSD to Enterprise SSD (ESSD), you do not need to specify Direction.
        self.direction = direction
        # The time when the new specifications take effect. Valid values:
        # 
        # >  **Specific changes may affect the instance**. Read the [Impact](https://help.aliyun.com/document_detail/96061.html) section before you specify this parameter. We recommend that you specify this parameter during off-peak hours.
        # 
        # *   **Immediate** (default): The changes immediately take effect.
        # *   **MaintainTime**: The changes take effect during the [maintenance window](https://help.aliyun.com/document_detail/610402.html) of the instance.
        # *   **ScheduleTime**: The changes take effect at the point in time that you specify. This time must be at least 12 hours later than the current time. The actual effective time is calculated based on the following formula: EffectiveTime = ScheduleTime + SwitchTime.
        self.effective_time = effective_time
        # The database engine version of the instance. Valid values:
        # 
        # **Regular RDS instances**
        # 
        # *   Valid values when Engine is set to MySQL: 5.5, 5.6, 5.7, and 8.0.
        # *   Valid values when Engine is set to SQLServer: 2008r2, 08r2_ent_ha, 2012, 2012_ent_ha, 2012_std_ha, 2012_web, 2014_std_ha, 2016_ent_ha, 2016_std_ha, 2016_web, 2017_std_ha, 2017_ent, 2019_std_ha, and 2019_ent.
        # *   Valid values when Engine is set to PostgreSQL: 10.0, 11.0, 12.0, 13.0, 14.0, and 15.0.
        # *   Valid value when Engine is set to MariaDB: 10.3.
        # 
        # **Serverless instances. ApsaraDB RDS for MariaDB does not support serverless instances.**
        # 
        # *   Valid values when Engine is set to MySQL: 5.7 and 8.0.
        # *   Valid values when Engine is set to SQL Server: 2016_std_sl, 2017_std_sl, and 2019_std_sl.
        # *   Valid values when Engine is set to PostgreSQL: 14.0, 15.0, and 16.0.
        self.engine_version = engine_version
        # A reserved parameter.
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to enable the write optimization feature for the ApsaraDB RDS for MySQL instance. For more information, see [Use the write optimization feature](https://help.aliyun.com/document_detail/2858761.html). Valid values:
        # 
        # *   **optimized**: enables the feature.
        # *   **none**: disables the feature.
        self.optimized_writes = optimized_writes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        # *   **Serverless**: serverless. This value is not supported for ApsaraDB RDS for MariaDB instances.
        # 
        # >  If you want to set this parameter to Serverless, **you must specify **AutoPause, MaxCapacity, MinCapacity, and SwitchForce. For more information, see [Overview of serverless ApsaraDB RDS for MySQL instances](https://help.aliyun.com/document_detail/411291.html), [Overview of serverless ApsaraDB RDS for SQL Server instances](https://help.aliyun.com/document_detail/604344.html), and [Overview of serverless ApsaraDB RDS for PostgreSQL instances](https://help.aliyun.com/document_detail/607742.html).
        self.pay_type = pay_type
        # The coupon code.
        self.promotion_code = promotion_code
        # The specification of the read-only instance when you change the storage type of the ApsaraDB RDS for MySQL instance that runs RDS High-availability Edition from cloud disk to local disk.
        self.read_only_dbinstance_class = read_only_dbinstance_class
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specifications that you want to change for a serverless instance.
        self.serverless_configuration_shrink = serverless_configuration_shrink
        # A deprecated parameter. You do not need to specify this parameter.
        self.source_biz = source_biz
        # The time at which you want to change the specifications. **We recommend that you perform the specification changes during off-peak hours.**
        # 
        # Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > *   The time at which you want to change the specifications **must be later than the current time**. Otherwise, the specification change task fails. If the specification change task fails, you must wait for the order to be automatically canceled, and then call this operation again.
        # > *   If you want to increase the storage capacity or change the ESSD storage type between different PLs, the specification change immediately takes effect and does not affect your workloads. You do not need to specify this parameter.
        self.switch_time = switch_time
        # The minor engine version number of the ApsaraDB RDS for PostgreSQL instance. For more information, see [Update the minor engine version](https://help.aliyun.com/document_detail/126002.html). If the minor engine version does not support changing the instance type, you must specify the minor engine version to **update the minor engine version when you change the instance type**.
        # 
        # Format: `rds_postgres_<Major engine version>00_<Minor engine version>`. For example, if the instance runs PostgreSQL 12, set this parameter to `rds_postgres_1200_20200830`.
        self.target_minor_version = target_minor_version
        # The validity period of the specification changes on an ApsaraDB RDS for SQL Server instance. At the end of the validity period, the specifications of the instance are restored to the specifications that are used before an [elastic upgrade](https://help.aliyun.com/document_detail/95665.html) is performed. Unit: days.
        self.used_time = used_time
        # The vSwitch ID. The vSwitch must belong to the zone that is specified by **ZoneId**.
        # 
        # *   If you set **InstanceNetworkType** to **VPC**, you must also specify this parameter.
        # *   If you specify ZoneSlaveId1, you must specify the IDs of two vSwitches for this parameter and separate the IDs with a comma (,).
        # 
        # >  If you want to upgrade the major engine version of an ApsaraDB RDS for SQL Server instance by specifying AllowMajorVersionUpgrade or change the vSwitch, you must specify this parameter.
        self.v_switch_id = v_switch_id
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition.
        # *   **HighAvailability**: RDS High-availability Edition.
        # *   **AlwaysOn**: RDS Cluster Edition for SQL Server.
        # *   **Finance**: RDS Enterprise Edition. This edition is available only on the China site (aliyun.com).
        # 
        # > If you set **EngineVersion** to an SQL Server version number, you must also specify this parameter.
        self.zone_id = zone_id
        # The zone ID of the secondary instance. If you set this parameter to the same value as **ZoneId**, the single-zone deployment method is used. If you set this parameter to a different value from **ZoneId**, the multi-zone deployment method is used.
        # 
        # >  If you want to upgrade the major engine version of an ApsaraDB RDS for SQL Server instance by specifying AllowMajorVersionUpgrade or change the secondary zone, you must specify this parameter.
        self.zone_id_slave_1 = zone_id_slave_1

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_major_version_upgrade is not None:
            result['AllowMajorVersionUpgrade'] = self.allow_major_version_upgrade

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.cold_data_enabled is not None:
            result['ColdDataEnabled'] = self.cold_data_enabled

        if self.compression_mode is not None:
            result['CompressionMode'] = self.compression_mode

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.optimized_writes is not None:
            result['OptimizedWrites'] = self.optimized_writes

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.read_only_dbinstance_class is not None:
            result['ReadOnlyDBInstanceClass'] = self.read_only_dbinstance_class

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.serverless_configuration_shrink is not None:
            result['ServerlessConfiguration'] = self.serverless_configuration_shrink

        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_id_slave_1 is not None:
            result['ZoneIdSlave1'] = self.zone_id_slave_1

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowMajorVersionUpgrade') is not None:
            self.allow_major_version_upgrade = m.get('AllowMajorVersionUpgrade')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ColdDataEnabled') is not None:
            self.cold_data_enabled = m.get('ColdDataEnabled')

        if m.get('CompressionMode') is not None:
            self.compression_mode = m.get('CompressionMode')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('OptimizedWrites') is not None:
            self.optimized_writes = m.get('OptimizedWrites')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ReadOnlyDBInstanceClass') is not None:
            self.read_only_dbinstance_class = m.get('ReadOnlyDBInstanceClass')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ServerlessConfiguration') is not None:
            self.serverless_configuration_shrink = m.get('ServerlessConfiguration')

        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdSlave1') is not None:
            self.zone_id_slave_1 = m.get('ZoneIdSlave1')

        return self

