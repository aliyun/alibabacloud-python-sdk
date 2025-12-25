# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        backup_retention_period: str = None,
        dbinstance_id: str = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        region_id: str = None,
    ):
        # The number of days for which you can retain the backup data.
        self.backup_retention_period = backup_retention_period
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The backup cycle, which indicates the day of the week when the system regularly backs up data. Separate multiple dates with commas (`,`).
        # 
        # This parameter is required.
        self.preferred_backup_period = preferred_backup_period
        # The backup time window within which the backup task is performed. The time is displayed in `UTC`. For example, `12:00Z-13:00Z` indicates that the backup time window ranges from `12:00` (UTC) to `13:00` `(UTC)`.
        # 
        # This parameter is required.
        self.preferred_backup_time = preferred_backup_time
        # The region ID.
        # 
        # This parameter is required.
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

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

