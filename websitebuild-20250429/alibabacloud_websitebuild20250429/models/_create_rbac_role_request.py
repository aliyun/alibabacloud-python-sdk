# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRbacRoleRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        role_data: str = None,
    ):
        self.biz_id = biz_id
        self.role_data = role_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.role_data is not None:
            result['RoleData'] = self.role_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('RoleData') is not None:
            self.role_data = m.get('RoleData')

        return self

