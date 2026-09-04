# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class QueryPrimaryObjectDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[Dict[str, str]] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The business status code. A value of 200 indicates success. A failure returns a backend error code (ERR.* / InvalidParameter.*).
        self.code = code
        # The incremental information list.
        self.items = items
        # The error description. This parameter is empty when the request succeeds.
        self.message = message
        # The current page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The request trace ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.items is not None:
            result['items'] = self.items

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('items') is not None:
            self.items = m.get('items')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

