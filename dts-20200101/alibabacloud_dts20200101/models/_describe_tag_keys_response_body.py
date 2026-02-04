# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        category: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_keys: List[str] = None,
        total_count: int = None,
    ):
        # The type of the tag.
        self.category = category
        # The start page of the returned pages.
        self.page_number = page_number
        # The number of tags returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The key of the tag.
        self.tag_keys = tag_keys
        # The total number of returned tag keys.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

