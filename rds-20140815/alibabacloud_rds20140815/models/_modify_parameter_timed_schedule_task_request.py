# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyParameterTimedScheduleTaskRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        switch_time: str = None,
        task_id: int = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.switch_time = switch_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

