# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RunAgentResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.RunAgentResponseBodyData = None,
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
            temp_model = main_models.RunAgentResponseBodyData()
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

class RunAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        function_call_responses: List[main_models.RunAgentResponseBodyDataFunctionCallResponses] = None,
        input_tokens: int = None,
        output_tokens: int = None,
        response: main_models.RunAgentResponseBodyDataResponse = None,
        thread_id: str = None,
        trace_id: str = None,
        version_id: str = None,
    ):
        self.function_call_responses = function_call_responses
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.response = response
        self.thread_id = thread_id
        self.trace_id = trace_id
        self.version_id = version_id

    def validate(self):
        if self.function_call_responses:
            for v1 in self.function_call_responses:
                 if v1:
                    v1.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['functionCallResponses'] = []
        if self.function_call_responses is not None:
            for k1 in self.function_call_responses:
                result['functionCallResponses'].append(k1.to_map() if k1 else None)

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.response is not None:
            result['response'] = self.response.to_map()

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_call_responses = []
        if m.get('functionCallResponses') is not None:
            for k1 in m.get('functionCallResponses'):
                temp_model = main_models.RunAgentResponseBodyDataFunctionCallResponses()
                self.function_call_responses.append(temp_model.from_map(k1))

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('response') is not None:
            temp_model = main_models.RunAgentResponseBodyDataResponse()
            self.response = temp_model.from_map(m.get('response'))

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

class RunAgentResponseBodyDataResponse(DaraModel):
    def __init__(
        self,
        choices: List[main_models.RunAgentResponseBodyDataResponseChoices] = None,
        created: int = None,
        id: str = None,
        model_id: str = None,
        time: str = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.model_id = model_id
        self.time = time

    def validate(self):
        if self.choices:
            for v1 in self.choices:
                 if v1:
                    v1.validate()

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

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k1 in m.get('choices'):
                temp_model = main_models.RunAgentResponseBodyDataResponseChoices()
                self.choices.append(temp_model.from_map(k1))

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class RunAgentResponseBodyDataResponseChoices(DaraModel):
    def __init__(
        self,
        finish_reason: str = None,
        index: int = None,
        message: main_models.RunAgentResponseBodyDataResponseChoicesMessage = None,
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
            temp_model = main_models.RunAgentResponseBodyDataResponseChoicesMessage()
            self.message = temp_model.from_map(m.get('message'))

        return self

class RunAgentResponseBodyDataResponseChoicesMessage(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
        role_display_name: str = None,
    ):
        self.content = content
        self.role = role
        self.role_display_name = role_display_name

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

        if self.role_display_name is not None:
            result['roleDisplayName'] = self.role_display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('roleDisplayName') is not None:
            self.role_display_name = m.get('roleDisplayName')

        return self

class RunAgentResponseBodyDataFunctionCallResponses(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        end_time: str = None,
        function_args: str = None,
        function_name: str = None,
        result: str = None,
        start_time: str = None,
    ):
        self.display_name = display_name
        self.end_time = end_time
        self.function_args = function_args
        self.function_name = function_name
        self.result = result
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.function_args is not None:
            result['functionArgs'] = self.function_args

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.result is not None:
            result['result'] = self.result

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('functionArgs') is not None:
            self.function_args = m.get('functionArgs')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

