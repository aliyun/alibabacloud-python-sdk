# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateDocumentRequest(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        library_id: str = None,
        meta: Dict[str, Any] = None,
        title: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.library_id = library_id
        self.meta = meta
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.meta is not None:
            result['meta'] = self.meta

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('meta') is not None:
            self.meta = m.get('meta')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

