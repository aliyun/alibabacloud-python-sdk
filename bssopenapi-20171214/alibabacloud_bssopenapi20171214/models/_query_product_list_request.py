# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryProductListRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        query_total_count: bool = None,
    ):
        # The page number of the page to return.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # Specifies whether to return the total number of services. Default value: false.
        self.query_total_count = query_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_total_count is not None:
            result['QueryTotalCount'] = self.query_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryTotalCount') is not None:
            self.query_total_count = m.get('QueryTotalCount')

        return self

