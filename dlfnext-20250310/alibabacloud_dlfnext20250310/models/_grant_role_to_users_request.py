# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GrantRoleToUsersRequest(DaraModel):
    def __init__(
        self,
        role_principal: str = None,
        user_principals: List[str] = None,
    ):
        self.role_principal = role_principal
        self.user_principals = user_principals

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal

        if self.user_principals is not None:
            result['userPrincipals'] = self.user_principals

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')

        if m.get('userPrincipals') is not None:
            self.user_principals = m.get('userPrincipals')

        return self

