# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        agent_type: str = None,
        description: str = None,
        expire_after_seconds: int = None,
    ):
        # This parameter is required.
        self.agent_name = agent_name
        self.agent_type = agent_type
        self.description = description
        self.expire_after_seconds = expire_after_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_after_seconds is not None:
            result['ExpireAfterSeconds'] = self.expire_after_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireAfterSeconds') is not None:
            self.expire_after_seconds = m.get('ExpireAfterSeconds')

        return self

