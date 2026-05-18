# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDocumentRequest(DaraModel):
    def __init__(
        self,
        document_name: str = None,
        kb_uuid: str = None,
    ):
        # This parameter is required.
        self.document_name = document_name
        # This parameter is required.
        self.kb_uuid = kb_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_name is not None:
            result['DocumentName'] = self.document_name

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        return self

