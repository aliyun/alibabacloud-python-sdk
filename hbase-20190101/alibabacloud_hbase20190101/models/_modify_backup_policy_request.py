# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        preferred_backup_end_time_utc: str = None,
        preferred_backup_period: str = None,
        preferred_backup_start_time_utc: str = None,
        preferred_backup_time: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The UTC time when the backup ends.
        self.preferred_backup_end_time_utc = preferred_backup_end_time_utc
        # The backup cycle. Valid values:
        # - Monday: performs backup every Monday.
        # - Tuesday: performs backup every Tuesday.
        # - Wednesday: performs backup every Wednesday.
        # - Thursday: performs backup every Thursday.
        # - Friday: performs backup every Friday.
        # - Saturday: performs backup every Saturday.
        # - Sunday: performs backup every Sunday.
        # 
        # This parameter is required.
        self.preferred_backup_period = preferred_backup_period
        # The UTC time when the backup starts.
        self.preferred_backup_start_time_utc = preferred_backup_start_time_utc
        # The backup time range in the current time zone. The interval is 1 hour.
        # 
        # This parameter is required.
        self.preferred_backup_time = preferred_backup_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.preferred_backup_end_time_utc is not None:
            result['PreferredBackupEndTimeUTC'] = self.preferred_backup_end_time_utc

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_start_time_utc is not None:
            result['PreferredBackupStartTimeUTC'] = self.preferred_backup_start_time_utc

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PreferredBackupEndTimeUTC') is not None:
            self.preferred_backup_end_time_utc = m.get('PreferredBackupEndTimeUTC')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupStartTimeUTC') is not None:
            self.preferred_backup_start_time_utc = m.get('PreferredBackupStartTimeUTC')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        return self

