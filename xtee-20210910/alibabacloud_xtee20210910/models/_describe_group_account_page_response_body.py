# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupAccountPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        data: bool = None,
        page_size: int = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Returned data object.
        self.data = data
        # Page size, default value is 10.
        self.page_size = page_size
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.data is not None:
            result['data'] = self.data

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

