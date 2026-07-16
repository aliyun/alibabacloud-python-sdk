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
        # - The name must be 2 to 128 characters in length.
        # - The name must start with a letter or a Chinese character.
        # - The name can contain digits, colons (:), underscores (_), or hyphens (-). It cannot start with `http://` or `https://`.
        # - Default value: empty.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The type of the file system.
        # 
        # Valid values: extreme (Extreme NAS).
        # 
        # This parameter is required.
        self.file_system_type = file_system_type
        # The days of the week on which automatic snapshots are created.
        # 
        # Cycle: week.
        # 
        # Valid values: 1 to 7, which represent Monday through Sunday.
        # 
        # To create automatic snapshots on multiple days in a week, specify multiple values separated by commas (,). You can specify a maximum of 7 values.
        # 
        # This parameter is required.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of automatic snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # - -1 (default): Automatic snapshots are permanently retained. When the snapshot quota is reached, the earliest automatic snapshots are automatically deleted.
        # - 1 to 65536: Automatic snapshots are retained for the specified number of days. Snapshots are subject to automatic release after the retention period expires.
        self.retention_days = retention_days
        # The time points at which automatic snapshots are created.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 23, which represent the 24 time points from 00:00 to 23:00. For example, 1 indicates 01:00.
        # 
        # To create multiple automatic snapshots within a day, specify multiple time points separated by commas (,). You can specify a maximum of 24 time points.
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

