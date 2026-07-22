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
        # The request ID.
        self.request_id = request_id
        # The task status. Valid values:
        # 
        # - finish: The task is completed. You can call a task query operation to obtain the download URL of the task file.
        # 
        # - start: The task has started.
        # 
        # - error: The task failed.
        # 
        # - expire: The task has expired. The task file is no longer valid and cannot be downloaded.
        # 
        # This field is returned only under specific conditions, such as when the task is completed synchronously. In regular responses, only RequestId is returned. Use a task query operation to obtain the real-time status.
        self.status = status
        # The task ID, which uniquely identifies the task. This field is returned only under specific conditions, such as when the task is completed synchronously. In regular responses, only RequestId is returned. Use a task query operation to obtain the task status and download URL.
        self.task_id = task_id
        # The name of the file download task. This field is returned only under specific conditions, such as when the task is completed synchronously. In regular responses, only RequestId is returned.
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

