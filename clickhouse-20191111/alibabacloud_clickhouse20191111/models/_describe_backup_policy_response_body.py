# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        backup_size: str = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        request_id: str = None,
        switch: str = None,
    ):
        # The retention period for the backup data. By default, the backup data is retained for seven days. Valid values: 7 to 730. Unit: day.
        self.backup_retention_period = backup_retention_period
        # The size of the backup data. Unit: MB.
        self.backup_size = backup_size
        # The day of a week when the system regularly backs up data. Valid values:
        # 
        # *   **Monday**
        # *   **Tuesday**
        # *   **Wednesday**
        # *   **Thursday**
        # *   **Friday**
        # *   **Saturday**
        # *   **Sunday**
        self.preferred_backup_period = preferred_backup_period
        # The backup window. The time is displayed in Coordinated Universal Time (UTC).
        self.preferred_backup_time = preferred_backup_time
        # The request ID.
        self.request_id = request_id
        # Indicates whether the backup feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.switch = switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.switch is not None:
            result['Switch'] = self.switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        return self

