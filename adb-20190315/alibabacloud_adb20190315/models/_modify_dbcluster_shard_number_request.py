# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterShardNumberRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dry_run: bool = None,
        is_rollback: bool = None,
        new_shard_number: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        switch_time_mode: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL Data Warehouse Edition clusters within a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # *   true: sends a request to check whether the cluster meets the prerequisites for changing the number of shards and whether the desired number of shards is valid, but **does not** perform the change operation.
        # *   false (default): sends a request to perform a check and trigger the change operation.
        self.dry_run = dry_run
        self.is_rollback = is_rollback
        # The desired number of shards.
        self.new_shard_number = new_shard_number
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time when you want the system to perform the change operation. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.switch_time = switch_time
        # The mode in which you want the change operation to be performed. Valid values:
        # 
        # *   **Immediate** (default): immediately performs the change operation.
        # *   **MaintainTime**: performs the change operation within the maintenance window of the cluster. You can call the ModifyDBInstanceMaintainTime operation to change the maintenance window.
        # *   **ScheduleTime**: performs the change operation at the point in time that you specify. If you specify this value, you must also specify **SwitchTime**.
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.is_rollback is not None:
            result['IsRollback'] = self.is_rollback

        if self.new_shard_number is not None:
            result['NewShardNumber'] = self.new_shard_number

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IsRollback') is not None:
            self.is_rollback = m.get('IsRollback')

        if m.get('NewShardNumber') is not None:
            self.new_shard_number = m.get('NewShardNumber')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        return self

