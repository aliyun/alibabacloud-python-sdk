# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateToOtherZoneRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        effective_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        read_only_count: int = None,
        replica_count: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_zone_id: str = None,
        security_token: str = None,
        slave_read_only_count: int = None,
        slave_replica_count: int = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The time when the database switchover is performed after data migration. Valid values: 
        # * **Immediately**: The switchover is performed immediately after the migration.
        # * **MaintainTime**: The switchover is performed within the maintenance window.
        # 
        # > Default value: **Immediately**.
        self.effective_time = effective_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes in the primary zone.
        # > * The ReadOnlyCount and SlaveReadOnlyCount parameters apply only to cloud-native instances with read/write splitting enabled. When you migrate an instance to multiple zones, you can use these parameters to adjust the distribution of read-only nodes across the primary and secondary zones. This operation does not support adding or removing nodes. Therefore, the total number of read-only nodes calculated by ReadOnlyCount + SlaveReadOnlyCount must remain the same as that before the migration.
        # > * When you migrate an instance from a single zone to multiple zones and do not specify these parameters, one read-only node is migrated to the secondary zone by default, and the remaining read-only nodes stay in the primary zone.
        # > * If the instance uses the cluster architecture, these parameters specify the number of read-only nodes per shard in the primary and secondary zones.
        self.read_only_count = read_only_count
        # The number of secondary nodes in the primary zone.
        # > * The ReplicaCount and SlaveReplicaCount parameters apply only to cloud-native instances. When you migrate an instance to multiple zones, you can use these parameters to adjust the distribution of secondary nodes across the primary and secondary zones. This operation does not support adding or removing nodes. Therefore, the total number of secondary nodes calculated by ReplicaCount + SlaveReplicaCount must remain the same as that before the migration.
        # > * When you migrate an instance from a single zone to multiple zones and do not specify these parameters, one secondary node is migrated to the secondary zone by default, and the remaining secondary nodes stay in the primary zone.
        # > * If the instance uses the cluster architecture, these parameters specify the number of secondary nodes per shard in the primary and secondary zones.
        self.replica_count = replica_count
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the destination secondary zone. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query the zone ID.
        # > If you specify this parameter, the primary and secondary data nodes are distributed across different zones. This implements cross-zone disaster recovery and tolerates data center-level failures.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of read-only nodes in the secondary zone.
        self.slave_read_only_count = slave_read_only_count
        # The number of secondary nodes in the secondary zone.
        self.slave_replica_count = slave_replica_count
        # The vSwitch ID.
        # 
        # > * The zone where the vSwitch resides must be the same as the destination zone specified by ZoneId. 
        # > * This parameter is required if the network type of the instance is VPC.
        self.v_switch_id = v_switch_id
        # The ID of the destination primary zone. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query the zone ID.
        # 
        # This parameter is required.
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

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count

        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.slave_read_only_count is not None:
            result['SlaveReadOnlyCount'] = self.slave_read_only_count

        if self.slave_replica_count is not None:
            result['SlaveReplicaCount'] = self.slave_replica_count

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')

        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SlaveReadOnlyCount') is not None:
            self.slave_read_only_count = m.get('SlaveReadOnlyCount')

        if m.get('SlaveReplicaCount') is not None:
            self.slave_replica_count = m.get('SlaveReplicaCount')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

