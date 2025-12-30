# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDocumentRequest(DaraModel):
    def __init__(
        self,
        doc_ids: List[str] = None,
        library_id: str = None,
    ):
        # This parameter is required.
        self.doc_ids = doc_ids
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_ids is not None:
            result['docIds'] = self.doc_ids

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docIds') is not None:
            self.doc_ids = m.get('docIds')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        return self

