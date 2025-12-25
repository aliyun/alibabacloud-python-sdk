# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListUploadTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.ListUploadTasksResponseBodyTasks] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The file upload tasks.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListUploadTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class ListUploadTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        error_code: str = None,
        status: str = None,
        type: str = None,
        upload_id: str = None,
        upload_task_name: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The error message returned when the file upload task failed.
        self.description = description
        # The error code. Multiple error codes are separated by commas (,).
        # 
        # *   **InvalidUrl**: The URL format is incorrect.
        # *   **InvalidDomain**: The domain ownership fails to be verified.
        # *   **QuotaExcess**: The quota limit has been reached.
        # *   **OtherErrors**: Other errors.
        self.error_code = error_code
        # The task status.
        # 
        # *   **Complete**: The task is complete.
        # *   **Refreshing**: The task is in progress.
        # *   **Failed**: The task failed.
        self.status = status
        # The task type. Valid values:
        # 
        # *   **file**: purges the cache by file URL.
        # *   **preload**: prefetches files.
        # *   **directory**: purges the cache by directory.
        # *   **ignoreparams**: purges the cache by URL with specified parameters ignored.
        self.type = type
        # The ID of the file upload task.
        self.upload_id = upload_id
        # The name of the file upload task.
        self.upload_task_name = upload_task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        if self.upload_task_name is not None:
            result['UploadTaskName'] = self.upload_task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('UploadTaskName') is not None:
            self.upload_task_name = m.get('UploadTaskName')

        return self

