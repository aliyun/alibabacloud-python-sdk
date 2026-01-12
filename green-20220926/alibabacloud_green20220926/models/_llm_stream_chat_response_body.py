# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class LlmStreamChatResponseBody(DaraModel):
    def __init__(
        self,
        choices: List[main_models.LlmStreamChatResponseBodyChoices] = None,
        created: int = None,
        error: main_models.LlmStreamChatResponseBodyError = None,
        id: str = None,
        model: str = None,
        object: str = None,
        request_id: str = None,
        system_fingerprint: str = None,
        usage: str = None,
    ):
        # List of model generation results
        self.choices = choices
        # Timestamp of session creation
        self.created = created
        # Streaming response error information content
        self.error = error
        # Unique ID for this session
        self.id = id
        # Model identifier
        self.model = model
        # Response type
        self.object = object
        # Unique request ID
        self.request_id = request_id
        # System fingerprint
        self.system_fingerprint = system_fingerprint
        # Token usage
        self.usage = usage

    def validate(self):
        if self.choices:
            for v1 in self.choices:
                 if v1:
                    v1.validate()
        if self.error:
            self.error.validate()

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

        if self.error is not None:
            result['Error'] = self.error.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.model is not None:
            result['Model'] = self.model

        if self.object is not None:
            result['Object'] = self.object

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_fingerprint is not None:
            result['SystemFingerprint'] = self.system_fingerprint

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('Choices') is not None:
            for k1 in m.get('Choices'):
                temp_model = main_models.LlmStreamChatResponseBodyChoices()
                self.choices.append(temp_model.from_map(k1))

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Error') is not None:
            temp_model = main_models.LlmStreamChatResponseBodyError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemFingerprint') is not None:
            self.system_fingerprint = m.get('SystemFingerprint')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class LlmStreamChatResponseBodyError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        param: str = None,
        type: str = None,
    ):
        # Error code
        self.code = code
        # Error message
        self.message = message
        # Parameter that caused the error
        self.param = param
        # Error type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.param is not None:
            result['Param'] = self.param

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class LlmStreamChatResponseBodyChoices(DaraModel):
    def __init__(
        self,
        delta: main_models.LlmStreamChatResponseBodyChoicesDelta = None,
        finish_reason: str = None,
        index: int = None,
        logprobs: str = None,
    ):
        # Incremental content object
        self.delta = delta
        # For streaming output, it is null while generating and becomes \\"stop\\" if the generation ends due to a stop token.
        self.finish_reason = finish_reason
        # Stream sequence number
        self.index = index
        # Token probability information
        self.logprobs = logprobs

    def validate(self):
        if self.delta:
            self.delta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delta is not None:
            result['Delta'] = self.delta.to_map()

        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason

        if self.index is not None:
            result['Index'] = self.index

        if self.logprobs is not None:
            result['Logprobs'] = self.logprobs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delta') is not None:
            temp_model = main_models.LlmStreamChatResponseBodyChoicesDelta()
            self.delta = temp_model.from_map(m.get('Delta'))

        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Logprobs') is not None:
            self.logprobs = m.get('Logprobs')

        return self

class LlmStreamChatResponseBodyChoicesDelta(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # Real-time generated text content
        self.content = content
        # Role identifier
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

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

