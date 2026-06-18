# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentBySkillGroupIdRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        skill_group_id: int = None,
    ):
        # A unique ID for the Customer request. It is used for idempotency validation and can be generated using a UUID.
        self.client_token = client_token
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The skill group ID.  
        # You can invoke the [QuerySkillGroups](https://help.aliyun.com/zh/aiccs/developer-reference/api-aiccs-2019-10-15-queryskillgroups) API and view the **SkillGroupId** in the response parameters to obtain the skill group ID.
        # 
        # This parameter is required.
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

