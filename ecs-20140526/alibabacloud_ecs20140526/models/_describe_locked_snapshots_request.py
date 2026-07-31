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
        # - true: performs only a dry run. The system checks the request for potential issues, including required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned. 
        # - false (default): performs a dry run and sends the request. If the request passes the dry run, the operation is performed.
        self.dry_run = dry_run
        # The lock status. Valid values: 
        # - compliance-cooloff: The snapshot is locked in compliance mode but is still within the cooling-off period. The snapshot cannot be deleted, but users with the required RAM permissions can unlock the snapshot, extend or shorten the cooling-off period, or extend or shorten the lock duration. 
        # - compliance: The snapshot is locked in compliance mode and the cooling-off period has ended. The snapshot cannot be unlocked or deleted, but users with the required RAM permissions can extend the lock duration. 
        # - expired: The snapshot was previously locked, but the lock duration has ended and the lock has expired. The snapshot is currently unlocked and can be deleted.
        self.lock_status = lock_status
        # The maximum number of entries per page for a paging query. Maximum value: 100. 
        # 
        # Default value: 
        # - If this parameter is not specified or is set to a value less than 10, the default value is 10. 
        # - If this parameter is set to a value greater than 100, the default value is 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the `NextToken` value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call [DescribeRegions](https://www.alibabacloud.com/help/en/ecs/developer-reference/api-ecs-2014-05-26-describeregions) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of snapshot IDs. Valid values of array length: 1 to 100.
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

