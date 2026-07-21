# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAsyncTaskRequest(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        cds_id: str = None,
    ):
        # The asynchronous task ID. When you call the [CopyCdsFile](https://help.aliyun.com/document_detail/2247626.html) operation to copy a folder, this field is returned because the copy is performed asynchronously in the background. Call this operation and pass in the asynchronous task ID to retrieve the task details.
        # 
        # This parameter is required.
        self.async_task_id = async_task_id
        # The enterprise network disk ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id

        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        return self

