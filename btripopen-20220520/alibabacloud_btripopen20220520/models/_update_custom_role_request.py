# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomRoleRequest(DaraModel):
    def __init__(
        self,
        role_id: str = None,
        role_name: str = None,
    ):
        # This parameter is required.
        self.role_id = role_id
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_id is not None:
            result['role_id'] = self.role_id

        if self.role_name is not None:
            result['role_name'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        if m.get('role_name') is not None:
            self.role_name = m.get('role_name')

        return self

