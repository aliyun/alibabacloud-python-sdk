# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteAgentRequest(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
        stream: bool = None,
    ):
        # The ID of the business workspace.
        self.base_me_agent_id = base_me_agent_id
        # The complete JSON string. For more information, see the following detailed description.
        self.json_str = json_str
        # Specifies whether to enable Server-Sent Events (SSE) responses. Set to true to enable SSE responses. Default value: false.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id

        if self.json_str is not None:
            result['JsonStr'] = self.json_str

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

