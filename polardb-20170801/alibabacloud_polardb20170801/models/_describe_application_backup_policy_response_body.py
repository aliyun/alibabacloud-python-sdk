# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        preferred_backup_period: str = None,
        preferred_backup_retention_period: int = None,
        preferred_backup_time: str = None,
        request_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The application type, such as polarclaw.
        self.application_type = application_type
        # The days of the week when automatic backups are performed. Separate multiple values with commas. Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday.
        self.preferred_backup_period = preferred_backup_period
        # The retention period of level-1 backups, in days.
        self.preferred_backup_retention_period = preferred_backup_retention_period
        # The time period when automatic backups are performed. The time is in the HH:mmZ-HH:mmZ format and in UTC.
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period

        if self.preferred_backup_retention_period is not None:
            result['PreferredBackupRetentionPeriod'] = self.preferred_backup_retention_period

        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')

        if m.get('PreferredBackupRetentionPeriod') is not None:
            self.preferred_backup_retention_period = m.get('PreferredBackupRetentionPeriod')

        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

