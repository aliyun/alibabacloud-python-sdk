# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class InstallAppResponseBody(DaraModel):
    def __init__(
        self,
        child_task_info: List[main_models.InstallAppResponseBodyChildTaskInfo] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.child_task_info = child_task_info
        # The ID of the request.
        self.request_id = request_id
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        if self.child_task_info:
            for v1 in self.child_task_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChildTaskInfo'] = []
        if self.child_task_info is not None:
            for k1 in self.child_task_info:
                result['ChildTaskInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_task_info = []
        if m.get('ChildTaskInfo') is not None:
            for k1 in m.get('ChildTaskInfo'):
                temp_model = main_models.InstallAppResponseBodyChildTaskInfo()
                self.child_task_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class InstallAppResponseBodyChildTaskInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        child_task_id: str = None,
        instance_id: str = None,
    ):
        self.app_id = app_id
        self.child_task_id = child_task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.child_task_id is not None:
            result['ChildTaskId'] = self.child_task_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChildTaskId') is not None:
            self.child_task_id = m.get('ChildTaskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

