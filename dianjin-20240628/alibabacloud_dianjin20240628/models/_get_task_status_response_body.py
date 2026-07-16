# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        # Execution time, in milliseconds
        self.cost = cost
        # Response data. The current status of the task.
        # 
        # - invalid: Parameters or dependent resources are unavailable.
        # 
        # - success: The task completed successfully.
        # 
        # - evict: The task was canceled.
        # 
        # - error: The task failed.
        # 
        # - running: The task is running.
        # 
        # - pending: The task is queued.
        self.data = data
        # Data type
        self.data_type = data_type
        # Error code
        self.err_code = err_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the request succeeded
        self.success = success
        # Timestamp
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

