# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ExecuteAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ExecuteAgentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The returned result.
        self.data = data
        # The error message returned when an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. The caller can use this field to determine whether the request was successful. Valid values: **true**: The request was successful. **false/null**: The request failed.
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
            temp_model = main_models.ExecuteAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ExecuteAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        finish_reason: str = None,
        input_tokens: int = None,
        llm_request_id: str = None,
        output_tokens: int = None,
        text: str = None,
        total_tokens: int = None,
        tyxm_plus_count: str = None,
        tyxm_turbo_count: str = None,
    ):
        # If streaming output is used, this value is null during generation. When generation is complete, the value is stop if the generation ended due to a stop token.
        self.finish_reason = finish_reason
        # The number of input tokens.
        self.input_tokens = input_tokens
        # The request ID returned by the large language model service.
        self.llm_request_id = llm_request_id
        # The number of output tokens.
        self.output_tokens = output_tokens
        # The result returned by the large language model.
        self.text = text
        # The total number of tokens.
        self.total_tokens = total_tokens
        # The number of times the plus model was used.
        self.tyxm_plus_count = tyxm_plus_count
        # The number of times the turbo model was used.
        self.tyxm_turbo_count = tyxm_turbo_count

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

        if self.tyxm_plus_count is not None:
            result['TyxmPlusCount'] = self.tyxm_plus_count

        if self.tyxm_turbo_count is not None:
            result['TyxmTurboCount'] = self.tyxm_turbo_count

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

        if m.get('TyxmPlusCount') is not None:
            self.tyxm_plus_count = m.get('TyxmPlusCount')

        if m.get('TyxmTurboCount') is not None:
            self.tyxm_turbo_count = m.get('TyxmTurboCount')

        return self

