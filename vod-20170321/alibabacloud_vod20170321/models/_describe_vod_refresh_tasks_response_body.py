# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodRefreshTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: main_models.DescribeVodRefreshTasksResponseBodyTasks = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.tasks = tasks
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tasks') is not None:
            temp_model = main_models.DescribeVodRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m.get('Tasks'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVodRefreshTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        task: List[main_models.DescribeVodRefreshTasksResponseBodyTasksTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for v1 in self.task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Task'] = []
        if self.task is not None:
            for k1 in self.task:
                result['Task'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k1 in m.get('Task'):
                temp_model = main_models.DescribeVodRefreshTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k1))

        return self

class DescribeVodRefreshTasksResponseBodyTasksTask(DaraModel):
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
        self.creation_time = creation_time
        self.description = description
        self.object_path = object_path
        self.object_type = object_type
        self.process = process
        self.status = status
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

