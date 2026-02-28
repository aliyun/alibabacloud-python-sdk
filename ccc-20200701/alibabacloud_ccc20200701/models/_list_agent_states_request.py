# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentStatesRequest(DaraModel):
    def __init__(
        self,
        agent_ids: str = None,
        exclude_offline_users: bool = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_group_id: str = None,
        state: str = None,
    ):
        self.agent_ids = agent_ids
        self.exclude_offline_users = exclude_offline_users
        # This parameter is required.
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.skill_group_id = skill_group_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.exclude_offline_users is not None:
            result['ExcludeOfflineUsers'] = self.exclude_offline_users

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('ExcludeOfflineUsers') is not None:
            self.exclude_offline_users = m.get('ExcludeOfflineUsers')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

