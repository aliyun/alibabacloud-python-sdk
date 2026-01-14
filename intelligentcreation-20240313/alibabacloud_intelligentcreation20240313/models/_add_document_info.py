# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDocumentInfo(DaraModel):
    def __init__(
        self,
        document_type: str = None,
        name: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.document_type = document_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_type is not None:
            result['documentType'] = self.document_type

        if self.name is not None:
            result['name'] = self.name

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

