# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class RunCompletionMessageRequest(DaraModel):
    def __init__(
        self,
        messages: List[main_models.RunCompletionMessageRequestMessages] = None,
        model_code: str = None,
        stream: bool = None,
        response_format_type: str = None,
    ):
        # This parameter is required.
        self.messages = messages
        self.model_code = model_code
        self.stream = stream
        self.response_format_type = response_format_type

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

        if self.response_format_type is not None:
            result['responseFormatType'] = self.response_format_type

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

        if m.get('responseFormatType') is not None:
            self.response_format_type = m.get('responseFormatType')

        return self

class RunCompletionMessageRequestMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
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

