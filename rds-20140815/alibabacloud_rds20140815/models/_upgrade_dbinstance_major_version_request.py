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
        # Specifies when to execute statistics collection for the database.
        # Valid values:
        # - **Before**: collects statistics before the cutover. This ensures business stability. If the data volume of the instance is too large, the upgrade may take a long time.
        # - **After**: collects statistics after the cutover. This accelerates the instance upgrade. Accessing tables for which no statistics are generated after the upgrade may lead to inaccurate execution plans and even database breakdown during peak hours.
        # 
        # > For scenarios where no cutover is performed, collecting statistics before the cutover means collecting statistics before the new instance enables read and write operations, and collecting statistics after the cutover means collecting statistics after the new instance enables read and write operations.
        self.collect_stat_mode = collect_stat_mode
        # An internal reserved field. You do not need to specify this parameter.
        self.custom_extra_info = custom_extra_info
        # The instance type after the upgrade. The CPU and memory configurations must be greater than or equal to those of the original instance. When **UpgradeMode** is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, you **do not need to configure** this parameter.
        # 
        # For example, if the original instance type is `pg.n2.small.2c` with 1 core and 2 GB of memory, you can upgrade it to `pg.n2.medium.2c` with 2 cores and 4 GB of memory.
        # 
        # > For more information about ApsaraDB RDS for PostgreSQL instance types, see [Primary ApsaraDB RDS for PostgreSQL instance types](https://help.aliyun.com/document_detail/276990.html).
        self.dbinstance_class = dbinstance_class
        # The ID of the original instance.
        self.dbinstance_id = dbinstance_id
        # The instance storage after the upgrade. Unit: GB. When **UpgradeMode** (upgrade mode) is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, you **do not need to configure** this parameter.
        # 
        # Valid values:
        # - **ESSD PL1 cloud disk**: 20 GB to 3,200 GB
        # - **ESSD PL2 cloud disk**: 500 GB to 3,200 GB
        # - **ESSD PL3 cloud disk**: 1,500 GB to 3,200 GB
        # - **premium cloud disk**: 40 GB to 2,000 GB
        # 
        # > When you upgrade the major database version of an instance with premium local SSDs, storage capacity reduction is supported. For more information about the minimum storage capacity, see [Upgrade the major engine version](https://help.aliyun.com/document_detail/203309.html).
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance after the upgrade.
        # 
        # Valid values:
        # - **cloud_ssd**: standard SSD cloud disk
        # - **cloud_essd**: ESSD PL1 cloud disk
        # - **cloud_essd2**: ESSD PL2 cloud disk
        # - **cloud_essd3**: ESSD PL3 cloud disk
        # - **general_essd**: premium cloud disk
        # 
        # The major engine version upgrade feature is based on cloud disk snapshots. The following storage types are supported after the upgrade:
        # - When the original instance uses standard SSD cloud disks, you can select standard SSD cloud disks.
        # - When the original instance uses ESSD cloud disks, you can select ESSD PL1 cloud disks, ESSD PL2 cloud disks, ESSD PL3 cloud disks, or premium cloud disks.
        # - When the original instance uses premium local SSDs, you can select ESSD PL1 cloud disks, ESSD PL2 cloud disks, ESSD PL3 cloud disks, or premium cloud disks.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The network type of the instance after the upgrade. Set the value to VPC. Only VPC-connected instances support major engine version upgrades.
        # 
        # If the instance is connected to the classic network, switch the network type to VPC first. For more information about how to view or switch the network type, see [Switch the network type](https://help.aliyun.com/document_detail/96761.html).
        self.instance_network_type = instance_network_type
        # The billing method. Set the value to Postpaid, which indicates the pay-as-you-go billing method.
        # 
        # > If you want to change the billing method of the instance after the upgrade, see [Switch the billing method from pay-as-you-go to subscription](https://help.aliyun.com/document_detail/96743.html).
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # A reserved parameter. You do not need to configure this parameter.
        self.period = period
        # You do not need to configure this parameter. It specifies the internal IP address of the target instance. By default, the system automatically allocates an IP address based on the VPCId and vSwitchId parameters.
        self.private_ip_address = private_ip_address
        self.resource_owner_id = resource_owner_id
        # The cutover configuration. Specifies whether to switch traffic to the new-version instance based on your business requirements.
        # 
        # Valid values:
        # - **true**: performs the cutover and automatic switchover. This option is generally used to execute a formal upgrade after you confirm that your business can run stably on the new version.
        # - **false**: does not perform the cutover and does not perform automatic switchover. This option is generally used to test the compatibility of your current business with the new version before a formal upgrade.
        # 
        # > - If you choose to perform the cutover:
        # >     - Backoff is not supported after the cutover. Proceed with caution.
        # >     - During the switchover procedure, the original instance becomes read-only and your business cannot write data to the instance. Make sure that you execute the cutover during off-peak hours.
        # >     - If read-only instances are attached to the original instance, you cannot perform the cutover. You can only upgrade the instance without performing the cutover, and the original read-only instances are not cloned. After the upgrade is complete, you must create PostgreSQL read-only instances for the new-version instance.
        # > - If you choose not to perform the cutover:
        # >     - Your business on the original instance is not affected during the migration.
        # >     - If you upgrade the instance without performing the cutover, you must change the database endpoint in your application to the endpoint of the new instance after the migration is complete. For more information about how to view the endpoint, see [View or change the internal and public endpoints and port numbers](https://help.aliyun.com/document_detail/96788.html).
        self.switch_over = switch_over
        # A reserved parameter. You do not need to configure this parameter.
        self.switch_time = switch_time
        # The cutover time. This parameter is used together with SwitchOver and takes effect only when **SwitchOver** is set to **true**.
        # 
        # Valid values:
        # - **Immediate**: The cutover takes effect immediately.
        # - **MaintainTime**: The cutover takes effect within the maintenance window. You can call the ModifyDBInstanceMaintainTime operation to modify the maintenance window.
        self.switch_time_mode = switch_time_mode
        # The target major engine version after the upgrade. The value must be the same as the target version specified when you perform the pre-upgrade check.
        # 
        # > You can call the UpgradeDBInstanceMajorVersionPrecheck operation to perform a pre-upgrade check for a major engine version upgrade.
        self.target_major_version = target_major_version
        # The upgrade mode. When **SwitchOver** is set to **true**, you must configure this parameter. Valid values:
        # 
        # - **inPlaceUpgrade**: in-place upgrade. The major engine version upgrade task is executed on the original instance, and no new-version instance is created. The major engine version of the original instance is upgraded, and the original instance inherits the existing orders, instance name, tags, CloudMonitor alert rules, and backup rules.
        # - **blueGreenDeployment**: blue-green deployment. The major engine version upgrade retains the original instance and creates a new-version instance. You are not charged for the new instance while it is being created, but you are charged after it is created, and the billing method may change. After the upgrade is complete, both the original instance and the new instance incur fees, and the new instance does not enjoy the discounts of the original instance.
        # - **zeroDownTimeUpgrade**: zero-downtime upgrade. The system uses pg_upgrade to upgrade the original instance to the target version and implements incremental updates through native logical replication. Manual switchover is supported during the upgrade procedure, and you can verify the higher-version instance before the switchover. From the start of the upgrade to the manual switchover, the instance can maintain normal read and write operations. During the switchover, the read-only duration of the instance is measured in seconds.
        self.upgrade_mode = upgrade_mode
        # A reserved parameter. You do not need to configure this parameter.
        self.used_time = used_time
        # The VPC ID. When **UpgradeMode** is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, you **do not need to configure** this parameter.
        # 
        # You can call the DescribeDBInstanceAttribute operation to view the VPC ID of the original instance.
        self.vpcid = vpcid
        # The vSwitch ID of the target instance. When **UpgradeMode** (upgrade mode) is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, you **do not need to configure** this parameter.
        # - When the original instance is a Basic Edition instance, configure the vSwitch ID of the target instance.
        # - When the original instance is a high availability instance, you can configure the vSwitch IDs of the target primary and secondary instances, separated by commas (,).
        # 
        # > The configured vSwitch of the target instance must be in the same zone as the original instance. You can call the DescribeVSwitches operation to query the vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the destination primary zone. When **UpgradeMode** is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, you **do not need to configure** this parameter.
        # 
        # You can call the DescribeRegions operation to view the zone ID.
        # 
        # ApsaraDB RDS for PostgreSQL allows you to configure the new instance in a different zone within the same region as the original instance after the upgrade.
        self.zone_id = zone_id
        # The ID of the secondary zone of the target instance. This parameter is available only when the original instance is a high availability instance. When **UpgradeMode** (upgrade mode) is set to **inPlaceUpgrade** or **zeroDownTimeUpgrade**, you **do not need to configure** this parameter.
        # 
        # ApsaraDB RDS for PostgreSQL allows you to configure the new secondary instance in a different zone within the same region as the original instance after the upgrade.
        # 
        # You can call the DescribeRegions operation to view the zone ID.
        self.zone_id_slave_1 = zone_id_slave_1
        # A reserved parameter. You do not need to configure this parameter.
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

