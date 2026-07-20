# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRbacRoleRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        role_id: str = None,
    ):
        # The business ID of the application instance.
        self.biz_id = biz_id
        # The role ID.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

