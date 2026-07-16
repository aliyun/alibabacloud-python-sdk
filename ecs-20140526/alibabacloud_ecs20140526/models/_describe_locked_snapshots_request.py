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
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - true: performs a dry run without performing the actual operation. The system checks for required parameters, the request format, and business constraints. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # 
        # - false (default): performs a dry run and performs the actual operation if the request passes the dry run.
        self.dry_run = dry_run
        # The lock status. Valid values:
        # 
        # - compliance-cooloff: The snapshot is locked in compliance mode and is within its cool-off period. The snapshot cannot be deleted. Users with the required RAM permissions can unlock the snapshot, extend or shorten the cool-off period, and extend or shorten the lock duration.
        # 
        # - compliance: The snapshot is locked in compliance mode and the cool-off period has ended. The snapshot cannot be unlocked or deleted. Users with the required RAM permissions can extend the lock duration.
        # 
        # - expired: The lock on the snapshot has expired. The snapshot is no longer locked and can be deleted.
        self.lock_status = lock_status
        # The number of entries per page. Maximum value: 100.
        # 
        # Default value:
        # 
        # - If you do not specify this parameter or you specify a value smaller than 10, the default value is 10.
        # 
        # - If you specify a value larger than 100, the value is capped at 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. It is the `NextToken` value from a previous response.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-describeregions?spm=a2c4g.11186623.0.i2) to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # An array of one to 100 snapshot IDs.
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

