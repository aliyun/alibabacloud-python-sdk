# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryLiveWatchUserListShrinkRequest(DaraModel):
    def __init__(
        self,
        live_id: str = None,
        page_number: int = None,
        page_size: int = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.live_id = live_id
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_id is not None:
            result['LiveId'] = self.live_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

