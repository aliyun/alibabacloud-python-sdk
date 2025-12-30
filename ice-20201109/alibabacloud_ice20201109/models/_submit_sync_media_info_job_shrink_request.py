# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSyncMediaInfoJobShrinkRequest(DaraModel):
    def __init__(
        self,
        input_shrink: str = None,
        name: str = None,
        schedule_config_shrink: str = None,
        user_data: str = None,
    ):
        # The input of the job.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The job name.
        self.name = name
        # The scheduling parameters. This parameter is optional.
        self.schedule_config_shrink = schedule_config_shrink
        # The user data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.schedule_config_shrink is not None:
            result['ScheduleConfig'] = self.schedule_config_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config_shrink = m.get('ScheduleConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

