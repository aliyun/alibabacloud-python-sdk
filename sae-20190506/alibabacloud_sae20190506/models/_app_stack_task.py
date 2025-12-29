# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class AppStackTask(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        end_time: int = None,
        instance_id: str = None,
        stack_id: str = None,
        start_time: int = None,
        status: str = None,
        steps: List[main_models.AppStackTaskSteps] = None,
        task_id: str = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.instance_id = instance_id
        self.stack_id = stack_id
        self.start_time = start_time
        self.status = status
        self.steps = steps
        self.task_id = task_id

    def validate(self):
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        result['Steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['Steps'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.AppStackTaskSteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class AppStackTaskSteps(DaraModel):
    def __init__(
        self,
        code: str = None,
        duration: int = None,
        end_time: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.code = code
        self.duration = duration
        self.end_time = end_time
        self.id = id
        self.message = message
        self.name = name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

