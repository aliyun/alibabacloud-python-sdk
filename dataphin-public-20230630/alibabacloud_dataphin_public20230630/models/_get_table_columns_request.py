# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableColumnsRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        op_tenant_id: int = None,
        table_name: str = None,
    ):
        # This parameter is required.
        self.catalog = catalog
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

