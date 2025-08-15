# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRoleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        role_principal: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.role_principal = role_principal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')

        return self

