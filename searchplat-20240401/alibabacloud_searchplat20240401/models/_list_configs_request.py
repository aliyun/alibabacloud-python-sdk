# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConfigsRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        page: int = None,
        page_size: int = None,
    ):
        # The field-level equality filter condition. The value is a URL-encoded JSON string (which decodes to a {"fieldName": value} object). Multiple fields have an AND relationship, meaning all conditions must be met for a result to be returned.
        self.filter = filter
        # page
        self.page = page
        # pageSize
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

