# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        enable_tools: bool = None,
        name: str = None,
        system_prompt: str = None,
        tools_shrink: str = None,
    ):
        # AgentId。
        # 
        # This parameter is required.
        self.custom_agent_id = custom_agent_id
        self.enable_tools = enable_tools
        self.name = name
        self.system_prompt = system_prompt
        self.tools_shrink = tools_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools

        if self.name is not None:
            result['Name'] = self.name

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.tools_shrink is not None:
            result['Tools'] = self.tools_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('Tools') is not None:
            self.tools_shrink = m.get('Tools')

        return self

