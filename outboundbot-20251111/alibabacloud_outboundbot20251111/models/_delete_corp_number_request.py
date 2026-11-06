# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCorpNumberRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        number: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to force delete an existing number.
        self.force = force
        # The outbound number.
        # 
        # This parameter is required.
        self.number = number
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.number is not None:
            result['Number'] = self.number

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

