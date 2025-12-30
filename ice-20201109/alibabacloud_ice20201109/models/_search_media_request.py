# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMediaRequest(DaraModel):
    def __init__(
        self,
        custom_filters: str = None,
        entity_id: str = None,
        match: str = None,
        page_no: int = None,
        page_size: int = None,
        scroll_token: str = None,
        search_lib_name: str = None,
        sort_by: str = None,
    ):
        self.custom_filters = custom_filters
        # The ID of the entity.
        self.entity_id = entity_id
        # The filter conditions. For more information about the parameter syntax
        # <props="china">, see [Media asset search protocols](https://help.aliyun.com/document_detail/2584256.html).
        self.match = match
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The pagination identifier. The value can be up to 32 characters in length. The first time you call this operation for each new search, you do not need to specify this parameter. The value of this parameter is returned each time data records that meet the specified filter condition are found. The value is used to record the current position of queried data. Record the returned parameter value and set this parameter according to the following requirements during the next search: If you need to traverse all data that meets the filter criteria, you must set the ScrollToken parameter. If the value of the PageNo parameter exceeds 200, we recommend that you set this parameter to optimize search performance. You can only page backward. You can page a maximum of 1,000 entries in an operation.
        self.scroll_token = scroll_token
        # The search library.
        self.search_lib_name = search_lib_name
        # The sort field and order. Separate multiple parameters with commas (,).
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.match is not None:
            result['Match'] = self.match

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('Match') is not None:
            self.match = m.get('Match')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

