# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRowPermissionByTableGuidsShrinkRequest(DaraModel):
    def __init__(
        self,
        get_row_permission_by_table_guids_query_shrink: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The request command.
        # 
        # This parameter is required.
        self.get_row_permission_by_table_guids_query_shrink = get_row_permission_by_table_guids_query_shrink
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_row_permission_by_table_guids_query_shrink is not None:
            result['GetRowPermissionByTableGuidsQuery'] = self.get_row_permission_by_table_guids_query_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetRowPermissionByTableGuidsQuery') is not None:
            self.get_row_permission_by_table_guids_query_shrink = m.get('GetRowPermissionByTableGuidsQuery')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

