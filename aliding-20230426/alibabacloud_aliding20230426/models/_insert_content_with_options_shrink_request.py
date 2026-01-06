# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertContentWithOptionsShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        document_id: str = None,
        index: int = None,
        path_shrink: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.content_shrink = content_shrink
        # This parameter is required.
        self.document_id = document_id
        self.index = index
        self.path_shrink = path_shrink
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.index is not None:
            result['Index'] = self.index

        if self.path_shrink is not None:
            result['Path'] = self.path_shrink

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Path') is not None:
            self.path_shrink = m.get('Path')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

