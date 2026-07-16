# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LockSnapshotRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cool_off_period: int = None,
        dry_run: bool = None,
        lock_duration: int = None,
        lock_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_id: str = None,
    ):
        # A unique, case-sensitive token that you provide to ensure the idempotence of the request. The token can contain only ASCII characters and must not exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/zh/ecs/developer-reference/how-to-ensure-idempotence?spm=a2c4g.11186623.0.0.2a29d467Bh2sO5).
        self.client_token = client_token
        # The cool-off period. In compliance mode, you can specify a cool-off period or set this parameter to 0 to lock the snapshot immediately.
        # 
        # During the cool-off period, users with the required RAM permissions can unlock the snapshot, extend or shorten the cool-off period, and extend or shorten the lock duration. The snapshot cannot be deleted during the cool-off period.
        # 
        # After the cool-off period ends, you can only extend the lock duration.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 72. A value of 0 indicates that the cool-off period is skipped and the snapshot is locked immediately.
        # 
        # If a snapshot is already locked in compliance mode, you must set this parameter to 0 to extend its lock duration.
        # 
        # This parameter is required.
        self.cool_off_period = cool_off_period
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - `true`: Performs a dry run to check the request without executing it. The system checks for required parameters, request format, business constraints, and permissions. If the check passes, the `DryRunOperation` error code is returned. If the check fails, a corresponding error is returned.
        # 
        # - `false` (default): Checks the request and, if the checks pass, executes the operation.
        self.dry_run = dry_run
        # The number of days to lock the snapshot. The lock automatically expires at the end of this period.
        # 
        # Unit: days.
        # 
        # Valid values: 1 to 36500.
        # 
        # This parameter is required.
        self.lock_duration = lock_duration
        # The lock mode. Valid value:
        # 
        # - `compliance`: Locks the snapshot in compliance mode. A snapshot locked in compliance mode cannot be unlocked by any user and can be deleted only after its lock duration expires. You cannot shorten the lock duration. However, users with the required RAM permissions can extend the lock duration at any time. When you lock a snapshot in compliance mode, you can optionally specify a cool-off period.
        # 
        # This parameter is required.
        self.lock_mode = lock_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-describeregions?spm=a2c4g.11186623.0.i2) to get the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cool_off_period is not None:
            result['CoolOffPeriod'] = self.cool_off_period

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.lock_duration is not None:
            result['LockDuration'] = self.lock_duration

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

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

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CoolOffPeriod') is not None:
            self.cool_off_period = m.get('CoolOffPeriod')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LockDuration') is not None:
            self.lock_duration = m.get('LockDuration')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

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

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

