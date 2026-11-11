# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupStrategyRequest(DaraModel):
    def __init__(
        self,
        backup_log_interval_seconds: int = None,
        backup_period: str = None,
        backup_plan_id: str = None,
        backup_start_time: str = None,
        backup_strategy_type: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The incremental backup interval in seconds.
        # > Only physical backups are supported.
        self.backup_log_interval_seconds = backup_log_interval_seconds
        # The full backup cycle. Valid values:
        # - Monday: Monday
        # - Tuesday: Tuesday
        # - Wednesday: Wednesday
        # - Thursday: Thursday
        # - Friday: Friday
        # - Saturday: Saturday
        # - Sunday: Sunday
        # 
        # > You must specify at least two days of the week for BackupPeriod and separate the days with commas (,).
        # 
        # This parameter is required.
        self.backup_period = backup_period
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The start time of the full backup. Format: HH:mm.
        # 
        # > This parameter is required.
        self.backup_start_time = backup_start_time
        # The full backup epoch. Valid values:
        # - **simple**: periodic backup. This value is used together with BackupPeriod and BackupStartTime.
        # - **manual**: manual backup.
        # 
        # > Default value: **simple**.
        self.backup_strategy_type = backup_strategy_type
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_log_interval_seconds is not None:
            result['BackupLogIntervalSeconds'] = self.backup_log_interval_seconds

        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_strategy_type is not None:
            result['BackupStrategyType'] = self.backup_strategy_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLogIntervalSeconds') is not None:
            self.backup_log_interval_seconds = m.get('BackupLogIntervalSeconds')

        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStrategyType') is not None:
            self.backup_strategy_type = m.get('BackupStrategyType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

