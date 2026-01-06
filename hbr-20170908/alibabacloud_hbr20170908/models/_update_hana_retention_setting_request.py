# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHanaRetentionSettingRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        disabled: bool = None,
        retention_days: int = None,
        schedule: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        # 
        # This parameter is required.
        self.database_name = database_name
        # Specifies whether to permanently retain the backup. Valid values:
        # 
        # *   true: The backup is permanently retained.
        # *   false: The backup is retained for the specified number of days.
        # 
        # This parameter is required.
        self.disabled = disabled
        # The retention period of the backup data. Unit: days. If you set the Disabled parameter to false, the backup is retained for the number of days specified by this parameter.
        # 
        # This parameter is required.
        self.retention_days = retention_days
        # The policy to update the retention period. Format: `I|{startTime}|{interval}`. The retention period is updated at an interval of {interval} starting from {startTime}.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour, and P1D indicates an interval of one day.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

