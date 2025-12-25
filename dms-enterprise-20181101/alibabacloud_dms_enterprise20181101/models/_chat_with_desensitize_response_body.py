# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ChatWithDesensitizeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ChatWithDesensitizeResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ChatWithDesensitizeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ChatWithDesensitizeResponseBodyData(DaraModel):
    def __init__(
        self,
        choices: List[main_models.ChatWithDesensitizeResponseBodyDataChoices] = None,
        created: str = None,
        message: str = None,
        model: str = None,
        status_code: str = None,
        type: str = None,
        usage: main_models.ChatWithDesensitizeResponseBodyDataUsage = None,
    ):
        self.choices = choices
        self.created = created
        self.message = message
        self.model = model
        self.status_code = status_code
        self.type = type
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
        result['Choices'] = []
        if self.choices is not None:
            for k1 in self.choices:
                result['Choices'].append(k1.to_map() if k1 else None)

        if self.created is not None:
            result['Created'] = self.created

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.type is not None:
            result['Type'] = self.type

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('Choices') is not None:
            for k1 in m.get('Choices'):
                temp_model = main_models.ChatWithDesensitizeResponseBodyDataChoices()
                self.choices.append(temp_model.from_map(k1))

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Usage') is not None:
            temp_model = main_models.ChatWithDesensitizeResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class ChatWithDesensitizeResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        completion_tokens: str = None,
        completion_tokens_details: Dict[str, str] = None,
        prompt_tokens: str = None,
        prompt_tokens_details: Dict[str, str] = None,
        total_tokens: str = None,
    ):
        self.completion_tokens = completion_tokens
        self.completion_tokens_details = completion_tokens_details
        self.prompt_tokens = prompt_tokens
        self.prompt_tokens_details = prompt_tokens_details
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_tokens is not None:
            result['CompletionTokens'] = self.completion_tokens

        if self.completion_tokens_details is not None:
            result['CompletionTokensDetails'] = self.completion_tokens_details

        if self.prompt_tokens is not None:
            result['PromptTokens'] = self.prompt_tokens

        if self.prompt_tokens_details is not None:
            result['PromptTokensDetails'] = self.prompt_tokens_details

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletionTokens') is not None:
            self.completion_tokens = m.get('CompletionTokens')

        if m.get('CompletionTokensDetails') is not None:
            self.completion_tokens_details = m.get('CompletionTokensDetails')

        if m.get('PromptTokens') is not None:
            self.prompt_tokens = m.get('PromptTokens')

        if m.get('PromptTokensDetails') is not None:
            self.prompt_tokens_details = m.get('PromptTokensDetails')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class ChatWithDesensitizeResponseBodyDataChoices(DaraModel):
    def __init__(
        self,
        finish_reason: str = None,
        logprobs: Dict[str, Any] = None,
        message: main_models.ChatWithDesensitizeResponseBodyDataChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.logprobs = logprobs
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
            result['FinishReason'] = self.finish_reason

        if self.logprobs is not None:
            result['Logprobs'] = self.logprobs

        if self.message is not None:
            result['Message'] = self.message.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')

        if m.get('Logprobs') is not None:
            self.logprobs = m.get('Logprobs')

        if m.get('Message') is not None:
            temp_model = main_models.ChatWithDesensitizeResponseBodyDataChoicesMessage()
            self.message = temp_model.from_map(m.get('Message'))

        return self

class ChatWithDesensitizeResponseBodyDataChoicesMessage(DaraModel):
    def __init__(
        self,
        content: str = None,
        reasoning_content: str = None,
        role: str = None,
    ):
        self.content = content
        self.reasoning_content = reasoning_content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.reasoning_content is not None:
            result['ReasoningContent'] = self.reasoning_content

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ReasoningContent') is not None:
            self.reasoning_content = m.get('ReasoningContent')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

