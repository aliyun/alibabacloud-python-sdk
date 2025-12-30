# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDocumentUrlRequest(DaraModel):
    def __init__(
        self,
        document_id: str = None,
    ):
        # This parameter is required.
        self.document_id = document_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_id is not None:
            result['documentId'] = self.document_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')

        return self

