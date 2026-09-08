# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUsersToSkillGroupRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        skill_group_id: str = None,
        user_skill_level_list: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Skill group ID.
        # 
        # This parameter is required.
        self.skill_group_id = skill_group_id
        # A list of agent skill levels in the skill group, formatted as a JSON array string. Each array element is an object containing two fields: userId and skillLevel. The userId field specifies the ID of the agent to be added, and the skillLevel field specifies the agent\\"s skill level after joining the skill group. Skill levels range from 1 to 10; a lower value indicates stronger service capability and the ability to handle more calls per unit time.
        # 
        # This parameter is required.
        self.user_skill_level_list = user_skill_level_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.user_skill_level_list is not None:
            result['UserSkillLevelList'] = self.user_skill_level_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('UserSkillLevelList') is not None:
            self.user_skill_level_list = m.get('UserSkillLevelList')

        return self

