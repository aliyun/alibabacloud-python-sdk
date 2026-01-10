# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PaginationInfo(DaraModel):
    def __init__(
        self,
        limit: int = None,
        page: int = None,
        total: int = None,
        total_pages: int = None,
    ):
        self.limit = limit
        self.page = page
        self.total = total
        self.total_pages = total_pages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.page is not None:
            result['page'] = self.page

        if self.total is not None:
            result['total'] = self.total

        if self.total_pages is not None:
            result['totalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        return self

