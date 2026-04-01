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
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition
        # *   **HighAvailability**: RDS High-availability Edition
        # *   **AlwaysOn**: SQL Server on RDS Cluster Edition
        # *   **cluster**: MySQL on RDS Cluster Edition
        # *   **Finance**: RDS Enterprise Edition
        self.category = category
        self.custom_extra_info = custom_extra_info
        # The new instance type of the instance. You can change the instance type of the instance. You cannot change the storage type of the instance. If you set **IsModifySpec** to **true**, you must specify at least one of DBInstanceClass and **DBInstanceStorage**.
        # 
        # For more information about instance types, see [Primary ApsaraDB RDS for MySQL instance types](https://help.aliyun.com/document_detail/276975.html).
        self.dbinstance_class = dbinstance_class
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The new storage capacity of the instance. If you set **IsModifySpec** to **true**, you must specify at least one of DBInstanceStorage and **DBInstanceClass**.
        # 
        # Unit: GB. The available storage capacity range varies based on the instance type of the instance. For more information, see [Primary ApsaraDB RDS for MySQL instance types](https://help.aliyun.com/document_detail/276975.html).
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance. Valid values:
        # 
        # *   **local_ssd**: local SSD. This is the recommended storage type.
        # *   **general_essd**: general Enterprise SSD (ESSD). This is the recommended storage type.
        # *   **cloud_essd**: PL1 ESSD
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        # *   **cloud_ssd**: standard SSD. This storage type is not recommended. Standard SSDs are no longer available for purchase in some Alibaba Cloud regions.
        # 
        # The default value of this parameter is determined by the instance type specified by the **DBInstanceClass** parameter.
        # 
        # *   If the instance type specifies the local SSD storage type, the default value of this parameter is **local_ssd**.
        # *   If the instance type specifies the standard SSD or ESSD storage type, the default value of this parameter is **cloud_essd**.
        # 
        # >  Serverless instances support only PL1 ESSDs and general ESSDs.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The time when you want the change to take effect. Valid values:
        # 
        # *   **Immediately** (default): The change immediately takes effect.
        # *   **MaintainTime**: The change takes effect during the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # *   **ScheduleTime**: The change takes effect at the point in time that you specify.
        # 
        # >  If you set this parameter to **ScheduleTime**, you must specify the **SwitchTime** parameter.
        self.effective_time = effective_time
        # A reserved parameter.
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to change the specifications of the instance during the cross-zone migration. Valid values:
        # 
        # *   **true**: You want to change the specifications of the instance during the cross-zone migration. If you set this parameter to **true**, you must specify at least one of **DBInstanceClass** and **DBInstanceStorage**.
        # *   **false** (default): You do not want to change the specifications of the instance during the cross-zone migration.
        # 
        # > This parameter applies only to instances that run MySQL.
        self.is_modify_spec = is_modify_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The migration time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > This parameter is used with **EffectiveTime**. You must specify this parameter only when **EffectiveTime** is set to **ScheduleTime**.
        self.switch_time = switch_time
        # The ID of the virtual private cloud (VPC). Do not change the VPC of the instance when you migrate the instance across zones.
        # 
        # *   This parameter must be specified when the instance resides in a VPC.
        # *   If the instance runs SQL Server, you can change the VPC of the instance.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # *   This parameter must be specified when the instance resides in a VPC. You can call the DescribeVSwitches operation to query existing vSwitches.
        # *   If the instance runs PostgreSQL or SQL Server and a secondary zone is specified for the instance, you can specify multiple vSwitch IDs, each of which corresponds to a zone. Separate the vSwitch IDs with commas (,).
        self.v_switch_id = v_switch_id
        # The ID of the destination zone. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.zone_id = zone_id
        # The secondary zone 1 of the instance.
        # 
        # >  This parameter must be configured if the instance runs RDS editions other than RDS Basic Edition.
        self.zone_id_slave_1 = zone_id_slave_1
        # The secondary zone 2 of the instance.
        # 
        # >  You can specify this parameter only for instances that run RDS Enterprise Edition.
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

