# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveRbacRoleHierarchyRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        child_role_id: str = None,
        parent_role_id: str = None,
    ):
        self.biz_id = biz_id
        self.child_role_id = child_role_id
        self.parent_role_id = parent_role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.child_role_id is not None:
            result['ChildRoleId'] = self.child_role_id

        if self.parent_role_id is not None:
            result['ParentRoleId'] = self.parent_role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ChildRoleId') is not None:
            self.child_role_id = m.get('ChildRoleId')

        if m.get('ParentRoleId') is not None:
            self.parent_role_id = m.get('ParentRoleId')

        return self

