# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSkillGroupRequest(DaraModel):
    def __init__(
        self,
        channel_type: int = None,
        client_token: str = None,
        department_id: int = None,
        description: str = None,
        display_name: str = None,
        instance_id: str = None,
        skill_group_name: str = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        self.client_token = client_token
        self.department_id = department_id
        self.description = description
        self.display_name = display_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.skill_group_name = skill_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        return self

