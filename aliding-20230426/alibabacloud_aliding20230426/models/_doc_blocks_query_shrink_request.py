# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocBlocksQueryShrinkRequest(DaraModel):
    def __init__(
        self,
        block_type: str = None,
        doc_key: str = None,
        end_index: int = None,
        start_index: int = None,
        tenant_context_shrink: str = None,
    ):
        self.block_type = block_type
        # This parameter is required.
        self.doc_key = doc_key
        self.end_index = end_index
        self.start_index = start_index
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.doc_key is not None:
            result['DocKey'] = self.doc_key

        if self.end_index is not None:
            result['EndIndex'] = self.end_index

        if self.start_index is not None:
            result['StartIndex'] = self.start_index

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')

        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')

        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

