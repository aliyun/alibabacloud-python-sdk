# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateContextDatabaseSyncJobScheduleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        daily_times: List[str] = None,
        interval_minutes: int = None,
        job_id: str = None,
        missed_policy: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.client_token = client_token
        self.daily_times = daily_times
        self.interval_minutes = interval_minutes
        # This parameter is required.
        self.job_id = job_id
        self.missed_policy = missed_policy
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.daily_times is not None:
            result['DailyTimes'] = self.daily_times

        if self.interval_minutes is not None:
            result['IntervalMinutes'] = self.interval_minutes

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.missed_policy is not None:
            result['MissedPolicy'] = self.missed_policy

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DailyTimes') is not None:
            self.daily_times = m.get('DailyTimes')

        if m.get('IntervalMinutes') is not None:
            self.interval_minutes = m.get('IntervalMinutes')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MissedPolicy') is not None:
            self.missed_policy = m.get('MissedPolicy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

