# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveAgentFromSkillGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_ids_shrink: str = None,
        instance_id: str = None,
        skill_group_id: int = None,
    ):
        # This parameter is required.
        self.agent_ids_shrink = agent_ids_shrink
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

