# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRoleRequest(DaraModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        # The name of the RAM role.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, periods (.), and hyphens (-).
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

