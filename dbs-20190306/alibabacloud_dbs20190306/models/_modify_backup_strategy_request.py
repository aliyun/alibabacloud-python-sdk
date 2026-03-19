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
        # The interval at which you want to perform incremental log backups. Unit: seconds.
        # 
        # > This parameter takes effect only when physical backups are performed.
        self.backup_log_interval_seconds = backup_log_interval_seconds
        # The day of each week when the full backup task runs. Valid values:
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
        # 
        # This parameter is required.
        self.backup_period = backup_period
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The start time of the full backup task. Specify the time in the HH:mm format.
        self.backup_start_time = backup_start_time
        # The backup method that you want to use for full backups. Valid values:
        # 
        # - **simple**: scheduled backup. If you specify this value for the BackupStrategyType parameter, you must also specify the BackupPeriod and BackupStartTime parameters.
        # 
        # - **Manual**: manual backup.
        # 
        # > Default value: **simple**.
        self.backup_strategy_type = backup_strategy_type
        # The client token that is used to ensure the idempotence of the request.
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

