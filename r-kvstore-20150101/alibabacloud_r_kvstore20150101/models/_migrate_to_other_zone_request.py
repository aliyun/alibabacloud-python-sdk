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
        # The ID of the Tair (Redis OSS-compatible) instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The time when the database is switched after the instance is migrated. Valid values:
        # 
        # *   **Immediately**: The database is immediately switched after the instance is migrated.
        # *   **MaintainTime**: The database is switched within the maintenance window.
        # 
        # >  Default value: Immediately.
        self.effective_time = effective_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read replicas in the primary zone.
        # 
        # > 
        # 
        # *   The **ReadOnlyCount** and **SlaveReadOnlyCount** parameters are applicable only to cloud-native instances for which read/write splitting is enabled. When you migrate an instance to multiple zones, you can use these parameters to adjust the distribution of read replicas in the primary and secondary zones of the instance. This operation does not allow you to increase or decrease the number of nodes. Therefore, the sum of the values of `ReadOnlyCount and SlaveReadOnlyCount` must be the same as that before the migration.
        # 
        # *   If you do not specify these parameters when you migrate an instance from a single zone to multiple zones, one read replica is migrated to the secondary zone, and all other read replicas remain in the primary zone.
        # 
        # *   If the instance is a cluster instance, the preceding parameters indicate the number of read replicas per shard in the primary and secondary zones of the instance.
        self.read_only_count = read_only_count
        # The number of replica nodes in the primary zone.
        # 
        # > 
        # 
        # *   The **ReplicaCount** and **SlaveReplicaCount** parameters are applicable only to cloud-native instances. When you migrate an instance to multiple zones, you can use these parameters to adjust the distribution of replica nodes in the primary and secondary zones of the instance. This operation does not allow you to increase or decrease the number of nodes. Therefore, the sum of the values of `ReplicaCount and SlaveReplicaCount` must be the same as that before the migration.
        # 
        # *   If you do not specify these parameters when you migrate an instance from a single zone to multiple zones, one replica node is migrated to the secondary zone, and all other replica nodes remain in the primary zone.
        # 
        # *   If the instance is a cluster instance, the preceding parameters indicate the number of replica nodes per shard in the primary and secondary zones of the instance.
        self.replica_count = replica_count
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the secondary zone to which you want to migrate the instance. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query zone IDs.
        # 
        # >  If you specify this parameter, the master node and replica node of the instance can be deployed in different zones and disaster recovery is implemented across zones. The instance can withstand failures in data centers.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of read replicas in the secondary zone.
        self.slave_read_only_count = slave_read_only_count
        # The number of replica nodes in the secondary zone.
        self.slave_replica_count = slave_replica_count
        # The ID of the vSwitch.
        # 
        # > 
        # 
        # *   The zone where the vSwitch resides must be the same as the ID of the destination zone.
        # 
        # *   If the network type of the instance is VPC, this parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the destination primary zone. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query zone IDs.
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

