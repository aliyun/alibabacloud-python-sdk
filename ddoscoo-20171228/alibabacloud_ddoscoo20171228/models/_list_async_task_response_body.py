# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class ListAsyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        async_tasks: List[main_models.ListAsyncTaskResponseBodyAsyncTasks] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.async_tasks = async_tasks
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.async_tasks:
            for v1 in self.async_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k1 in self.async_tasks:
                result['AsyncTasks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.async_tasks = []
        if m.get('AsyncTasks') is not None:
            for k1 in m.get('AsyncTasks'):
                temp_model = main_models.ListAsyncTaskResponseBodyAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAsyncTaskResponseBodyAsyncTasks(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        task_id: int = None,
        task_params: str = None,
        task_result: str = None,
        task_status: int = None,
        task_type: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.task_id = task_id
        self.task_params = task_params
        self.task_result = task_result
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_params is not None:
            result['TaskParams'] = self.task_params

        if self.task_result is not None:
            result['TaskResult'] = self.task_result

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')

        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

