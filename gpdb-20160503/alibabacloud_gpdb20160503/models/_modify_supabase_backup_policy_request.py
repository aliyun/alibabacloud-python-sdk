# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySupabaseBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        enable_recovery_point: bool = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        project_id: str = None,
        recovery_point_period: str = None,
        region_id: str = None,
    ):
        # The data backup retention period. Unit: days. Valid values: 1 to 7.
        self.backup_retention_period = backup_retention_period
        # Specifies whether to enable automatic recovery points. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # If this parameter is not specified, false is used.
        self.enable_recovery_point = enable_recovery_point
        # The data backup cycle. Separate multiple values with commas (,). Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday.
        # 
        # This parameter is required.
        self.preferred_backup_period = preferred_backup_period
        # The start time of the data backup. The time is in UTC and follows the HH:mmZ format, such as 01:00Z. The HH:mmZ-HH:mmZ time range format is also supported, and the server uses the start time of the range.
        # 
        # This parameter is required.
        self.preferred_backup_time = preferred_backup_time
        # Instance ID of the Supabase instance. You can obtain instance ID on the Supabase page in the console.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The interval for the automatic creation of recovery points. Unit: hours. Valid values: 1/6 (10 minutes), 1/2 (30 minutes), 1, 2, 4, and 8. This parameter takes effect only when EnableRecoveryPoint is set to true. If this parameter is not specified, the default value 1 is used. If EnableRecoveryPoint is set to false, this parameter is ignored.
        self.recovery_point_period = recovery_point_period
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

