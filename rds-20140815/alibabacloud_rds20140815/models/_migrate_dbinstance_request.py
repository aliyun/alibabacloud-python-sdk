# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dedicated_host_group_id: str = None,
        effective_time: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        specified_time: str = None,
        target_dedicated_host_id_for_master: str = None,
        target_dedicated_host_id_for_slave: str = None,
        zone_id_for_follower: str = None,
        zone_id_for_log: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The dedicated cluster ID. You can call the DescribeDedicatedHostGroups operation to query the dedicated cluster ID.
        # 
        # This parameter is required.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The time when you want the system to start the migration. Valid values:
        # 
        # *   **Immediately**: The system immediately starts the migration. This is the default value.
        # *   **MaintainTime**: The system starts the migration during the specified maintenance window.
        # *   **Specified**: The system starts the migration at the specified point in time.
        self.effective_time = effective_time
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time when you want the system to start the migration. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > This parameter must be specified when you set **EffectiveTime** to **Specified**.
        self.specified_time = specified_time
        # The ID of the host to which you want to migrate the primary instance. You can call the DescribeDedicatedHosts operation to query the host ID.
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master
        # The ID of the host to which you want to migrate the secondary instance. You can call the DescribeDedicatedHosts operation to query the host ID.
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave
        # The zone ID of the secondary node.
        self.zone_id_for_follower = zone_id_for_follower
        # The zone ID of the logger instance.
        self.zone_id_for_log = zone_id_for_log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

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

        if self.target_dedicated_host_id_for_master is not None:
            result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master

        if self.target_dedicated_host_id_for_slave is not None:
            result['TargetDedicatedHostIdForSlave'] = self.target_dedicated_host_id_for_slave

        if self.zone_id_for_follower is not None:
            result['ZoneIdForFollower'] = self.zone_id_for_follower

        if self.zone_id_for_log is not None:
            result['ZoneIdForLog'] = self.zone_id_for_log

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

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

        if m.get('TargetDedicatedHostIdForMaster') is not None:
            self.target_dedicated_host_id_for_master = m.get('TargetDedicatedHostIdForMaster')

        if m.get('TargetDedicatedHostIdForSlave') is not None:
            self.target_dedicated_host_id_for_slave = m.get('TargetDedicatedHostIdForSlave')

        if m.get('ZoneIdForFollower') is not None:
            self.zone_id_for_follower = m.get('ZoneIdForFollower')

        if m.get('ZoneIdForLog') is not None:
            self.zone_id_for_log = m.get('ZoneIdForLog')

        return self

