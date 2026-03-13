# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetDocumentRankRequest(DaraModel):
    def __init__(
        self,
        docs: List[str] = None,
        query: str = None,
    ):
        # This parameter is required.
        self.docs = docs
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.docs is not None:
            result['docs'] = self.docs

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docs') is not None:
            self.docs = m.get('docs')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

