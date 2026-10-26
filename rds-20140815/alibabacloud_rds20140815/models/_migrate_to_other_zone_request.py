# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateToOtherZoneRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        custom_extra_info: str = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        effective_time: str = None,
        io_acceleration_enabled: str = None,
        is_modify_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
        zone_id_slave_2: str = None,
    ):
        # The instance edition. Valid values:
        # 
        # * **Basic**: Basic Edition.
        # * **HighAvailability**: High-availability Edition.
        # * **AlwaysOn**: Cluster Edition for SQL Server.
        # * **cluster**: Cluster Edition for MySQL.
        # * **Finance**: RDS Enterprise Edition.
        self.category = category
        self.custom_extra_info = custom_extra_info
        # The instance type code of the destination instance. Only instance type changes are supported. Storage type changes are not supported.
        # When the **IsModifySpec** parameter settings are **true**, you must specify at least one of this parameter and **DBInstanceStorage**.
        # 
        # For more information about instance type codes, see [ApsaraDB RDS for MySQL primary instance types](https://help.aliyun.com/document_detail/276975.html).
        self.dbinstance_class = dbinstance_class
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The destination storage capacity. When the **IsModifySpec** parameter settings are **true**, you must specify at least one of this parameter and **DBInstanceClass**.
        # 
        # Unit: GB.
        # Valid values: The storage capacity that can be expanded varies by instance type. For more information, see [ApsaraDB RDS for MySQL primary instance types](https://help.aliyun.com/document_detail/276975.html).
        self.dbinstance_storage = dbinstance_storage
        # The instance storage type. Valid values:
        # - cloud_essd: PL1 ESSD.
        # - cloud_essd2: PL2 ESSD.
        # - cloud_essd3: PL3 ESSD.
        # - cloud_ssd: standard SSD. This is not recommended because standard SSDs are no longer available in some regions.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The effective period. Valid values:
        # * **Immediate**: Takes effect immediately. This is the default value.
        # * **MaintainTime**: Takes effect within the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # * **ScheduleTime**: Takes effect at a specified time.
        # 
        # > If you set this parameter to **ScheduleTime**, you must also specify the **SwitchTime** parameter.
        self.effective_time = effective_time
        # The Buffer Pool Extension (BPE) feature switch for premium cloud disks. Valid values:
        # 
        #  - **1**: Enables the feature.
        #  - **0**: Disables the feature.
        # 
        # > For more information about the BPE feature, see [Buffer Pool Extension (BPE)](https://help.aliyun.com/document_detail/2527067.html).
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to change the specifications during zone migration. Valid values:
        # 
        # - **true**: Changes the specifications. If you set this parameter to **true**, you must specify at least one of the **DBInstanceClass** or **DBInstanceStorage** parameters.
        # - **false**: Does not change the specifications. This is the default value.
        # 
        # > This parameter is only applicable to ApsaraDB RDS for MySQL instances.
        self.is_modify_spec = is_modify_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The custom effective time for switching zones. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        # >This parameter is used together with the **EffectiveTime** parameter and is required only when **EffectiveTime** is set to **ScheduleTime**.
        self.switch_time = switch_time
        # The ID of the virtual private cloud (VPC). The VPC cannot be changed during instance migration and must remain the same.
        # 
        # - This parameter is required when you migrate a VPC-connected instance across zones.
        # - If the instance runs SQL Server, the VPC can be changed during instance migration.
        self.vpcid = vpcid
        # The vSwitch ID.
        # - This parameter is required when you migrate a VPC-connected instance across zones. You can call the DescribeVSwitches operation to query the created vSwitches.
        # - When you migrate an ApsaraDB RDS for PostgreSQL or ApsaraDB RDS for SQL Server instance across zones and configure a secondary zone, you can specify multiple vSwitch IDs separated by commas (,). The vSwitch IDs must correspond to the zones.
        self.v_switch_id = v_switch_id
        # The ID of the destination zone. You can call the DescribeRegions operation to query the zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id
        # The ID of secondary zone 1.
        # >This parameter is required for instances that are not Basic Edition.
        self.zone_id_slave_1 = zone_id_slave_1
        # The ID of secondary zone 2.
        # >This parameter is only applicable to RDS Enterprise Edition instances.
        self.zone_id_slave_2 = zone_id_slave_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

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

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.is_modify_spec is not None:
            result['IsModifySpec'] = self.is_modify_spec

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

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
        if m.get('Category') is not None:
            self.category = m.get('Category')

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

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('IsModifySpec') is not None:
            self.is_modify_spec = m.get('IsModifySpec')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

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

