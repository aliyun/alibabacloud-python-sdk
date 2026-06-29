# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SingleTenant(DaraModel):
    def __init__(
        self,
        description: str = None,
        status: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        uuid: str = None,
    ):
        # Tenant description
        self.description = description
        # Tenant status
        self.status = status
        # Tenant ID
        self.tenant_id = tenant_id
        # Tenant name
        self.tenant_name = tenant_name
        # Tenant UUID
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.uuid is not None:
            result['UUID'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        return self

