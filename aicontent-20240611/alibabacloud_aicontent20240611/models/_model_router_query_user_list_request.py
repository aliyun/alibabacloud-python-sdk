# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryUserListRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_index: int = None,
        page_size: int = None,
        phone: str = None,
    ):
        # The search keyword.
        self.keyword = keyword
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # Specifies the phone number for exact matching (not fuzzy). When specified together with keyword, the two conditions are combined with AND, meaning both must be satisfied. If not specified, no filtering by phone number is applied.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

