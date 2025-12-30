# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLibraryListRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        query: str = None,
    ):
        self.page = page
        self.page_size = page_size
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

