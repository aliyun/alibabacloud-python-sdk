# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserLevelsOfSkillGroupRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        skill_group_id: str = None,
        user_level_list: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.skill_group_id = skill_group_id
        # This parameter is required.
        self.user_level_list = user_level_list

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

        if self.user_level_list is not None:
            result['UserLevelList'] = self.user_level_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('UserLevelList') is not None:
            self.user_level_list = m.get('UserLevelList')

        return self

