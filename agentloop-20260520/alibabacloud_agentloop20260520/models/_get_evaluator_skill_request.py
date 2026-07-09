# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEvaluatorSkillRequest(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        version: str = None,
    ):
        # The AgentSpace name.
        # 
        # This parameter is required.
        self.agent_space = agent_space
        # The skill version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

