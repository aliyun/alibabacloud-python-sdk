# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateThirdSsoAgentRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        client_id: str = None,
        client_token: str = None,
        display_name: str = None,
        instance_id: str = None,
        role_ids: List[int] = None,
        skill_group_ids: List[int] = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.client_id = client_id
        self.client_token = client_token
        self.display_name = display_name
        # This parameter is required.
        self.instance_id = instance_id
        self.role_ids = role_ids
        self.skill_group_ids = skill_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.skill_group_ids is not None:
            result['SkillGroupIds'] = self.skill_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('SkillGroupIds') is not None:
            self.skill_group_ids = m.get('SkillGroupIds')

        return self

