# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchPbcAssetsRequest(DaraModel):
    def __init__(
        self,
        industry: str = None,
        keyword: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.industry = industry
        self.keyword = keyword
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.industry is not None:
            result['industry'] = self.industry

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.order_by is not None:
            result['order_by'] = self.order_by

        if self.order_direction is not None:
            result['order_direction'] = self.order_direction

        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

