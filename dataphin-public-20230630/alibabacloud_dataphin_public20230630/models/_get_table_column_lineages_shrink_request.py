# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableColumnLineagesShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_query_shrink: str = None,
        op_tenant_id: int = None,
        table_guid: str = None,
    ):
        self.filter_query_shrink = filter_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_query_shrink is not None:
            result['FilterQuery'] = self.filter_query_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterQuery') is not None:
            self.filter_query_shrink = m.get('FilterQuery')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

