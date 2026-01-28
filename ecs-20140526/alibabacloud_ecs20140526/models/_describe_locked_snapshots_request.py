# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLockedSnapshotsRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        lock_status: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_ids: List[str] = None,
    ):
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # *   true: The request is checked and is not executed. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the check fails, the corresponding error is returned. If the check passes, the error code DryRunOperation is returned.
        # *   false (default): Sends a normal request, checks it, and executes the request directly if it passes the check.
        self.dry_run = dry_run
        # The lock status. Valid values:
        # 
        # *   compliance-cooloff: The snapshot is locked in compliance mode but is still in a cooling-off period. Snapshots cannot be deleted. However, users with the corresponding RAM permissions can unlock snapshots, extend or shorten the cooling-off period, and extend or shorten the lock duration.
        # *   compliance: The snapshot is locked in compliance mode and the cooling-off period has ended. Snapshots cannot be unlocked or deleted. However, users with the corresponding RAM permissions can extend the locked duration.
        # *   expired: The snapshot was once locked, but the lock duration has ended and the lock has expired. The snapshot is not locked and can be deleted.
        self.lock_status = lock_status
        # The maximum number of entries to return on each page. Maximum value: 100.
        # 
        # Default value:
        # 
        # *   If no value is set or the set value is less than 10, the default value is 10.
        # *   If you set a value greater than 100, the default value is 100.
        self.max_results = max_results
        # The query token. Set the value to the `NextToken` parameter value returned in the last API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-describeregions?spm=a2c4g.11186623.0.i2) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The snapshot IDs. You can specify 1 to 100 IDs.
        self.snapshot_ids = snapshot_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.lock_status is not None:
            result['LockStatus'] = self.lock_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LockStatus') is not None:
            self.lock_status = m.get('LockStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')

        return self

