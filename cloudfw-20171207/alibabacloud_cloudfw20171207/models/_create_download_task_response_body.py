# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDownloadTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        task_id: int = None,
        task_name: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The task status. Valid values:
        # 
        # - finish: The task is completed. You can query the task to obtain the download URL of the task file.
        # - start: The task is started.
        # - error: The task failed.
        # - expire: The task has expired. The task file is invalid and cannot be downloaded.
        # 
        # Note: This field is returned only under specific conditions, such as when the task is completed synchronously. A standard response returns only RequestId. To query the real-time status, call a task query operation.
        self.status = status
        # The unique identifier of the task. Note: This field is returned only under specific conditions, such as when the task is completed synchronously. A standard response returns only RequestId. To obtain the task status and download URL, call a task query operation.
        self.task_id = task_id
        # The name of the file download task. Note: This field is returned only under specific conditions, such as when the task is completed synchronously. A standard response returns only RequestId.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

