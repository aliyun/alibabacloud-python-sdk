# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBizEntityRequest(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        id: int = None,
        op_tenant_id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.biz_unit_id = biz_unit_id
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.id is not None:
            result['Id'] = self.id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

