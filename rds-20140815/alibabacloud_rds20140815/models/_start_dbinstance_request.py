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
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is supported only for dedicated cluster instances. The migration method of the instance. Valid values:
        # * **0**: Default value. The system preferentially performs a local specification change. If local resources are insufficient, a cross-instance migration is performed.
        # * **1**: Local specification change. If the system determines that the instance does not support a local specification change, an error is returned.
        # * **2**: Cross-instance migration. The instance is migrated to a specified host. You must specify **DedicatedHostGroupId**, **TargetDedicatedHostIdForMaster**, and **TargetDedicatedHostIdForSlave**. The instance cannot be migrated to the host on which it currently resides. Otherwise, the migration fails.
        self.dbinstance_trans_type = dbinstance_trans_type
        # This operation also supports starting an ApsaraDB RDS instance in a dedicated cluster. In this case, specify the dedicated cluster ID. You can call DescribeDedicatedHostGroups to query the dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # This parameter is supported only for dedicated cluster instances. The effective period. Valid values:
        # 
        # * **Immediate**: The operation takes effect immediately.
        # * **MaintainTime**: The operation takes effect during the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # * **SpecificTime**: The operation takes effect at a specified time.
        # 
        # Default value: MaintainTime.
        self.effective_time = effective_time
        # This parameter is supported only for dedicated cluster instances. The database engine version.
        self.engine_version = engine_version
        self.owner_id = owner_id
        # The region ID. You can call DescribeRegions to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is supported only for dedicated cluster instances. The specified switchover time. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        # 
        # > This parameter is required when **EffectiveTime** is set to **Specified**.
        self.specified_time = specified_time
        # This parameter is supported only for dedicated cluster instances. The custom storage capacity. Valid values: **5 to 2000**. Unit: GB. If you do not specify this parameter, the storage capacity remains unchanged.
        self.storage = storage
        # This parameter is supported only for dedicated cluster instances. The instance type of the target instance.
        self.target_dbinstance_class = target_dbinstance_class
        # **[Deprecated]** This parameter is deprecated and does not need to be configured.
        self.target_dedicated_host_id_for_log = target_dedicated_host_id_for_log
        # This parameter is supported only for dedicated cluster instances. Specifies the ID of the destination host for the primary node.
        # 
        # > This parameter is required when **DBInstanceTransType** is set to **2**.
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master
        # This parameter is supported only for dedicated cluster instances. Specifies the ID of the destination host for the secondary node.
        # 
        # > This parameter is required when **DBInstanceTransType** is set to **2**.
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave
        # This parameter is supported only for dedicated cluster instances. The vSwitch ID.
        self.v_switch_id = v_switch_id
        # This parameter is supported only for dedicated cluster instances. The zone ID.
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

