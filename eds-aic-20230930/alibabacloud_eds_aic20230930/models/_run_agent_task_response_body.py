# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class RunAgentTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        message: str = None,
        request_id: str = None,
        tasks: List[main_models.RunAgentTaskResponseBodyTasks] = None,
    ):
        self.code = code
        self.count = count
        self.message = message
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.RunAgentTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class RunAgentTaskResponseBodyTasks(DaraModel):
    def __init__(
        self,
        current_status: str = None,
        instance_id: str = None,
        running_at: str = None,
        task_id: str = None,
        user_prompt: str = None,
    ):
        self.current_status = current_status
        self.instance_id = instance_id
        self.running_at = running_at
        self.task_id = task_id
        self.user_prompt = user_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.running_at is not None:
            result['RunningAt'] = self.running_at

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RunningAt') is not None:
            self.running_at = m.get('RunningAt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        return self

