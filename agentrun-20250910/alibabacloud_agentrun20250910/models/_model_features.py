# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelFeatures(DaraModel):
    def __init__(
        self,
        agent_thought: bool = None,
        multi_tool_call: bool = None,
        stream_tool_call: bool = None,
        tool_call: bool = None,
        vision: bool = None,
    ):
        self.agent_thought = agent_thought
        self.multi_tool_call = multi_tool_call
        self.stream_tool_call = stream_tool_call
        self.tool_call = tool_call
        self.vision = vision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_thought is not None:
            result['agentThought'] = self.agent_thought

        if self.multi_tool_call is not None:
            result['multiToolCall'] = self.multi_tool_call

        if self.stream_tool_call is not None:
            result['streamToolCall'] = self.stream_tool_call

        if self.tool_call is not None:
            result['toolCall'] = self.tool_call

        if self.vision is not None:
            result['vision'] = self.vision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentThought') is not None:
            self.agent_thought = m.get('agentThought')

        if m.get('multiToolCall') is not None:
            self.multi_tool_call = m.get('multiToolCall')

        if m.get('streamToolCall') is not None:
            self.stream_tool_call = m.get('streamToolCall')

        if m.get('toolCall') is not None:
            self.tool_call = m.get('toolCall')

        if m.get('vision') is not None:
            self.vision = m.get('vision')

        return self

