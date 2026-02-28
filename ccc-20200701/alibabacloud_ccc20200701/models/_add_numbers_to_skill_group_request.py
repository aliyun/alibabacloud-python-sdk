# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddNumbersToSkillGroupRequest(DaraModel):
    def __init__(
        self,
        inst_number_group_id_list: str = None,
        instance_id: str = None,
        number_list: str = None,
        skill_group_id: str = None,
    ):
        self.inst_number_group_id_list = inst_number_group_id_list
        # This parameter is required.
        self.instance_id = instance_id
        self.number_list = number_list
        # This parameter is required.
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inst_number_group_id_list is not None:
            result['InstNumberGroupIdList'] = self.inst_number_group_id_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstNumberGroupIdList') is not None:
            self.inst_number_group_id_list = m.get('InstNumberGroupIdList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

