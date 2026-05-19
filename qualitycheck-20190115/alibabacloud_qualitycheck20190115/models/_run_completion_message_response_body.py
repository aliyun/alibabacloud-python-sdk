# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class RunCompletionMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RunCompletionMessageResponseBodyData = None,
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
            temp_model = main_models.RunCompletionMessageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RunCompletionMessageResponseBodyData(DaraModel):
    def __init__(
        self,
        finish_reason: str = None,
        input_tokens: int = None,
        llm_request_id: str = None,
        output_tokens: int = None,
        text: str = None,
        total_tokens: int = None,
    ):
        self.finish_reason = finish_reason
        self.input_tokens = input_tokens
        self.llm_request_id = llm_request_id
        self.output_tokens = output_tokens
        self.text = text
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.llm_request_id is not None:
            result['LlmRequestId'] = self.llm_request_id

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.text is not None:
            result['Text'] = self.text

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('LlmRequestId') is not None:
            self.llm_request_id = m.get('LlmRequestId')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

