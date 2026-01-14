# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InteractTextRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        content: str = None,
        session_id: str = None,
    ):
        self.agent_id = agent_id
        self.content = content
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.content is not None:
            result['content'] = self.content

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

