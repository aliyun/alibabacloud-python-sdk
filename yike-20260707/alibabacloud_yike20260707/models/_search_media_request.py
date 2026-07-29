# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMediaRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        match: str = None,
        page_no: int = None,
        page_size: int = None,
        scroll_token: str = None,
        sort_by: str = None,
    ):
        self.category_id = category_id
        self.match = match
        self.page_no = page_no
        self.page_size = page_size
        self.scroll_token = scroll_token
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.match is not None:
            result['Match'] = self.match

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Match') is not None:
            self.match = m.get('Match')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

