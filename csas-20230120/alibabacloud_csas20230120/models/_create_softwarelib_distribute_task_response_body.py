# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateSoftwarelibDistributeTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: main_models.CreateSoftwarelibDistributeTaskResponseBodyTask = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The information about the created task.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Task') is not None:
            temp_model = main_models.CreateSoftwarelibDistributeTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class CreateSoftwarelibDistributeTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        software_name: str = None,
        status: str = None,
        support_os: str = None,
        task_id: str = None,
    ):
        # The task creation time as a second-level UNIX timestamp.
        self.create_time = create_time
        # The task name.
        self.name = name
        # The software name.
        self.software_name = software_name
        # The task status. Valid values:
        # - **enabled**: enabled.
        # - **disabled**: disabled.
        # 
        # The initial status of a task after creation is disabled.
        self.status = status
        # The operating system to which the task applies. Valid values:
        # - **Windows**: Windows.
        # - **Mac(Apple)**: macOS with Apple silicon.
        # - **Mac(Intel)**: macOS with Intel processors.
        self.support_os = support_os
        # The task ID, which is used to query the task execution result.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.software_name is not None:
            result['SoftwareName'] = self.software_name

        if self.status is not None:
            result['Status'] = self.status

        if self.support_os is not None:
            result['SupportOs'] = self.support_os

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportOs') is not None:
            self.support_os = m.get('SupportOs')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

