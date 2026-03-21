# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceImageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
        tasks: main_models.UpdateInstanceImageResponseBodyTasks = None,
    ):
        self.request_id = request_id
        self.task_id = task_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Tasks') is not None:
            temp_model = main_models.UpdateInstanceImageResponseBodyTasks()
            self.tasks = temp_model.from_map(m.get('Tasks'))

        return self

class UpdateInstanceImageResponseBodyTasks(DaraModel):
    def __init__(
        self,
        child_tasks: List[main_models.UpdateInstanceImageResponseBodyTasksChildTasks] = None,
        parent_task_id: str = None,
    ):
        self.child_tasks = child_tasks
        self.parent_task_id = parent_task_id

    def validate(self):
        if self.child_tasks:
            for v1 in self.child_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChildTasks'] = []
        if self.child_tasks is not None:
            for k1 in self.child_tasks:
                result['ChildTasks'].append(k1.to_map() if k1 else None)

        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_tasks = []
        if m.get('ChildTasks') is not None:
            for k1 in m.get('ChildTasks'):
                temp_model = main_models.UpdateInstanceImageResponseBodyTasksChildTasks()
                self.child_tasks.append(temp_model.from_map(k1))

        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')

        return self

class UpdateInstanceImageResponseBodyTasksChildTasks(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
    ):
        self.instance_id = instance_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

