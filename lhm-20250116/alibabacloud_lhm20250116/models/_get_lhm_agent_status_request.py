# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLhmAgentStatusRequest(DaraModel):
    def __init__(
        self,
        agent_type: int = None,
        skill_name: str = None,
    ):
        # The Agent type. Valid values:
        # - 0: data validation (the only type currently supported).
        # - 1: metadata.
        # 
        # This parameter is required.
        self.agent_type = agent_type
        # The skill name. This parameter is optional.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['agentType'] = self.agent_type

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentType') is not None:
            self.agent_type = m.get('agentType')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        return self

