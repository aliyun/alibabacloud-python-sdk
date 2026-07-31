# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        enable_backup_log: str = None,
        log_backup_retention_period: int = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        request_id: str = None,
    ):
        # The number of days to retain data backups.
        self.backup_retention_period = backup_retention_period
        # Indicates whether real-time log backup is enabled. Valid values:
        # 
        # - **Enable**: enabled.
        # 
        # - **Disable**: disabled.
        self.enable_backup_log = enable_backup_log
        # The number of days to retain log backups.
        self.log_backup_retention_period = log_backup_retention_period
        # The data backup cycle. Separate multiple values with commas (,). Valid values:
        # 
        # - Monday
        # 
        # - Tuesday
        # 
        # - Wednesday
        # 
        # - Thursday
        # 
        # - Friday
        # 
        # - Saturday
        # 
        # - Sunday
        self.preferred_backup_period = preferred_backup_period
        # The data backup time. The time is in the HH:mmZ-HH:mmZ format.
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

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

