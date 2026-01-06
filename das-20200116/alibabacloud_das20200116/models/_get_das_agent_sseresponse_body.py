# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetDasAgentSSEResponseBody(DaraModel):
    def __init__(
        self,
        answer: str = None,
        event: str = None,
        id: str = None,
        metadata: main_models.GetDasAgentSSEResponseBodyMetadata = None,
    ):
        self.answer = answer
        self.event = event
        self.id = id
        self.metadata = metadata

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.event is not None:
            result['Event'] = self.event

        if self.id is not None:
            result['Id'] = self.id

        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Metadata') is not None:
            temp_model = main_models.GetDasAgentSSEResponseBodyMetadata()
            self.metadata = temp_model.from_map(m.get('Metadata'))

        return self

class GetDasAgentSSEResponseBodyMetadata(DaraModel):
    def __init__(
        self,
        char_count: int = None,
        code: int = None,
        request_id: str = None,
        tool_name: str = None,
        tool_params: List[str] = None,
    ):
        self.char_count = char_count
        self.code = code
        self.request_id = request_id
        self.tool_name = tool_name
        self.tool_params = tool_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.char_count is not None:
            result['CharCount'] = self.char_count

        if self.code is not None:
            result['Code'] = self.code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        if self.tool_params is not None:
            result['ToolParams'] = self.tool_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharCount') is not None:
            self.char_count = m.get('CharCount')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        if m.get('ToolParams') is not None:
            self.tool_params = m.get('ToolParams')

        return self

