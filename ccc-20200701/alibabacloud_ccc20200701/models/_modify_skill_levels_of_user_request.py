# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySkillLevelsOfUserRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        skill_level_list: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.skill_level_list = skill_level_list
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.skill_level_list is not None:
            result['SkillLevelList'] = self.skill_level_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillLevelList') is not None:
            self.skill_level_list = m.get('SkillLevelList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

