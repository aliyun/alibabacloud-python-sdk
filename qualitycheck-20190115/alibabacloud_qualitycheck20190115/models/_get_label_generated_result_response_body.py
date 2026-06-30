# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetLabelGeneratedResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetLabelGeneratedResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Other values indicate failure. You can use this field to determine the cause of failure.
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned when the request fails.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. true: The call was successful. false: The call failed.
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
            temp_model = main_models.GetLabelGeneratedResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLabelGeneratedResultResponseBodyData(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        llm_call_num: int = None,
        output_tokens: int = None,
        result_file_url: str = None,
        task_id: str = None,
    ):
        # The number of input tokens for the LLM.
        self.input_tokens = input_tokens
        # The number of LLM calls.
        self.llm_call_num = llm_call_num
        # The number of output tokens for the LLM.
        self.output_tokens = output_tokens
        # The pre-signed download URL of the result file.
        self.result_file_url = result_file_url
        # The ID of the generation task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.llm_call_num is not None:
            result['LlmCallNum'] = self.llm_call_num

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.result_file_url is not None:
            result['ResultFileUrl'] = self.result_file_url

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('LlmCallNum') is not None:
            self.llm_call_num = m.get('LlmCallNum')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('ResultFileUrl') is not None:
            self.result_file_url = m.get('ResultFileUrl')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

