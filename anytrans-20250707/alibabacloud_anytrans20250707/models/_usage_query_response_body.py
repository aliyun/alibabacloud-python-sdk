# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class UsageQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.UsageQueryResponseBodyData] = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.UsageQueryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class UsageQueryResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        task_id: str = None,
        total_tokens: int = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.task_id = task_id
        self.total_tokens = total_tokens
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

