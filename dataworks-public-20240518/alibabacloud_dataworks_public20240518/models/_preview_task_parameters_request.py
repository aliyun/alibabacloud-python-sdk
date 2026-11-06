# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreviewTaskParametersRequest(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        cron: str = None,
        parameters: str = None,
        preview_count: int = None,
        project_env: str = None,
        project_id: int = None,
        start_time: str = None,
    ):
        # The business date. The value is a 13-digit UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.bizdate = bizdate
        # The scheduling CRON expression.
        # 
        # This parameter is required.
        self.cron = cron
        # The list of script parameters. The length cannot exceed 65,535 characters. Separate multiple parameters with spaces, such as para1=$bizdate para2=$[hh24]. An empty string is allowed.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The number of scheduling cycles to preview. Valid values: 1 to 10. Default value: 3.
        self.preview_count = preview_count
        # The project environment. Valid values:
        # - Prod: production
        # - Dev: development
        # Default value: Prod.
        self.project_env = project_env
        # The workspace ID. The workspace must belong to the current tenant.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The preview start time for the first scheduling day. The format is HH:mm:ss. Default value: 00:00:00. This parameter takes effect only for non-daily schedules and is used to filter out cycles that occur before this time on the first scheduling day.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.cron is not None:
            result['Cron'] = self.cron

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.preview_count is not None:
            result['PreviewCount'] = self.preview_count

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PreviewCount') is not None:
            self.preview_count = m.get('PreviewCount')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

