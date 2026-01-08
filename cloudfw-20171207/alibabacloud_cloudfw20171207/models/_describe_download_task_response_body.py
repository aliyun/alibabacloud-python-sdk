# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeDownloadTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.DescribeDownloadTaskResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The tasks.
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
                temp_model = main_models.DescribeDownloadTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDownloadTaskResponseBodyTasks(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        expire_time: int = None,
        file_size: str = None,
        file_url: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The time when the task was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the task expires. The value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time
        # The size of the file.
        self.file_size = file_size
        # The URL of the OSS file.
        self.file_url = file_url
        # The status of the task. Valid values:
        # 
        # *   **finish**
        # *   **start**
        # *   **error**
        # *   **expire**: The task file is invalid and cannot be downloaded.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The name of the task.
        self.task_name = task_name
        # The type of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

