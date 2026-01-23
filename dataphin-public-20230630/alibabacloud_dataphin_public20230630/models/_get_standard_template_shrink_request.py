# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStandardTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_query_shrink: str = None,
        id: int = None,
        nullable: bool = None,
        op_tenant_id: int = None,
    ):
        self.filter_query_shrink = filter_query_shrink
        # This parameter is required.
        self.id = id
        self.nullable = nullable
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_query_shrink is not None:
            result['FilterQuery'] = self.filter_query_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterQuery') is not None:
            self.filter_query_shrink = m.get('FilterQuery')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

