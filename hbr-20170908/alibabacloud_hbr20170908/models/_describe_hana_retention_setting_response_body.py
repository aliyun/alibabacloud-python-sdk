# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHanaRetentionSettingResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        code: str = None,
        database_name: str = None,
        disabled: bool = None,
        message: str = None,
        request_id: str = None,
        retention_days: int = None,
        schedule: str = None,
        success: bool = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The database name.
        self.database_name = database_name
        # Indicates whether the backup is permanently retained. Valid values:
        # 
        # *   true: The backup is permanently retained.
        # *   false: The backup is retained for the specified number of days.
        self.disabled = disabled
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The number of days for which the backup is retained. If the value of the Disabled parameter is false, the backup is retained for the number of days specified by this parameter.
        self.retention_days = retention_days
        # The policy to update the retention period. Format: `I|{startTime}|{interval}`, which indicates that the retention period is updated at an interval of {interval} starting from {startTime}.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the backup vault.
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

        if self.code is not None:
            result['Code'] = self.code

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.success is not None:
            result['Success'] = self.success

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

