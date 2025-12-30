# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitPackageJobShrinkRequest(DaraModel):
    def __init__(
        self,
        inputs_shrink: str = None,
        name: str = None,
        output_shrink: str = None,
        schedule_config_shrink: str = None,
        user_data: str = None,
    ):
        # The input of the job.
        # 
        # This parameter is required.
        self.inputs_shrink = inputs_shrink
        # The name of the job.
        self.name = name
        # The output of the job.
        # 
        # This parameter is required.
        self.output_shrink = output_shrink
        # The scheduling settings.
        self.schedule_config_shrink = schedule_config_shrink
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.output_shrink is not None:
            result['Output'] = self.output_shrink

        if self.schedule_config_shrink is not None:
            result['ScheduleConfig'] = self.schedule_config_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            self.output_shrink = m.get('Output')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config_shrink = m.get('ScheduleConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

