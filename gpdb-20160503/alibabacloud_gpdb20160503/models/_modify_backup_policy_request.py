# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        dbinstance_id: str = None,
        enable_recovery_point: bool = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        recovery_point_period: str = None,
    ):
        # The number of days for which data backups are retained. Default value: 7. Maximum value: 7. Valid values: 1 to 7.
        self.backup_retention_period = backup_retention_period
        # The ID of the instance.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specified region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable automatic recovery point creation. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # Default value: true.
        self.enable_recovery_point = enable_recovery_point
        # The data backup cycle. Separate multiple values with commas (,). Valid values:
        # 
        # - Monday: Monday.
        # - Tuesday: Tuesday.
        # - Wednesday: Wednesday.
        # - Thursday: Thursday.
        # - Friday: Friday.
        # - Saturday: Saturday.
        # - Sunday: Sunday.
        # 
        # This parameter is required.
        self.preferred_backup_period = preferred_backup_period
        # The data backup time. Default value: 00:00Z-01:00Z. Format: HH:mmZ-HH:mmZ (UTC).
        # 
        # This parameter is required.
        self.preferred_backup_time = preferred_backup_time
        # The frequency of recovery points. Valid values:
        # 
        # - **1**: Every hour.
        # - **2**: Every two hours.
        # - **4**: Every four hours.
        # - **8**: Every eight hours.
        # Default value: **1**.
        self.recovery_point_period = recovery_point_period

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

        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')

        return self

