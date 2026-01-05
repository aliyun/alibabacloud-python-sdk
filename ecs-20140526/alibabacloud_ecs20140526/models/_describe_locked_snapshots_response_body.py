# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeLockedSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        locked_snapshots_info: List[main_models.DescribeLockedSnapshotsResponseBodyLockedSnapshotsInfo] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Details of the locked snapshots.
        self.locked_snapshots_info = locked_snapshots_info
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.locked_snapshots_info:
            for v1 in self.locked_snapshots_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LockedSnapshotsInfo'] = []
        if self.locked_snapshots_info is not None:
            for k1 in self.locked_snapshots_info:
                result['LockedSnapshotsInfo'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.locked_snapshots_info = []
        if m.get('LockedSnapshotsInfo') is not None:
            for k1 in m.get('LockedSnapshotsInfo'):
                temp_model = main_models.DescribeLockedSnapshotsResponseBodyLockedSnapshotsInfo()
                self.locked_snapshots_info.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLockedSnapshotsResponseBodyLockedSnapshotsInfo(DaraModel):
    def __init__(
        self,
        cool_off_period: int = None,
        cool_off_period_expired_time: str = None,
        lock_creation_time: str = None,
        lock_duration: int = None,
        lock_duration_start_time: str = None,
        lock_expired_time: str = None,
        lock_status: str = None,
        snapshot_id: str = None,
    ):
        # The cooling-off period of the compliance mode. Unit: hours.
        self.cool_off_period = cool_off_period
        # The end time of the cooling-off period in compliance mode. The time follows the [ISO 8601](https://help.aliyun.com/zh/ecs/developer-reference/iso-8601-time-format?spm=a2c4g.11186623.0.0.277c6c92kl7kXM) standard in the yyyy-MM-ddTHH:mm:ssZ format (in UTC).
        self.cool_off_period_expired_time = cool_off_period_expired_time
        # The date and time at which the snapshot is locked. The time follows the [ISO 8601](https://help.aliyun.com/zh/ecs/developer-reference/iso-8601-time-format?spm=a2c4g.11186623.0.0.277c6c92kl7kXM) standard in the yyyy-MM-ddTHH:mm:ssZ format (in UTC).
        self.lock_creation_time = lock_creation_time
        # The lock duration. The snapshot lock automatically expires after the lock duration ends. Unit: days.
        self.lock_duration = lock_duration
        # The start time of the lock duration. The time follows the [ISO 8601](https://help.aliyun.com/zh/ecs/developer-reference/iso-8601-time-format?spm=a2c4g.11186623.0.0.277c6c92kl7kXM) standard in the yyyy-MM-ddTHH:mm:ssZ format (in UTC). If you lock a snapshot that is in the Progressing state, the lock time is not calculated until the snapshot enters the Accomplished state.
        self.lock_duration_start_time = lock_duration_start_time
        # The time when the lock expires. The time follows the [ISO 8601](https://help.aliyun.com/zh/ecs/developer-reference/iso-8601-time-format?spm=a2c4g.11186623.0.0.277c6c92kl7kXM) standard in the yyyy-MM-ddTHH:mm:ssZ format (in UTC).
        self.lock_expired_time = lock_expired_time
        # The lock status. Valid values:
        # 
        # *   compliance-cooloff: The snapshot is locked in compliance mode but is still in a cooling-off period. Snapshots cannot be deleted. However, users with the corresponding RAM permissions can unlock snapshots, extend or shorten the cooling-off period, and extend or shorten the lock duration.
        # *   compliance: The snapshot is locked in compliance mode and the cooling-off period has ended. Snapshots cannot be unlocked or deleted. However, users with the corresponding RAM permissions can extend the lock duration.
        # *   expired: The snapshot was once locked, but the lock duration has ended and the lock has expired. The snapshot is not locked and can be deleted.
        self.lock_status = lock_status
        # The snapshot ID.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cool_off_period is not None:
            result['CoolOffPeriod'] = self.cool_off_period

        if self.cool_off_period_expired_time is not None:
            result['CoolOffPeriodExpiredTime'] = self.cool_off_period_expired_time

        if self.lock_creation_time is not None:
            result['LockCreationTime'] = self.lock_creation_time

        if self.lock_duration is not None:
            result['LockDuration'] = self.lock_duration

        if self.lock_duration_start_time is not None:
            result['LockDurationStartTime'] = self.lock_duration_start_time

        if self.lock_expired_time is not None:
            result['LockExpiredTime'] = self.lock_expired_time

        if self.lock_status is not None:
            result['LockStatus'] = self.lock_status

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoolOffPeriod') is not None:
            self.cool_off_period = m.get('CoolOffPeriod')

        if m.get('CoolOffPeriodExpiredTime') is not None:
            self.cool_off_period_expired_time = m.get('CoolOffPeriodExpiredTime')

        if m.get('LockCreationTime') is not None:
            self.lock_creation_time = m.get('LockCreationTime')

        if m.get('LockDuration') is not None:
            self.lock_duration = m.get('LockDuration')

        if m.get('LockDurationStartTime') is not None:
            self.lock_duration_start_time = m.get('LockDurationStartTime')

        if m.get('LockExpiredTime') is not None:
            self.lock_expired_time = m.get('LockExpiredTime')

        if m.get('LockStatus') is not None:
            self.lock_status = m.get('LockStatus')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

