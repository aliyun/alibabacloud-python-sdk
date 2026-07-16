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
        # The custom filter, specified as a JSON string. Supports the integer field intField1 and the string fields strField1 and strField2. Use only one match type per field. Conditions on different fields are combined with a logical AND.
        # 
        # - Exact match: `{"intField1":12,"strField1":"abc"}`
        # 
        # - Multi-value match: `{"intField1":[12,13],"strField1":["abc","cd"]}`
        # 
        # - Range match: `{"intField1":{"gte":12,"lte":13}}`
        self.custom_filters = custom_filters
        # The entity ID.
        self.entity_id = entity_id
        # The filter condition for the search. <props="china">For syntax rules, see the [Media Search Protocol](https://help.aliyun.com/document_detail/2584256.html).
        self.match = match
        # The page number to return. The default value is 1.
        self.page_no = page_no
        # The number of results per page. The default value is 10, and the maximum value is 50.
        self.page_size = page_size
        # The scroll token for deep pagination. It is a 32-character string. This parameter is not required for the first search request. If a search is successful, the response includes a `ScrollToken` to mark the current position. Use this token in subsequent requests to retrieve the next page of results. This parameter is required to iterate through all matching results. For optimal performance, use this parameter when the `PageNo` value exceeds 200. You can scroll only forward, up to a maximum of 1,000 media assets.
        self.scroll_token = scroll_token
        # The name of the search library.
        self.search_lib_name = search_lib_name
        # The sort field and sort order. Separate multiple sort criteria with a comma (,).
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

