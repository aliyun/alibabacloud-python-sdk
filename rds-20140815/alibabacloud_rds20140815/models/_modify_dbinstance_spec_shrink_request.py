# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSpecShrinkRequest(DaraModel):
    def __init__(
        self,
        allocate_strategy: str = None,
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
        self.allocate_strategy = allocate_strategy
        # Specifies whether to perform a [major engine version upgrade](https://help.aliyun.com/document_detail/127458.html) for the ApsaraDB RDS for SQL Server instance. Valid values:
        # - **true**: performs the upgrade.
        # - **false** (default): does not perform the upgrade.
        # 
        # > - When you perform a major engine version upgrade, you must also specify other required parameters, including DBInstanceId, EngineVersion, DBInstanceClass, Category, ZoneId, and VSwitchId.
        # > - If you want to upgrade the instance to the High-availability Edition or Cluster Edition, you must also specify the ZoneIdSlave1 parameter.
        self.allow_major_version_upgrade = allow_major_version_upgrade
        # Specifies whether to use vouchers to offset fees. Valid values:
        # 
        # - **true** (default): uses vouchers.
        # - **false**: does not use vouchers.
        self.auto_use_coupon = auto_use_coupon
        # Specifies whether to enable the [I/O performance burst feature for Premium ESSDs](https://help.aliyun.com/document_detail/2340501.html). Valid values:
        # 
        # - **true**: enables the feature.
        # - **false**: disables the feature.
        self.bursting_enabled = bursting_enabled
        # The [instance edition](https://help.aliyun.com/document_detail/53509.html). Valid values:
        # > This parameter is required when **EngineVersion** is set to a SQL Server version number.
        # <details>
        # <summary>Regular ApsaraDB RDS instances</summary>
        # 
        # - **Basic**: Basic Edition
        # - **HighAvailability**: High-availability Edition
        # - **AlwaysOn**: SQL Server Cluster Edition
        # - **Cluster**: MySQL Cluster Edition
        # - <props="china">**Finance**: Enterprise Edition
        # 
        # </details>
        # 
        # <details>
        # <summary>Serverless ApsaraDB RDS instances (not supported for MariaDB)</summary>
        # 
        # - **serverless_basic**: Serverless Basic Edition (MySQL and PostgreSQL only)
        # - **serverless_standard**: Serverless High-availability Edition (MySQL and PostgreSQL only)
        # - **serverless_ha**: Serverless High-availability Edition (SQL Server only)
        # 
        # </details>
        self.category = category
        # Specifies whether to enable the [data archiving feature for Premium ESSDs](https://help.aliyun.com/document_detail/2701832.html). Valid values:
        # 
        # - **true**: enables the feature.
        # 
        # - **false**: disables the feature.
        self.cold_data_enabled = cold_data_enabled
        # Specifies whether to enable the [storage compression feature](https://help.aliyun.com/document_detail/2861985.html) for ApsaraDB RDS for MySQL. Valid values:
        # 
        # - **on**: enables the feature.
        # - **off**: disables the feature.
        self.compression_mode = compression_mode
        # The [target instance type](https://help.aliyun.com/document_detail/26312.html). You can call the [DescribeAvailableClasses](https://help.aliyun.com/document_detail/610393.html) operation to query the available instance types for specification changes.
        # 
        # > * You must specify at least one of this parameter and **DBInstanceStorage**.
        # > * You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/610394.html) operation to view the current instance type.
        self.dbinstance_class = dbinstance_class
        # The instance ID. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The [target storage capacity](https://help.aliyun.com/document_detail/26312.html). Unit: GB. You can call the [DescribeAvailableClasses](https://help.aliyun.com/document_detail/610393.html) operation to query the available storage capacity range for the target instance type.
        # 
        # > * You must specify at least one of this parameter and **DBInstanceClass**.
        # > * You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/610394.html) operation to view the current storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage
        # The instance storage type. Valid values:
        # * **local_ssd**: premium local SSD
        # * **cloud_ssd**: standard SSD (not recommended. Sales have stopped in some regions)
        # * **cloud_essd**: PL1 ESSD
        # * **cloud_essd2**: PL2 ESSD
        # * **cloud_essd3**: PL3 ESSD
        # * **general_essd**: Premium ESSD
        # 
        # If you want to change the instance storage type, take note of the following items:
        # <props="china">* If you change the instance storage type from ESSD to Premium ESSD, other parameters such as the instance type and storage capacity must remain the same as the original values and cannot be modified.
        # 
        # <props="china">* For ApsaraDB RDS for MySQL or MariaDB instances whose instance storage type is standard SSD, you can set this parameter to `cloud_essd` to [upgrade the instance storage type to ESSD](https://help.aliyun.com/document_detail/314678.html). To perform the upgrade, you must specify both **DBInstanceClass** and **DBInstanceStorage**, and their values must be the same as the current values of the instance.
        # 
        # <props="china">* For ApsaraDB RDS for PostgreSQL instances, you can upgrade standard SSDs to [ESSDs of any PL](https://help.aliyun.com/document_detail/96750.html), but **you cannot downgrade ESSDs to standard SSDs**.
        # 
        # <props="intl">For ApsaraDB RDS for PostgreSQL instances, you can upgrade standard SSDs to [ESSDs of any PL](https://help.aliyun.com/document_detail/96750.html), but **you cannot downgrade ESSDs to standard SSDs**.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The type of the specification change. Valid values:
        # 
        # - **Up** (default): upgrade for subscription instances, and upgrade or downgrade for pay-as-you-go instances.
        # - **Down**: downgrade for subscription instances.
        # - **TempUpgrade**: elastic specification change for subscription ApsaraDB RDS for SQL Server instances. This value is required for elastic specification changes.
        # - **Serverless**: configuration for adjusting the elastic settings of serverless instances.
        # 
        # > If you only change the **DBInstanceStorageType** parameter, such as changing standard SSDs to ESSDs, leave this parameter empty.
        self.direction = direction
        # The effective time of the new configurations. Valid values:
        # > **Changing some configurations may affect the instance**. Read the [Impact section in the feature documentation](https://help.aliyun.com/document_detail/96061.html) carefully before you configure this parameter. We recommend that you do this during off-peak hours.
        # * **Immediate** (default): takes effect immediately.
        # * **MaintainTime**: takes effect within the [maintenance window](https://help.aliyun.com/document_detail/610402.html).
        # * **ScheduleTime**: takes effect at a specified time. The specified time must be at least 12 hours later than the current time, and the actual switchover time follows the formula: EffectiveTime = ScheduleTime + SwitchTime.
        self.effective_time = effective_time
        # The database engine version. Valid values:
        # <details>
        # <summary>Regular ApsaraDB RDS instances</summary>
        # 
        # - MySQL: 5.5, 5.6, 5.7, and 8.0
        # - SQL Server: 2008r2, 08r2_ent_ha, 2012, 2012_ent_ha, 2012_std_ha, 2012_web, 2014_std_ha, 2016_ent_ha, 2016_std_ha, 2016_web, 2017_std_ha, 2017_ent, 2019_std_ha, 2019_ent, 2022_web, 2022_std_ha, 2022_ent, 2025_std, and 2025_ent
        # - PostgreSQL: 10.0, 11.0, 12.0, 13.0, 14.0, and 15.0
        # - MariaDB: 10.3
        # 
        # </details>
        # 
        # <details>
        # <summary>Serverless ApsaraDB RDS instances (not supported for MariaDB)</summary>
        # 
        # - MySQL: 5.7 and 8.0
        # - SQL Server: 2016_std_sl, 2017_std_sl, and 2019_std_sl
        # - PostgreSQL: 14.0, 15.0, and 16.0
        # 
        # </details>
        self.engine_version = engine_version
        # Specifies whether to enable the [Buffer Pool Extension (BPE) feature for Premium ESSDs](https://help.aliyun.com/document_detail/2527067.html). Valid values:
        # 
        # -  **1**: enables the feature.
        # -  **0**: disables the feature.
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to enable the [16KB atomic write feature](https://help.aliyun.com/document_detail/2858761.html) for ApsaraDB RDS for MySQL. Valid values:
        # 
        # - **optimized**: enables the feature.
        # - **none**: disables the feature.
        self.optimized_writes = optimized_writes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The current billing method of the instance. Valid values:
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        # - **Serverless** (not supported for ApsaraDB RDS for MariaDB instances): serverless.
        # 
        # > To change the billing method to serverless, **you must configure** the auto-start and auto-stop (AutoPause), scaling range (MaxCapacity and MinCapacity), and elastic policy (SwitchForce) in subsequent parameters. For more information, see [Overview of serverless ApsaraDB RDS for MySQL instances](https://help.aliyun.com/document_detail/411291.html), [Overview of serverless ApsaraDB RDS for SQL Server instances](https://help.aliyun.com/document_detail/604344.html), and [Overview of serverless ApsaraDB RDS for PostgreSQL instances](https://help.aliyun.com/document_detail/607742.html).
        self.pay_type = pay_type
        # The coupon code.
        self.promotion_code = promotion_code
        # The [target instance type of the read-only instance](https://help.aliyun.com/document_detail/276980.html) when you change an ApsaraDB RDS for MySQL High-availability Edition instance with premium local SSDs to a cloud disk instance.
        self.read_only_dbinstance_class = read_only_dbinstance_class
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The configurations for changing the serverless instance.
        self.serverless_configuration_shrink = serverless_configuration_shrink
        # **[Deprecated]** This parameter is deprecated and does not need to be configured.
        self.source_biz = source_biz
        # The time when the specification change is performed. **We recommend that you perform the specification change during off-peak hours**.
        # 
        # Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        # 
        # > - The specified time **must be later than the current time** (the time when the call is initiated). Otherwise, the specification change task will fail. After the task fails, you must wait for the order to be automatically canceled before you can initiate the call again.
        # > - If you only increase the storage capacity or change the ESSD storage type, the specification change is performed immediately after submission because it does not affect your business. You do not need to configure this parameter.
        self.switch_time = switch_time
        # The [minor engine version](https://help.aliyun.com/document_detail/126002.html) of the ApsaraDB RDS for PostgreSQL instance. When you change the instance type and an error indicates that the minor engine version is not supported, you must specify the minor engine version **to upgrade the minor engine version during the instance type change**.
        # 
        # Format: `rds_postgres_<Major version>00_<Minor version>`. For example, for version 12 and minor version 20200830: `rds_postgres_1200_20200830`.
        self.target_minor_version = target_minor_version
        # The duration of the [elastic upgrade](https://help.aliyun.com/document_detail/95665.html) for the ApsaraDB RDS for SQL Server instance. Unit: days.
        self.used_time = used_time
        # The vSwitch ID. The zone where the vSwitch resides must correspond to the zone ID specified in **ZoneId**.
        # 
        # - The network type (**InstanceNetworkType**) must be **VPC**.
        # - If you specify ZoneSlaveId1 (the secondary zone ID), you must specify two vSwitch IDs and separate them with a comma (,).
        # > You only need to specify the vSwitch when you upgrade the major engine version of an ApsaraDB RDS for SQL Server instance (AllowMajorVersionUpgrade) or when you switch the vSwitch.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id
        # The zone ID of the secondary node. If this value is the same as the value of **ZoneId**, it is a single-zone deployment. If this value is different from the value of **ZoneId**, it is a multi-zone deployment.
        # > You only need to specify the secondary zone when you upgrade the major engine version of an ApsaraDB RDS for SQL Server instance (AllowMajorVersionUpgrade), or you need to configure this parameter when switching the secondary zone.
        self.zone_id_slave_1 = zone_id_slave_1

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_strategy is not None:
            result['AllocateStrategy'] = self.allocate_strategy

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
        if m.get('AllocateStrategy') is not None:
            self.allocate_strategy = m.get('AllocateStrategy')

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

