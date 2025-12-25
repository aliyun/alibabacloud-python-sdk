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
        # Specify the point in time at which the system collects the statistics of the instance.
        # 
        # *   **Before**: The system collects the statistics of the instance before the switchover to ensure service stability. If the instance contains a large amount of data, the upgrade may require a long period of time.
        # *   **After**: The system collects the statistics of the instance after the switchover to accelerate the upgrade. After the upgrade, if you access tables for which no statistics are generated, the query plans may be inaccurate, and your database service may be unavailable during peak hours.
        # 
        # >  If you set the SwitchOver parameter to false, the value Before specifies that the system collects the statistics of the instance before the instance starts to process read and write requests, and the value After specifies that the system collects the statistics of the instance after the instance starts to process read and write requests.
        self.collect_stat_mode = collect_stat_mode
        self.custom_extra_info = custom_extra_info
        # The new instance type of the instance. The new CPU and memory specifications of the instance must be higher than or equal to the original CPU and memory specifications. If you set the **UpgradeMode** parameter to **inPlaceUpgrade**, you **do not need to configure** this parameter.
        # 
        # For example, you can upgrade the instance type from `pg.n2.small.2c` to `pg.n2.medium.2c`. The pg.n2.small.2c instance type provides 1 CPU core and 2 GB of memory. The pg.n2.medium.2c instance type provides 2 CPU cores and 4 GB of memory.
        # 
        # >  For more information about the instance types of ApsaraDB RDS for PostgreSQL instances, see [Instance types for primary ApsaraDB RDS for PostgreSQL instances](https://help.aliyun.com/document_detail/276990.html).
        self.dbinstance_class = dbinstance_class
        # The ID of the original instance.
        self.dbinstance_id = dbinstance_id
        # The new storage capacity of the instance. Unit: GB If you set the **UpgradeMode** parameter to **inPlaceUpgrade**, you **do not need to configure** this parameter.
        # 
        # Valid values:
        # 
        # *   **PL1 ESSD**: 20 GB to 32,000 GB
        # *   **PL2 ESSD**: 500 GB to 3,200 GB
        # *   **PL3 ESSD**: 1,500 GB to 3,200 GB
        # *   **General ESSD**: 40 GB to 2,000 GB
        # 
        # >  If the original instance uses local disks, you can reduce the storage capacity of the instance when you upgrade the major engine version of the instance. For more information about the minimum storage capacity, see [Upgrade the major engine version](https://help.aliyun.com/document_detail/203309.html).
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance that runs the required major engine version.
        # 
        # Valid values:
        # 
        # *   **cloud_ssd**: standard SSD
        # *   **cloud_essd**: performance level 1 (PL1) Enterprise SSD (ESSD)
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        # *   **general_essd**: general ESSD
        # 
        # The major engine version upgrade feature is developed based on snapshots for cloud disks. You can select a storage type after the upgrade based on the following items:
        # 
        # *   If the original instance uses standard SSDs, set this parameter to cloud_ssd.
        # *   If the original instance uses ESSDs, set this parameter to cloud_essd, cloud_essd2, cloud_essd3, or general_essd.
        # *   If the original instance uses local SSDs, set this parameter to cloud_essd, cloud_essd2, cloud_essd3, or general_essd.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The network type of the new instance. Set the value to VPC. The major engine version upgrade feature is supported only for instances that reside in VPCs.
        # 
        # If the original instance resides in the classic network, you must migrate the instance to a VPC before you call this operation. For more information about how to view or change the network type of an instance, see [Change the network type of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/96761.html).
        self.instance_network_type = instance_network_type
        # The billing method. Set the value to Postpaid.
        # 
        # >  For more information about how to change the billing method of an instance after the upgrade, see [Change the billing method of an instance from pay-as-you-go to subscription](https://help.aliyun.com/document_detail/96743.html).
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # A reserved parameter. You do not need to specify this parameter.
        self.period = period
        # The internal IP address of the new instance. You do not need to specify this parameter. The system automatically assigns an internal IP address based on the values of the VPCId and vSwitchId parameters.
        self.private_ip_address = private_ip_address
        self.resource_owner_id = resource_owner_id
        # Specifies whether to switch your workloads over to the instance that runs the required major engine version based on your business requirements.
        # 
        # Valid values:
        # 
        # *   **true**: The system automatically switches workloads over to the instance. This configuration method is used to perform an upgrade after you verify that the new major engine version is compatible with your workloads.
        # *   **false**: The system does not automatically switch your workloads over to the instance. In most cases, this configuration method is used to test whether the new major engine version is compatible with your workloads before you perform the upgrade.
        # 
        # > 
        # 
        # *   If you set this parameter to true, you must take note of the following items:
        # 
        #     *   After the switchover is complete, you cannot roll your workloads back to the original instance. Proceed with caution.
        #     *   During the switchover, the original instance processes only read requests. We recommend that you perform the switchover during off-peak hours.
        #     *   If read-only instances are attached to the original instance, you can set this parameter only to false. In this case, the read-only instances that are attached to the original instance cannot be cloned. After the upgrade is complete, you must create read-only instances for the instance.
        # 
        # *   If you set this parameter to false, you must take note of the following items:
        # 
        #     *   The data migration does not interrupt your workloads on the original instance.
        #     *   After data is migrated to the instance that runs the required major engine version, you must update the endpoint configuration in your application. This update requires you to replace the endpoint of the original instance with the endpoint of the instance that runs the required major engine version. For more information about how to view the endpoint of an instance, see [Viewing and change of the internal and public endpoints and port numbers](https://help.aliyun.com/document_detail/96788.html).
        self.switch_over = switch_over
        # A reserved parameter. You do not need to specify this parameter.
        self.switch_time = switch_time
        # The point in time at which the workloads are switched over. This parameter is used together with the SwitchOver parameter. This parameter is available only when you set the **SwitchOver** parameter to **true**.
        # 
        # Valid values:
        # 
        # *   **Immediate**: The workloads are immediately switched over.
        # *   **MaintainTime**: The workloads are switched over within the maintenance window that you specify. You can call the ModifyDBInstanceMaintainTime operation to change the maintenance window of an instance.
        self.switch_time_mode = switch_time_mode
        # The major engine version of the new instance. The value of this parameter must be the major engine version on which an upgrade check is performed.
        # 
        # >  You can call the UpgradeDBInstanceMajorVersionPrecheck operation to perform an upgrade check.
        self.target_major_version = target_major_version
        # The upgrade mode. This parameter is required when you set the **SwitchOver** parameter to **true**. Valid values:
        # 
        # *   **inPlaceUpgrade**: local upgrade. The major engine version upgrade is performed on the original instance, and no new instance is created. After the upgrade, the original instance runs the required major engine version and inherits the original orders, name, tags, alert rules in CloudMonitor, and backup settings.
        # *   **blueGreenDeployment**: blue-green deployment. After the major engine version of the instance is upgraded, the original instance is retained and a new instance is created. Fees are generated for the new instance based on the billing method that you specified. However, no fees are generated for the creation of the new instance. After the upgrade is complete, fees are generated for both the original and new instances and the new instance cannot enjoy the discounts provided for the original instance.
        self.upgrade_mode = upgrade_mode
        # A reserved parameter. You do not need to specify this parameter.
        self.used_time = used_time
        # The virtual private cloud (VPC) ID of the instance. If you set the **UpgradeMode** parameter to **inPlaceUpgrade**, you **do not need to configure** this parameter.
        # 
        # You can call the DescribeDBInstanceAttribute operation to query the VPC ID of the original instance.
        self.vpcid = vpcid
        # The vSwitch ID of the instance that runs the required major engine version. If you set the **UpgradeMode** parameter to **inPlaceUpgrade**, you **do not need to configure** this parameter.
        # 
        # *   If the original instance runs RDS Basic Edition, configure the vSwitch ID for the instance that runs the required major engine version.
        # *   If the original instance runs RDS High-availability Edition, configure the vSwitch IDs for the instance that runs the required major engine version and its secondary instance. Separate the vSwitch IDs with commas (,).
        # 
        # >  The vSwitches that you specify must reside in the same zone as the original instance. You can call the DescribeVSwitches operation to query the vSwitch IDs.
        self.v_switch_id = v_switch_id
        # The ID of the zone to which the primary instance that runs the required major engine version belongs. If you set the **UpgradeMode** parameter to **inPlaceUpgrade**, you **do not need to configure** this parameter.
        # 
        # You can call the DescribeRegions operation to query zone IDs.
        # 
        # You can select a zone that belongs to the region in which the original instance resides.
        self.zone_id = zone_id
        # The ID of the zone to which the secondary instance runs the required major engine version belongs. This parameter is available only when the original instance runs RDS High-availability Edition. If you set the **UpgradeMode** parameter to **inPlaceUpgrade**, you **do not need to configure** this parameter.
        # 
        # You can select a zone that belongs to the region in which the original instance resides.
        # 
        # You can call the DescribeRegions operation to query zone IDs.
        self.zone_id_slave_1 = zone_id_slave_1
        # A reserved parameter. You do not need to specify this parameter.
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

