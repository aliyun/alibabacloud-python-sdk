# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAbacPoliciesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        tid: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The search keyword. Fuzzy match is supported.
        self.search_key = search_key
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

