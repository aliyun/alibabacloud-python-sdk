# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssignUsersRequest(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        instance_id: str = None,
        ram_id_list: str = None,
        role_id: str = None,
        skill_level_list: str = None,
        work_mode: str = None,
    ):
        self.async_ = async_
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # A JSON array of RAM user IDs to import, formatted as a string.
        # 
        # This parameter is required.
        self.ram_id_list = ram_id_list
        # The ID of the role to assign to the users in the instance. After the RAM users are imported, they are assigned this role. Valid roles are Administrator, Teamleader, and Agent.
        # 
        # This parameter is required.
        self.role_id = role_id
        # A JSON array of skill objects, provided as a string. Each object specifies a skillGroupId and a skillLevel from 1 to 10. A lower skillLevel value indicates higher proficiency and greater call-handling capacity.
        self.skill_level_list = skill_level_list
        # The work mode for the agents.
        # 
        # This parameter is required.
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ram_id_list is not None:
            result['RamIdList'] = self.ram_id_list

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.skill_level_list is not None:
            result['SkillLevelList'] = self.skill_level_list

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RamIdList') is not None:
            self.ram_id_list = m.get('RamIdList')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('SkillLevelList') is not None:
            self.skill_level_list = m.get('SkillLevelList')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

