# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRoleRequest(DaraModel):
    def __init__(
        self,
        role_id: int = None,
    ):
        # The ID of the RAM role.
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

