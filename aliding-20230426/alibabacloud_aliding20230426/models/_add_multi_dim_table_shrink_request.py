# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMultiDimTableShrinkRequest(DaraModel):
    def __init__(
        self,
        base_id: str = None,
        fields_shrink: str = None,
        name: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.base_id = base_id
        self.fields_shrink = fields_shrink
        self.name = name
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_id is not None:
            result['BaseId'] = self.base_id

        if self.fields_shrink is not None:
            result['Fields'] = self.fields_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        if m.get('Fields') is not None:
            self.fields_shrink = m.get('Fields')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

