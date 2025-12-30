# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetSummaryTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetSummaryTaskResultResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

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
            temp_model = main_models.GetSummaryTaskResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

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

class GetSummaryTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        choices: List[main_models.GetSummaryTaskResultResponseBodyDataChoices] = None,
        created: int = None,
        id: str = None,
        model_id: str = None,
        request_id: str = None,
        time: str = None,
        total_tokens: int = None,
        usage: main_models.GetSummaryTaskResultResponseBodyDataUsage = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.model_id = model_id
        self.request_id = request_id
        self.time = time
        self.total_tokens = total_tokens
        self.usage = usage

    def validate(self):
        if self.choices:
            for v1 in self.choices:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['choices'] = []
        if self.choices is not None:
            for k1 in self.choices:
                result['choices'].append(k1.to_map() if k1 else None)

        if self.created is not None:
            result['created'] = self.created

        if self.id is not None:
            result['id'] = self.id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.time is not None:
            result['time'] = self.time

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k1 in m.get('choices'):
                temp_model = main_models.GetSummaryTaskResultResponseBodyDataChoices()
                self.choices.append(temp_model.from_map(k1))

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        if m.get('usage') is not None:
            temp_model = main_models.GetSummaryTaskResultResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetSummaryTaskResultResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        image_count: int = None,
        image_tokens: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.image_count = image_count
        self.image_tokens = image_tokens
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_count is not None:
            result['imageCount'] = self.image_count

        if self.image_tokens is not None:
            result['imageTokens'] = self.image_tokens

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')

        if m.get('imageTokens') is not None:
            self.image_tokens = m.get('imageTokens')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class GetSummaryTaskResultResponseBodyDataChoices(DaraModel):
    def __init__(
        self,
        finish_reason: str = None,
        index: int = None,
        message: main_models.GetSummaryTaskResultResponseBodyDataChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason

        if self.index is not None:
            result['index'] = self.index

        if self.message is not None:
            result['message'] = self.message.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('message') is not None:
            temp_model = main_models.GetSummaryTaskResultResponseBodyDataChoicesMessage()
            self.message = temp_model.from_map(m.get('message'))

        return self

class GetSummaryTaskResultResponseBodyDataChoicesMessage(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
        tool_calls: List[Dict[str, Any]] = None,
    ):
        self.content = content
        self.role = role
        self.tool_calls = tool_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        if self.tool_calls is not None:
            result['toolCalls'] = self.tool_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('toolCalls') is not None:
            self.tool_calls = m.get('toolCalls')

        return self

