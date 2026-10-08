# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyDBInstanceSpecRequest(DaraModel):
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
        serverless_configuration: main_models.ModifyDBInstanceSpecRequestServerlessConfiguration = None,
        source_biz: str = None,
        switch_time: str = None,
        target_minor_version: str = None,
        used_time: int = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
    ):
        self.allocate_strategy = allocate_strategy
        # Specifies whether to enable [major engine version upgrade](https://help.aliyun.com/document_detail/127458.html) for the SQL Server instance. Valid values:
        self.allow_major_version_upgrade = allow_major_version_upgrade
        # Specifies whether to use coupons to offset fees. Valid values:
        self.auto_use_coupon = auto_use_coupon
        # Specifies whether to enable the [I/O performance burst feature for Premium ESSDs](https://help.aliyun.com/document_detail/2340501.html). Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.bursting_enabled = bursting_enabled
        # The [instance edition](https://help.aliyun.com/document_detail/53509.html). Valid values:
        # > This parameter is required if **EngineVersion** is set to a SQL Server version number.
        # <details>
        # <summary>Regular ApsaraDB RDS instances</summary>
        # 
        # - **Basic**: Basic Edition
        # - **HighAvailability**: High-availability Edition
        # - **AlwaysOn**: SQL Server Cluster Edition
        # - **Cluster**: MySQL Cluster Edition.
        # - <props="china">**Finance**: Enterprise Edition
        # 
        # </details>
        # 
        # <details>
        # <summary>Serverless ApsaraDB RDS instances (not supported for MariaDB)</summary>
        # 
        # - **serverless_basic**: Serverless Basic Edition (applicable only to MySQL and PostgreSQL)
        # - **serverless_standard**: Serverless High-availability Edition (applicable only to MySQL and PostgreSQL)
        # - **serverless_ha**: Serverless High-availability Edition (applicable only to SQL Server)
        # 
        # </details>
        self.category = category
        # The [cold data archiving feature](https://help.aliyun.com/document_detail/2701832.html) for premium performance disks. Valid values:
        self.cold_data_enabled = cold_data_enabled
        # The MySQL [storage compression feature](https://help.aliyun.com/document_detail/2861985.html). Valid values:
        self.compression_mode = compression_mode
        # The [target instance type](https://help.aliyun.com/document_detail/26312.html). You can call [DescribeAvailableClasses](https://help.aliyun.com/document_detail/610393.html) to query the instance types to which the instance can be changed.
        self.dbinstance_class = dbinstance_class
        # The instance ID. You can call [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The [target storage capacity](https://help.aliyun.com/document_detail/26312.html). Unit: GB. You can call [DescribeAvailableClasses](https://help.aliyun.com/document_detail/610393.html) to query the available storage capacity range for the target instance type.
        self.dbinstance_storage = dbinstance_storage
        # The instance storage type. Valid values:
        self.dbinstance_storage_type = dbinstance_storage_type
        # The dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The type of specification change. Valid values:
        # 
        # - **Up** (default): upgrade of a subscription instance or upgrade/downgrade of a pay-as-you-go instance.
        # - **Down**: downgrade of a subscription instance.
        # - **TempUpgrade**: elastic specification change of a subscription ApsaraDB RDS for SQL Server instance. This value is required for elastic specification changes.
        # - **Serverless**: configuration of elastic settings for a serverless instance.
        # 
        # > If you want to change only the **DBInstanceStorageType** parameter, for example, from standard SSD to ESSD, leave this parameter empty.
        self.direction = direction
        # The time when the new configurations take effect. Valid values:
        # > **Changing certain configurations may affect the instance**. Read the [impact section in the feature documentation](https://help.aliyun.com/document_detail/96061.html) before configuring this parameter. Perform this operation during off-peak hours.
        # * **Immediate** (default): The new configurations take effect immediately.
        # * **MaintainTime**: The new configurations take effect during the [maintenance window](https://help.aliyun.com/document_detail/610402.html).
        # * **ScheduleTime**: The new configurations take effect at a specified time. The specified time must be at least 12 hours later than the current time. The actual switchover time follows the rule: EffectiveTime = ScheduleTime + SwitchTime.
        self.effective_time = effective_time
        # The database engine version. Valid values:
        # <details>
        # <summary>Regular ApsaraDB RDS instances</summary>
        # 
        # - MySQL: 5.5, 5.6, 5.7, 8.0
        # - SQL Server: 2008r2, 08r2_ent_ha, 2012, 2012_ent_ha, 2012_std_ha, 2012_web, 2014_std_ha, 2016_ent_ha, 2016_std_ha, 2016_web, 2017_std_ha, 2017_ent, 2019_std_ha, 2019_ent, 2022_web, 2022_std_ha, 2022_ent, 2025_std, 2025_ent
        # - PostgreSQL: 10.0, 11.0, 12.0, 13.0, 14.0, 15.0
        # - MariaDB: 10.3
        # 
        # </details>
        # 
        # <details>
        # <summary>Serverless ApsaraDB RDS instances (MariaDB is not supported)</summary>
        # 
        # - MySQL: 5.7, 8.0
        # - SQL Server: 2016_std_sl, 2017_std_sl, 2019_std_sl
        # - PostgreSQL: 14.0, 15.0, 16.0
        # 
        # </details>
        self.engine_version = engine_version
        # The [Buffer Pool Extension (BPE) feature](https://help.aliyun.com/document_detail/2527067.html) for premium performance disks. Valid values:
        # 
        # -  **1**: Enabled.
        # -  **0**: Not enabled.
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to enable the MySQL [16KB atomic write feature](https://help.aliyun.com/document_detail/2858761.html). Valid values:
        self.optimized_writes = optimized_writes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        # - **Serverless** (not supported for MariaDB instances): serverless billing method.
        # 
        # > To change the billing method to Serverless, you **must configure the following parameters**: automatic start and stop (AutoPause), scaling range (MaxCapacity and MinCapacity), and elastic policy (SwitchForce). For more information, see [Introduction to MySQL Serverless instances](https://help.aliyun.com/document_detail/411291.html), [Introduction to SQL Server Serverless instances](https://help.aliyun.com/document_detail/604344.html), and [Introduction to PostgreSQL Serverless instances](https://help.aliyun.com/document_detail/607742.html).
        self.pay_type = pay_type
        # The coupon code.
        self.promotion_code = promotion_code
        # The [target instance type of read-only instances](https://help.aliyun.com/document_detail/276980.html) when you perform an Upgrade/Downgrade to change a MySQL high availability (HA) instance with Premium Local SSDs to a cloud disk instance. This parameter is active only when the instance meets the requirements.
        self.read_only_dbinstance_class = read_only_dbinstance_class
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The serverless instance configuration for the specification change.
        self.serverless_configuration = serverless_configuration
        # A deprecated parameter. You do not need to configure this parameter.
        self.source_biz = source_biz
        # The time at which the specification change is performed. **Perform the specification change during off-peak hours.**
        self.switch_time = switch_time
        # The [minor engine version](https://help.aliyun.com/document_detail/126002.html) of the PostgreSQL instance. If the specification change fails because the minor engine version is not supported, specify this parameter to **upgrade the minor engine version during the specification change**.
        self.target_minor_version = target_minor_version
        # The duration of the SQL Server [elastic upgrade](https://help.aliyun.com/document_detail/95665.html). Unit: days.
        self.used_time = used_time
        # The vSwitch ID. The zone of the vSwitch must correspond to the zone ID specified in **ZoneId**.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id
        # The zone ID of the secondary node. If this value is the same as **ZoneId**, the instance uses single-zone deployment. If this value is different from **ZoneId**, the instance uses multi-zone deployment.
        self.zone_id_slave_1 = zone_id_slave_1

    def validate(self):
        if self.serverless_configuration:
            self.serverless_configuration.validate()

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

        if self.serverless_configuration is not None:
            result['ServerlessConfiguration'] = self.serverless_configuration.to_map()

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
            temp_model = main_models.ModifyDBInstanceSpecRequestServerlessConfiguration()
            self.serverless_configuration = temp_model.from_map(m.get('ServerlessConfiguration'))

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

class ModifyDBInstanceSpecRequestServerlessConfiguration(DaraModel):
    def __init__(
        self,
        auto_pause: bool = None,
        max_capacity: float = None,
        min_capacity: float = None,
        switch_force: bool = None,
    ):
        # The [intelligent suspension and startup](https://help.aliyun.com/document_detail/2838448.html) feature for MySQL Serverless or PostgreSQL Serverless instances. Valid values:
        self.auto_pause = auto_pause
        # The **maximum** value of the automatic scaling range for RCUs of the serverless instance. Valid values:
        self.max_capacity = max_capacity
        # The **minimum** value of the automatic scaling range for RCUs of the serverless instance. Valid values:
        self.min_capacity = min_capacity
        # Specifies whether to enable forced scaling for MySQL Serverless or PostgreSQL Serverless instances. Elastic scaling of instance RCUs usually takes effect immediately, but in certain special cases (such as during large transaction execution), scaling cannot be completed instantly. In such cases, you can enable this parameter to force scaling. Valid values:
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

        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        if self.switch_force is not None:
            result['SwitchForce'] = self.switch_force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPause') is not None:
            self.auto_pause = m.get('AutoPause')

        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        if m.get('SwitchForce') is not None:
            self.switch_force = m.get('SwitchForce')

        return self

