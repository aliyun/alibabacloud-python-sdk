# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolarClawAgentSkillsShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        skills_shrink: str = None,
    ):
        # Agent ID
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The skill allowlist. A value of null indicates that all skills are allowed.
        self.skills_shrink = skills_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.skills_shrink is not None:
            result['Skills'] = self.skills_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Skills') is not None:
            self.skills_shrink = m.get('Skills')

        return self

