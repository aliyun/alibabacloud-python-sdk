# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class DebugModelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DebugModelResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value SUCCESS indicates success.
        self.code = code
        # The model debugging result.
        self.data = data
        # The HTTP status code. The value 200 indicates success.
        self.http_status_code = http_status_code
        # The request processing result message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.DebugModelResponseBodyData()
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

class DebugModelResponseBodyData(DaraModel):
    def __init__(
        self,
        connection_id: str = None,
        debug_success: bool = None,
        error_code: str = None,
        error_message: str = None,
        input_tokens: int = None,
        latency_ms: int = None,
        model_id: str = None,
        output_tokens: int = None,
        response: str = None,
        status: str = None,
    ):
        # The model connection ID.
        self.connection_id = connection_id
        # Indicates whether the model debugging was successful.
        self.debug_success = debug_success
        # The error code returned when debugging fails.
        self.error_code = error_code
        # The error message returned when debugging fails.
        self.error_message = error_message
        # The number of input tokens consumed by this model debugging request.
        self.input_tokens = input_tokens
        # The time consumed by this model debugging call, in milliseconds.
        self.latency_ms = latency_ms
        # The model ID.
        self.model_id = model_id
        # The number of output tokens consumed by this model debugging response.
        self.output_tokens = output_tokens
        # The text response returned by the model when debugging succeeds. This value is empty when debugging fails.
        self.response = response
        # The debug result status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_id is not None:
            result['connectionId'] = self.connection_id

        if self.debug_success is not None:
            result['debugSuccess'] = self.debug_success

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.latency_ms is not None:
            result['latencyMs'] = self.latency_ms

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.response is not None:
            result['response'] = self.response

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionId') is not None:
            self.connection_id = m.get('connectionId')

        if m.get('debugSuccess') is not None:
            self.debug_success = m.get('debugSuccess')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('latencyMs') is not None:
            self.latency_ms = m.get('latencyMs')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('response') is not None:
            self.response = m.get('response')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

