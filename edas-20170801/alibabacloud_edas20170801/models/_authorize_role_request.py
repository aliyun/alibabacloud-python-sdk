# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeRoleRequest(DaraModel):
    def __init__(
        self,
        role_ids: str = None,
        target_user_id: str = None,
    ):
        # The ID of the role to be assigned. If you want to assign multiple roles to the specified RAM user, separate the IDs of the roles with semicolons (;). If you leave this parameter empty, the roles assigned to the specified RAM user are revoked.
        # 
        # This parameter is required.
        self.role_ids = role_ids
        # The ID of the RAM user to which you want to assign the roles.
        # 
        # This parameter is required.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

