# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAsyncTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        task_code: str = None,
        task_execute_time: str = None,
        task_name: str = None,
        task_param: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.task_code = task_code
        self.task_execute_time = task_execute_time
        self.task_name = task_name
        self.task_param = task_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_execute_time is not None:
            result['TaskExecuteTime'] = self.task_execute_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_param is not None:
            result['TaskParam'] = self.task_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskExecuteTime') is not None:
            self.task_execute_time = m.get('TaskExecuteTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')

        return self

