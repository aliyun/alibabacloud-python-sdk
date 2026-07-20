# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRbacPermissionRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        permission_id: str = None,
    ):
        self.biz_id = biz_id
        self.permission_id = permission_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.permission_id is not None:
            result['PermissionId'] = self.permission_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('PermissionId') is not None:
            self.permission_id = m.get('PermissionId')

        return self

