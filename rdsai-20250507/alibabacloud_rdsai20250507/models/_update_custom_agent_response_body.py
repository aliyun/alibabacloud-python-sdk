# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateCustomAgentResponseBody(DaraModel):
    def __init__(
        self,
        enable_tools: str = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        system_prompt: str = None,
        tools: List[str] = None,
    ):
        self.enable_tools = enable_tools
        # AgentId。
        self.id = id
        self.name = name
        self.request_id = request_id
        self.system_prompt = system_prompt
        self.tools = tools

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.tools is not None:
            result['Tools'] = self.tools

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('Tools') is not None:
            self.tools = m.get('Tools')

        return self

