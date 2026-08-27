# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSourceContentRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        force_sync: bool = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # The returned content.
        # 
        # This parameter is required.
        self.content = content
        # Specifies whether to force synchronous processing.
        self.force_sync = force_sync
        # The ID of the data source.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The ID of the effective tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.force_sync is not None:
            result['forceSync'] = self.force_sync

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('forceSync') is not None:
            self.force_sync = m.get('forceSync')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

