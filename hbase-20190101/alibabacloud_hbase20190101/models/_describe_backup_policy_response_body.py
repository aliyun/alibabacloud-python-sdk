# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        backup_retention_period: str = None,
        preferred_backup_end_time_utc: str = None,
        preferred_backup_period: str = None,
        preferred_backup_start_time_utc: str = None,
        preferred_backup_time: str = None,
        request_id: str = None,
    ):
        # The number of days for which backups are retained.
        self.backup_retention_period = backup_retention_period
        # The UTC time when the backup ends.
        self.preferred_backup_end_time_utc = preferred_backup_end_time_utc
        # The backup cycle. For example, Friday indicates that the backup is performed every Friday.
        self.preferred_backup_period = preferred_backup_period
        # The UTC time when the backup starts.
        self.preferred_backup_start_time_utc = preferred_backup_start_time_utc
        # The backup time range in the current time zone.
        self.preferred_backup_time = preferred_backup_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.preferred_backup_end_time_utc is not None:
            result['PreferredBackupEndTimeUTC'] = self.preferred_backup_end_time_utc

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_start_time_utc is not None:
            result['PreferredBackupStartTimeUTC'] = self.preferred_backup_start_time_utc

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('PreferredBackupEndTimeUTC') is not None:
            self.preferred_backup_end_time_utc = m.get('PreferredBackupEndTimeUTC')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupStartTimeUTC') is not None:
            self.preferred_backup_start_time_utc = m.get('PreferredBackupStartTimeUTC')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

