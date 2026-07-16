# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class RunCompletionMessageRequest(DaraModel):
    def __init__(
        self,
        messages: List[main_models.RunCompletionMessageRequestMessages] = None,
        model_code: str = None,
        stream: bool = None,
    ):
        # A list of messages that form the conversation history and the current prompt.
        self.messages = messages
        # The model specification to use. Valid values: `TYXM_PLUS` and `TYXM_TURBO`.
        self.model_code = model_code
        # Specifies whether to stream the response using Server-Sent Events (SSE). If `true`, the response is streamed. Defaults to `false`.
        self.stream = stream

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.RunCompletionMessageRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

class RunCompletionMessageRequestMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # The content of the message.
        self.content = content
        # The role of the message sender. Valid values: `user`, `agent`, `system`, and `function`.
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

