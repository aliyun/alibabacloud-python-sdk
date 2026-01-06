# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAutoSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_name: str = None,
        file_system_type: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        # The name of the automatic snapshot policy.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter.
        # *   The name can contain digits, colons (:), underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        # *   This parameter is empty by default.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        # 
        # This parameter is required.
        self.file_system_type = file_system_type
        # The days of a week on which to create automatic snapshots.
        # 
        # Cycle: week.
        # 
        # Valid values: 1 to 7. The values from 1 to 7 indicate the seven days in a week from Monday to Sunday.
        # 
        # If you want to create multiple auto snapshots within a week, you can specify multiple days from Monday to Sunday and separate the days with commas (,). You can specify a maximum of seven days.
        # 
        # This parameter is required.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of auto snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \\-1 (default). Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The points in time at which auto snapshots were created.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 23. The values from 0 to 23 indicate a total of 24 hours from 00:00 to 23:00. For example, the value 1 indicates 01:00.
        # 
        # If you want to create multiple auto snapshots within a day, you can specify multiple points in time and separate the points in time with commas (,). You can specify a maximum of 24 points in time.
        # 
        # This parameter is required.
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        return self

