# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeRefreshTaskByIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.DescribeRefreshTaskByIdResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Details about tasks.
        self.tasks = tasks
        # The total number of tasks.
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.DescribeRefreshTaskByIdResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRefreshTaskByIdResponseBodyTasks(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        object_path: str = None,
        object_type: str = None,
        process: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The time when the task was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The error returned when the refresh or prefetch task failed. Valid values:
        # 
        # *   **Internal Error**
        # *   **Origin Timeout**
        # *   **Origin Return StatusCode 5XX**
        self.description = description
        # The path of the object refreshed by the refresh task.
        self.object_path = object_path
        # The type of the task. Valid values:
        # 
        # *   **file**: refreshes an individual file.
        # *   **directory**: refreshes files in the specified directory.
        # *   **preload**: prefetches an individual file.
        # *   **regex**: refreshes content based on a regular expression.
        self.object_type = object_type
        # The progress of the task, in percentage.
        self.process = process
        # The status of the task. Valid values:
        # 
        # *   **Complete**
        # *   **Pending**
        # *   **Refreshing**
        # *   **Failed**
        self.status = status
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.object_path is not None:
            result['ObjectPath'] = self.object_path

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.process is not None:
            result['Process'] = self.process

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

