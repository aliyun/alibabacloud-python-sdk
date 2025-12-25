# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartDBInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbinstance_trans_type: int = None,
        dedicated_host_group_id: str = None,
        effective_time: str = None,
        engine_version: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        specified_time: str = None,
        storage: int = None,
        target_dbinstance_class: str = None,
        target_dedicated_host_id_for_log: str = None,
        target_dedicated_host_id_for_master: str = None,
        target_dedicated_host_id_for_slave: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The data migration method of the instance. This parameter is available only for instances that are created in dedicated clusters. Valid values:
        # 
        # *   **0** (default): The system preferentially upgrades or downgrades the instance without a migration. If the resources on the host on which the instance resides are insufficient, the system migrates the instance to another suitable host.
        # *   **1**: The system upgrades or downgrades the instance without a migration. If the upgrade or downgrade is not supported, the system reports an error.
        # *   **2**: The system migrates the data of the instance from the host on which the instance resides to another host. You must also specify **DedicatedHostGroupId**, **TargetDedicatedHostIdForMaster**, and **TargetDedicatedHostIdForSlave**. If you set DBInstanceTransType to 2, you cannot migrate the data of the instance to the host on which the instance resides. If you migrate the data of the instance to the host on which the instance resides, the migration fails.
        self.dbinstance_trans_type = dbinstance_trans_type
        # The dedicated cluster ID. This parameter is supported if you call this operation to suspend an RDS instance in the dedicated cluster. You can call the DescribeDedicatedHostGroups operation to query the dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The effective time. This parameter is available only for instances that are created in dedicated clusters.
        # 
        # *   **Immediate**
        # *   **MaintainTime**: The change takes effect during the planned maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # *   **SpecificTime**: The change takes effect at a specified point in time.
        # 
        # Default value: MaintainTime.
        self.effective_time = effective_time
        # The database engine version of the instance. This parameter is available only for instances that are created in dedicated clusters.
        self.engine_version = engine_version
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The switching time. This parameter is available only for instances that are created in dedicated clusters. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > This parameter must be specified when **EffectiveTime** is set to **Specified**.
        self.specified_time = specified_time
        # The storage capacity of the instance. This parameter is available only for instances that are created in dedicated clusters. Valid values: **5 to 2000**. Unit: GB. If you do not specify this parameter, the storage capacity of the instance remains unchanged.
        self.storage = storage
        # The instance type of the required instance. This parameter is available only for instances that are created in dedicated clusters.
        self.target_dbinstance_class = target_dbinstance_class
        # A deprecated parameter. You do not need to specify this parameter.
        self.target_dedicated_host_id_for_log = target_dedicated_host_id_for_log
        # The ID of the host on which the primary instance is created. This parameter is available only for instances that are created in dedicated clusters.
        # 
        # > This parameter must be specified when **DBInstanceTransType** is set to **2**.
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master
        # The ID of the host on which the secondary instance is created. This parameter is available only for instances that are created in dedicated clusters.
        # 
        # > This parameter must be specified when **DBInstanceTransType** is set to **2**.
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave
        # The vSwitch ID. This parameter is available only for instances that are created in dedicated clusters.
        self.v_switch_id = v_switch_id
        # The zone ID. This parameter is available only for instances that are created in dedicated clusters.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_trans_type is not None:
            result['DBInstanceTransType'] = self.dbinstance_trans_type

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.specified_time is not None:
            result['SpecifiedTime'] = self.specified_time

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.target_dbinstance_class is not None:
            result['TargetDBInstanceClass'] = self.target_dbinstance_class

        if self.target_dedicated_host_id_for_log is not None:
            result['TargetDedicatedHostIdForLog'] = self.target_dedicated_host_id_for_log

        if self.target_dedicated_host_id_for_master is not None:
            result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master

        if self.target_dedicated_host_id_for_slave is not None:
            result['TargetDedicatedHostIdForSlave'] = self.target_dedicated_host_id_for_slave

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceTransType') is not None:
            self.dbinstance_trans_type = m.get('DBInstanceTransType')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SpecifiedTime') is not None:
            self.specified_time = m.get('SpecifiedTime')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('TargetDBInstanceClass') is not None:
            self.target_dbinstance_class = m.get('TargetDBInstanceClass')

        if m.get('TargetDedicatedHostIdForLog') is not None:
            self.target_dedicated_host_id_for_log = m.get('TargetDedicatedHostIdForLog')

        if m.get('TargetDedicatedHostIdForMaster') is not None:
            self.target_dedicated_host_id_for_master = m.get('TargetDedicatedHostIdForMaster')

        if m.get('TargetDedicatedHostIdForSlave') is not None:
            self.target_dedicated_host_id_for_slave = m.get('TargetDedicatedHostIdForSlave')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

