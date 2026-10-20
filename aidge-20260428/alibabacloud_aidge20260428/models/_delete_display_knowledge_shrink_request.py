# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDisplayKnowledgeShrinkRequest(DaraModel):
    def __init__(
        self,
        rag_id: str = None,
        record_ids_shrink: str = None,
    ):
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.rag_id = rag_id
        # The IDs of the records to delete. You can specify up to 500 record IDs.
        # 
        # This parameter is required.
        self.record_ids_shrink = record_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        if self.record_ids_shrink is not None:
            result['RecordIds'] = self.record_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        if m.get('RecordIds') is not None:
            self.record_ids_shrink = m.get('RecordIds')

        return self

