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
        # A client token that is used to ensure the idempotence of the request. You can use the client to generate a client token. Make sure that a unique client token is used for each request. ClientToken only supports ASCII characters and cannot exceed 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/zh/ecs/developer-reference/how-to-ensure-idempotence?spm=a2c4g.11186623.0.0.2a29d467Bh2sO5).
        self.client_token = client_token
        # Cooling-off period. In compliance mode, you can set a cooling-off period or skip the cooling-off period to directly lock the snapshot.
        # 
        # During the cooling-off period, users with corresponding RAM permissions can unlock snapshots, extend or shorten the cooling-off period, and extend or shorten the lock duration. Snapshots cannot be deleted during the cooling-off period.
        # 
        # After the cooling-off period ends, only extending the lock duration is supported.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 72. A value of 0 indicates skipping the cooling-off period and directly locking the snapshot.
        # 
        # If the snapshot has entered the compliance mode lock period, set this parameter to 0 when extending the lock duration.
        # 
        # This parameter is required.
        self.cool_off_period = cool_off_period
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # *   true: The request is checked and is not executed. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the check fails, the corresponding error is returned. If the check passes, the error code DryRunOperation is returned.
        # *   false (default): Sends a normal request, checks it, and executes the request directly if it passes the check.
        self.dry_run = dry_run
        # Lock duration. After the lock duration ends, the snapshot lock will automatically expire.
        # 
        # Unit: days.
        # 
        # Valid values: 1 to 36500.
        # 
        # This parameter is required.
        self.lock_duration = lock_duration
        # The lock mode. Valid values:
        # 
        # *   compliance: The snapshot is locked in compliance mode. A snapshot that is locked in compliance mode cannot be unlocked by any user. It can be deleted only after the lock duration expires. Users cannot shorten the lock duration, but users with the corresponding RAM permissions can extend the lock duration at any time. When locking a snapshot in compliance mode, you can optionally specify a cooling-off period.
        # 
        # This parameter is required.
        self.lock_mode = lock_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID You can call the [DescribeRegions](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-describeregions?spm=a2c4g.11186623.0.i2) operation to query the most recent region list.
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

