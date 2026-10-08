# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBInstanceMajorVersionRequest(DaraModel):
    def __init__(
        self,
        allow_ddl: bool = None,
        collect_stat_mode: str = None,
        custom_extra_info: str = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        instance_network_type: str = None,
        pay_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        resource_owner_id: int = None,
        switch_over: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_major_version: str = None,
        upgrade_mode: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
        zone_id_slave_2: str = None,
    ):
        self.allow_ddl = allow_ddl
        # Specifies when to execute statistics information collection on the database.
        # - **Before**: Execute collection before the switchover. This ensures business stability. If the instance has a large data volume, the upgrade may take a long time.
        # - **After**: Execute collection after the switchover. The upgrade is faster. Accessing tables without generated statistics information after the upgrade may cause inaccurate execution plans. During peak hours, this may cause the database to break down.
        # 
        # > For non-switchover scenarios, "before switchover" means statistics information is collected before the new instance is opened for read/write, and "after switchover" means statistics information is collected after the new instance is opened for read/write.
        self.collect_stat_mode = collect_stat_mode
        self.custom_extra_info = custom_extra_info
        # The instance type after the upgrade. The CPU and memory configurations must be greater than or equal to those of the original instance type. If **UpgradeMode** is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, **you do not need to configure** this parameter.
        # 
        # For example, if the original instance type is `pg.n2.small.2c` with 1 CPU core and 2 GB of memory, you can upgrade it to `pg.n2.medium.2c` with 2 CPU cores and 4 GB of memory.
        # 
        # > For the instance type codes of ApsaraDB RDS for PostgreSQL, refer to [Primary ApsaraDB RDS for PostgreSQL instance types](https://help.aliyun.com/document_detail/276990.html).
        self.dbinstance_class = dbinstance_class
        # The instance ID of the original instance.
        self.dbinstance_id = dbinstance_id
        # The instance storage capacity after the upgrade. Unit: GB. If **UpgradeMode** (upgrade pattern) is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, **you do not need to configure** this parameter.
        # 
        # Valid values:
        # - **PL1 ESSD cloud disk**: 20 GB to 3200 GB
        # - **PL2 ESSD cloud disk**: 500 GB to 3200 GB
        # - **PL3 ESSD cloud disk**: 1500 GB to 3200 GB
        # - **Premium performance disk**: 40 GB to 2000 GB
        # 
        # > When upgrading the major engine version of an instance with Premium Local SSDs, storage capacity reduction is supported. For the minimum storage capacity, refer to [Upgrade the major engine version of a database](https://help.aliyun.com/document_detail/203309.html).
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance after the upgrade.
        # 
        # Valid values:
        # - **cloud_ssd**: standard SSD
        # - **cloud_essd**: PL1 ESSD
        # - **cloud_essd2**: PL2 ESSD
        # - **cloud_essd3**: PL3 ESSD
        # - **general_essd**: premium performance disk
        # 
        # 
        # The major engine version upgrade feature is based on cloud disk snapshots. The supported storage types after the upgrade are as follows:
        # - If the original instance uses a standard SSD, you can select standard SSD.
        # - If the original instance uses an ESSD cloud disk, you can select PL1 ESSD, PL2 ESSD, PL3 ESSD, or premium performance disk.
        # - If the original instance uses Premium Local SSDs, you can select PL1 ESSD, PL2 ESSD, PL3 ESSD, or premium performance disk.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The network type of the instance after the upgrade. Set this parameter to VPC. Only VPC-connected instances support major engine version upgrades.
        # 
        # If the network type is classic network, switch to VPC first. For information about how to view or switch the network type, refer to [Switch the network type](https://help.aliyun.com/document_detail/96761.html).
        self.instance_network_type = instance_network_type
        # The billing method of the instance. Set this parameter to Postpaid for pay-as-you-go billing.
        # 
        # > If you want to change the billing method after the upgrade, refer to [Switch from pay-as-you-go to subscription](https://help.aliyun.com/document_detail/96743.html).
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # Reserved parameter. You do not need to configure this parameter.
        self.period = period
        # You do not need to configure this parameter. It specifies the internal IP address of the target instance. The system automatically assigns an IP address based on VPCId and vSwitchId by default.
        self.private_ip_address = private_ip_address
        self.resource_owner_id = resource_owner_id
        # The switchover configuration. Specifies whether to switch traffic to the new version instance based on your business requirements.
        # 
        # Valid values:
        # 
        # - **true**: Switchover is performed and automatic switchover is enabled. This option is typically used to execute the formal upgrade after confirming that your business can run stably on the new version.
        # - **false**: Switchover is not performed and automatic switchover is not enabled. This option is typically used to test the compatibility of your application with the new version before the formal upgrade.
        # 
        # > - If you select switchover:
        # >     - Switchover cannot be rolled back after execution. Proceed with caution.
        # >     - During the switchover procedure, the original instance becomes read-only and writes are not allowed. Execute the switchover during off-peak hours.
        # >     - If read-only instances are created for the original instance, you cannot select switchover. You can only upgrade the instance without switchover, and the original read-only instances are not cloned. After the upgrade, create new PostgreSQL read-only instances for the new version instance.
        # > - If you do not select switchover:
        # >     - The business on the original instance is not affected during migration.
        # >     - To upgrade the instance without switchover, change the database connection address in your application to the database connection address of the new instance after migration is complete. For information about how to view the connection address, refer to [View or modify the internal and public endpoints and port numbers](https://help.aliyun.com/document_detail/96788.html).
        self.switch_over = switch_over
        # Reserved parameter. You do not need to configure this parameter.
        self.switch_time = switch_time
        # This parameter is used together with SwitchOver and takes effect only when **SwitchOver** is set to **true**. Specifies the switchover time.
        # 
        # Valid values:
        # - **Immediate**: The switchover takes effect immediately.
        # - **MaintainTime**: The switchover takes effect during the maintenance window. You can call the ModifyDBInstanceMaintainTime operation to modify the maintenance window.
        self.switch_time_mode = switch_time_mode
        # The target major engine version of the instance after the upgrade. This value must be the same as the target version specified during the pre-upgrade check.
        # 
        # > You can call the UpgradeDBInstanceMajorVersionPrecheck operation to perform a pre-upgrade check for the major engine version upgrade.
        self.target_major_version = target_major_version
        # The upgrade pattern. Configure this parameter when **SwitchOver** is set to **true**. Valid values:
        # 
        # - **inPlaceUpgrade**: In-place upgrade. The major engine version upgrade task is executed on the original instance without creating a new version instance. After the upgrade, the original instance inherits the existing order, instance name, tags, CloudMonitor alert rules, and backup rules.
        # - **blueGreenDeployment**: Blue-green deployment. The major engine version upgrade retains the original instance and creates a new version instance. The new instance is free of charge during creation. After the new instance is created, fees are incurred and the billing method may change. After the upgrade, both the original and new instances incur fees, and the new instance does not inherit the discounts of the original instance.
        # - **zeroDownTimeUpgrade**: Zero-downtime upgrade. The system uses pg_upgrade to upgrade the original instance to the target version and uses native logical replication for incremental updates. Active switchover is supported during the upgrade procedure, and you can validate the higher version instance before the switchover. From the start of the upgrade until the active switchover, the instance maintains normal read/write operations. During the switchover, the read-only duration is at the second level.
        self.upgrade_mode = upgrade_mode
        # Reserved parameter. You do not need to configure this parameter.
        self.used_time = used_time
        # The VPC ID. If **UpgradeMode** is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, **you do not need to configure** this parameter.
        # 
        # You can call the DescribeDBInstanceAttribute operation to query the VPC ID of the original instance.
        self.vpcid = vpcid
        # The vSwitch ID of the target instance. If **UpgradeMode** (upgrade pattern) is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, **you do not need to configure** this parameter.
        # - If the original instance is a Basic Edition instance, specify the vSwitch ID of the target instance.
        # - If the original instance is a high-availability series instance, you can specify the vSwitch IDs of the target primary and secondary instances, separated by commas (,).
        # 
        # > The target vSwitch must be in the same zone as the original instance. You can call the DescribeVSwitches operation to query vSwitches.
        self.v_switch_id = v_switch_id
        # The primary zone ID of the target instance. If **UpgradeMode** is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, **you do not need to configure** this parameter.
        # 
        # You can call the DescribeRegions operation to query zone IDs.
        # 
        # ApsaraDB RDS for PostgreSQL allows you to deploy the new instance in a different zone within the same region as the original instance after the upgrade.
        self.zone_id = zone_id
        # This parameter can be configured only when the original instance is a high-availability series instance. Specifies the secondary zone ID of the target instance. If **UpgradeMode** (upgrade pattern) is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, **you do not need to configure** this parameter.
        # 
        # ApsaraDB RDS for PostgreSQL allows you to deploy the new secondary instance in a different zone within the same region as the original instance after the upgrade.
        # 
        # You can call the DescribeRegions operation to query zone IDs.
        self.zone_id_slave_1 = zone_id_slave_1
        # Reserved parameter. You do not need to configure this parameter.
        self.zone_id_slave_2 = zone_id_slave_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_ddl is not None:
            result['AllowDDL'] = self.allow_ddl

        if self.collect_stat_mode is not None:
            result['CollectStatMode'] = self.collect_stat_mode

        if self.custom_extra_info is not None:
            result['CustomExtraInfo'] = self.custom_extra_info

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_over is not None:
            result['SwitchOver'] = self.switch_over

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        if self.target_major_version is not None:
            result['TargetMajorVersion'] = self.target_major_version

        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_id_slave_1 is not None:
            result['ZoneIdSlave1'] = self.zone_id_slave_1

        if self.zone_id_slave_2 is not None:
            result['ZoneIdSlave2'] = self.zone_id_slave_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowDDL') is not None:
            self.allow_ddl = m.get('AllowDDL')

        if m.get('CollectStatMode') is not None:
            self.collect_stat_mode = m.get('CollectStatMode')

        if m.get('CustomExtraInfo') is not None:
            self.custom_extra_info = m.get('CustomExtraInfo')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchOver') is not None:
            self.switch_over = m.get('SwitchOver')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        if m.get('TargetMajorVersion') is not None:
            self.target_major_version = m.get('TargetMajorVersion')

        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdSlave1') is not None:
            self.zone_id_slave_1 = m.get('ZoneIdSlave1')

        if m.get('ZoneIdSlave2') is not None:
            self.zone_id_slave_2 = m.get('ZoneIdSlave2')

        return self

