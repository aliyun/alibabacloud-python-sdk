# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocUpdateContentShrinkRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        data_type: str = None,
        doc_key: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.data_type = data_type
        # This parameter is required.
        self.doc_key = doc_key
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.doc_key is not None:
            result['DocKey'] = self.doc_key

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

