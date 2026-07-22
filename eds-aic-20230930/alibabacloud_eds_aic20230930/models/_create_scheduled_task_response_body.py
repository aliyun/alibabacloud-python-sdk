# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateScheduledTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        tasks: List[main_models.CreateScheduledTaskResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.CreateScheduledTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class CreateScheduledTaskResponseBodyTasks(DaraModel):
    def __init__(
        self,
        instance_results: List[main_models.CreateScheduledTaskResponseBodyTasksInstanceResults] = None,
        scheduled_id: str = None,
        task_config_id: str = None,
    ):
        self.instance_results = instance_results
        self.scheduled_id = scheduled_id
        self.task_config_id = task_config_id

    def validate(self):
        if self.instance_results:
            for v1 in self.instance_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceResults'] = []
        if self.instance_results is not None:
            for k1 in self.instance_results:
                result['InstanceResults'].append(k1.to_map() if k1 else None)

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.task_config_id is not None:
            result['TaskConfigId'] = self.task_config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_results = []
        if m.get('InstanceResults') is not None:
            for k1 in m.get('InstanceResults'):
                temp_model = main_models.CreateScheduledTaskResponseBodyTasksInstanceResults()
                self.instance_results.append(temp_model.from_map(k1))

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('TaskConfigId') is not None:
            self.task_config_id = m.get('TaskConfigId')

        return self

class CreateScheduledTaskResponseBodyTasksInstanceResults(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        instance_id: str = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.instance_id = instance_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

