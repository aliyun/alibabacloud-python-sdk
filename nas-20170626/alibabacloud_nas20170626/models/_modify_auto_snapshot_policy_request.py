# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAutoSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        # The ID of the automatic snapshot policy.
        # 
        # You can call DescribeAutoSnapshotPolicies to query available automatic snapshot policies.
        # 
        # This parameter is required.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The name of the automatic snapshot policy. If this parameter is left empty, the policy name is not modified.
        # 
        # Limits:
        # 
        # - The name must be 2 to 128 characters in length.
        # - The name must start with a letter.
        # - The name can contain digits, colons (:), underscores (_), and hyphens (-). The name cannot start with `http://` or `https://`.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The days of the week on which automatic snapshots are created.
        # 
        # Cycle: week.
        # 
        # Valid values: 1 to 7. For example, 1 indicates Monday. To create multiple automatic snapshots within a week, specify multiple days and separate them with commas (,). You can specify up to 7 days.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of automatic snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # - -1 (default): Automatic snapshots are permanently retained.
        # - 1 to 65536: Automatic snapshots are retained for the specified number of days.
        self.retention_days = retention_days
        # The points in time at which automatic snapshots are created.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 23, which correspond to the 24 points in time from 00:00 to 23:00. For example, 1 indicates 01:00. To create multiple automatic snapshots within a day, specify multiple points in time and separate them with commas (,). You can specify up to 24 points in time.
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name

        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')

        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        return self

