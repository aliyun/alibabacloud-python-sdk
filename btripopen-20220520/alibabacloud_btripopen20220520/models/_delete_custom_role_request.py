# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCustomRoleRequest(DaraModel):
    def __init__(
        self,
        role_id: str = None,
    ):
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
            result['role_id'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        return self

