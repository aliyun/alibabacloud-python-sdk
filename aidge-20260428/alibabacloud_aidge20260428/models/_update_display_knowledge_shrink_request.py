# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDisplayKnowledgeShrinkRequest(DaraModel):
    def __init__(
        self,
        rag_id: str = None,
        records_shrink: str = None,
    ):
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.rag_id = rag_id
        # The records to update. A maximum of 500 records can be specified.
        # 
        # This parameter is required.
        self.records_shrink = records_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        if self.records_shrink is not None:
            result['Records'] = self.records_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        if m.get('Records') is not None:
            self.records_shrink = m.get('Records')

        return self

