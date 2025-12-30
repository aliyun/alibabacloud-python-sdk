# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBizEntityInfoByVersionRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        op_tenant_id: int = None,
        type: str = None,
        version_id: int = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

