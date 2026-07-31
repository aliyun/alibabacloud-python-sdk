# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class LockSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        locked_snapshot_info: main_models.LockSnapshotResponseBodyLockedSnapshotInfo = None,
        request_id: str = None,
    ):
        # The locked snapshot information.
        self.locked_snapshot_info = locked_snapshot_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.locked_snapshot_info:
            self.locked_snapshot_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.locked_snapshot_info is not None:
            result['LockedSnapshotInfo'] = self.locked_snapshot_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockedSnapshotInfo') is not None:
            temp_model = main_models.LockSnapshotResponseBodyLockedSnapshotInfo()
            self.locked_snapshot_info = temp_model.from_map(m.get('LockedSnapshotInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class LockSnapshotResponseBodyLockedSnapshotInfo(DaraModel):
    def __init__(
        self,
        cool_off_period: int = None,
        cool_off_period_expired_time: str = None,
        lock_creation_time: str = None,
        lock_duration: int = None,
        lock_duration_start_time: str = None,
        lock_expired_time: str = None,
        lock_mode: str = None,
        lock_status: str = None,
        snapshot_id: str = None,
    ):
        # The cool-off period in compliance mode. Unit: hours.
        self.cool_off_period = cool_off_period
        # The time when the cool-off period in compliance mode ends. The time follows the [ISO 8601](https://www.alibabacloud.com/help/en/ecs/developer-reference/iso-8601-time-format) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.cool_off_period_expired_time = cool_off_period_expired_time
        # The time when the snapshot was locked. The time follows the [ISO 8601](https://www.alibabacloud.com/help/en/ecs/developer-reference/iso-8601-time-format) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.lock_creation_time = lock_creation_time
        # The lock duration. The snapshot lock automatically expires after the lock duration ends. Unit: days.
        self.lock_duration = lock_duration
        # The time when the lock duration starts. The time follows the [ISO 8601](https://www.alibabacloud.com/help/en/ecs/developer-reference/iso-8601-time-format) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. 
        # 
        # If you lock a snapshot that is in the progressing state, the lock duration starts only after the snapshot enters the accomplished state.
        self.lock_duration_start_time = lock_duration_start_time
        # The time when the lock expires. The time follows the [ISO 8601](https://www.alibabacloud.com/help/en/ecs/developer-reference/iso-8601-time-format) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.lock_expired_time = lock_expired_time
        # The lock mode. Valid values: 
        # - compliance: The snapshot is locked in compliance mode. A snapshot locked in compliance mode cannot be unlocked by any user and can be deleted only after the lock duration expires. Users cannot shorten the lock duration, but users with the required RAM permissions can extend the lock duration at any time. When locking a snapshot in compliance mode, you can optionally specify a cool-off period.
        self.lock_mode = lock_mode
        # The lock status. Valid values: 
        # - compliance-cooloff: The snapshot is locked in compliance mode but is still within the cool-off period. The snapshot cannot be deleted, but users with the required RAM permissions can unlock the snapshot, extend or shorten the cool-off period, and extend or shorten the lock duration. 
        # - compliance: The snapshot is locked in compliance mode and the cool-off period has ended. The snapshot cannot be unlocked or deleted, but users with the required RAM permissions can extend the lock duration. 
        # - expired: The snapshot was previously locked, but the lock duration has ended and the lock has expired. The snapshot is currently unlocked and can be deleted.
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

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

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

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockStatus') is not None:
            self.lock_status = m.get('LockStatus')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

