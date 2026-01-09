# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAgentRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        client_token: str = None,
        display_name: str = None,
        instance_id: str = None,
        skill_group_id: List[int] = None,
        skill_group_id_list: List[int] = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        self.client_token = client_token
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.instance_id = instance_id
        self.skill_group_id = skill_group_id
        self.skill_group_id_list = skill_group_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')

        return self

