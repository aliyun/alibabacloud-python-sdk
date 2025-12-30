# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRowPermissionByUserIdShrinkRequest(DaraModel):
    def __init__(
        self,
        list_row_permission_by_user_id_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_row_permission_by_user_id_query_shrink = list_row_permission_by_user_id_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_row_permission_by_user_id_query_shrink is not None:
            result['ListRowPermissionByUserIdQuery'] = self.list_row_permission_by_user_id_query_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListRowPermissionByUserIdQuery') is not None:
            self.list_row_permission_by_user_id_query_shrink = m.get('ListRowPermissionByUserIdQuery')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

