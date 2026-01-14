# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIndexDocumentShrinkRequest(DaraModel):
    def __init__(
        self,
        document_ids_shrink: str = None,
        index_id: str = None,
    ):
        # The list of the primary key IDs of the documents.
        # 
        # This parameter is required.
        self.document_ids_shrink = document_ids_shrink
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        return self

