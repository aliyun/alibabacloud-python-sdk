# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetMemoryTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMemoryTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The task details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetMemoryTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetMemoryTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error: main_models.GetMemoryTaskResponseBodyDataError = None,
        memories: List[main_models.GetMemoryTaskResponseBodyDataMemories] = None,
        status: str = None,
        task_id: str = None,
    ):
        # The task error returned only when the status is FAILED or UNKNOWN. This does not indicate that the current query failed.
        self.error = error
        # The memories returned only when the status is SUCCEEDED. An empty array is allowed.
        self.memories = memories
        # The extraction task status.
        # 
        # This parameter is required.
        self.status = status
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        if self.error:
            self.error.validate()
        if self.memories:
            for v1 in self.memories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['error'] = self.error.to_map()

        result['memories'] = []
        if self.memories is not None:
            for k1 in self.memories:
                result['memories'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            temp_model = main_models.GetMemoryTaskResponseBodyDataError()
            self.error = temp_model.from_map(m.get('error'))

        self.memories = []
        if m.get('memories') is not None:
            for k1 in m.get('memories'):
                temp_model = main_models.GetMemoryTaskResponseBodyDataMemories()
                self.memories.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class GetMemoryTaskResponseBodyDataMemories(DaraModel):
    def __init__(
        self,
        memory_id: str = None,
    ):
        # The long-term memory ID.
        self.memory_id = memory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        return self

class GetMemoryTaskResponseBodyDataError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The task error code.
        self.code = code
        # The task error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

