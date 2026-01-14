# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocumentInfo(DaraModel):
    def __init__(
        self,
        document_type: str = None,
        id: str = None,
        name: str = None,
        process_status: str = None,
    ):
        self.document_type = document_type
        self.id = id
        self.name = name
        self.process_status = process_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_type is not None:
            result['documentType'] = self.document_type

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.process_status is not None:
            result['processStatus'] = self.process_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('processStatus') is not None:
            self.process_status = m.get('processStatus')

        return self

