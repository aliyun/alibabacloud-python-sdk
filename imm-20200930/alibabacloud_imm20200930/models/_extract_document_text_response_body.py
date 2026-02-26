# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExtractDocumentTextResponseBody(DaraModel):
    def __init__(
        self,
        document_text: str = None,
        request_id: str = None,
    ):
        # The text content of the document.
        self.document_text = document_text
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_text is not None:
            result['DocumentText'] = self.document_text

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentText') is not None:
            self.document_text = m.get('DocumentText')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

