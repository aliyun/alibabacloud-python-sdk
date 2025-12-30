# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParseResultRequest(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        library_id: str = None,
        use_url_result: bool = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.library_id = library_id
        self.use_url_result = use_url_result

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

        if self.use_url_result is not None:
            result['useUrlResult'] = self.use_url_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('useUrlResult') is not None:
            self.use_url_result = m.get('useUrlResult')

        return self

