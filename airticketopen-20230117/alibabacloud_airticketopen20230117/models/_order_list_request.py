# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OrderListRequest(DaraModel):
    def __init__(
        self,
        book_time_end: int = None,
        book_time_start: int = None,
        page_index: int = None,
        page_size: int = None,
        status: int = None,
    ):
        # The query end time. The value is a 13-digit UNIX timestamp.
        # 
        # This parameter is required.
        self.book_time_end = book_time_end
        # The query start time. The value is a 13-digit UNIX timestamp.
        # 
        # This parameter is required.
        self.book_time_start = book_time_start
        # The page index. The value starts from 1.
        self.page_index = page_index
        # The page size.
        self.page_size = page_size
        # The order status. Valid values:
        # - 2: order creation succeeded.
        # - 3: order paid.
        # - 4: order succeeded.
        # - 5: order closed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.book_time_end is not None:
            result['book_time_end'] = self.book_time_end

        if self.book_time_start is not None:
            result['book_time_start'] = self.book_time_start

        if self.page_index is not None:
            result['page_index'] = self.page_index

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('book_time_end') is not None:
            self.book_time_end = m.get('book_time_end')

        if m.get('book_time_start') is not None:
            self.book_time_start = m.get('book_time_start')

        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

