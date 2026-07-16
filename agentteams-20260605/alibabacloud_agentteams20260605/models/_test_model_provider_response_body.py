# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class TestModelProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TestModelProviderResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.TestModelProviderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TestModelProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        input_tokens: int = None,
        latency_ms: int = None,
        output_tokens: int = None,
        response: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.input_tokens = input_tokens
        self.latency_ms = latency_ms
        self.output_tokens = output_tokens
        self.response = response
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.latency_ms is not None:
            result['LatencyMs'] = self.latency_ms

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.response is not None:
            result['Response'] = self.response

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('LatencyMs') is not None:
            self.latency_ms = m.get('LatencyMs')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('Response') is not None:
            self.response = m.get('Response')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

