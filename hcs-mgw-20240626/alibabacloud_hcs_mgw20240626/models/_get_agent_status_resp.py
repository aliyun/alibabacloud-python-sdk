# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentStatusResp(DaraModel):
    def __init__(
        self,
        agent_ip: str = None,
        agent_version: str = None,
        status: str = None,
    ):
        self.agent_ip = agent_ip
        self.agent_version = agent_version
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ip is not None:
            result['AgentIP'] = self.agent_ip

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIP') is not None:
            self.agent_ip = m.get('AgentIP')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

