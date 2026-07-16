# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSkillGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        display_name: str = None,
        instance_id: str = None,
        skill_group_id: int = None,
        skill_group_name: str = None,
    ):
        # Unique ID of the customer request. Used for idempotency validation. You can generate it by using a UUID.
        self.client_token = client_token
        # Skill group description.  
        # > This parameter can be updated.
        self.description = description
        # Display name of the skill group.  
        # > This parameter can be updated.
        self.display_name = display_name
        # AICCS instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Skill group ID.  
        # 
        # You can invoke the [QuerySkillGroups](https://help.aliyun.com/zh/aiccs/developer-reference/api-aiccs-2019-10-15-queryskillgroups) API and check the **SkillGroupId** field in the response to obtain the skill group ID.  
        # 
        # > This parameter cannot be updated.
        # 
        # This parameter is required.
        self.skill_group_id = skill_group_id
        # Skill group name.  
        # > This parameter cannot be updated.
        self.skill_group_name = skill_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        return self

