# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMediaRequest(DaraModel):
    def __init__(
        self,
        fields: str = None,
        match: str = None,
        page_no: int = None,
        page_size: int = None,
        scroll_token: str = None,
        search_type: str = None,
        sort_by: str = None,
    ):
        # The media asset fields to return in the search results.
        # 
        # By default, only basic media asset fields are returned. You can specify additional media asset fields to return. For more information, see [Usage examples](https://help.aliyun.com/document_detail/99179.html).
        self.fields = fields
        # The filter conditions. For syntax rules, see [Search protocol syntax](https://help.aliyun.com/document_detail/86991.html).
        self.match = match
        # The page number. Default value: **1**.
        # 
        # > If this parameter exceeds **200**, set the ScrollToken parameter as well.
        self.page_no = page_no
        # The number of records per page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The pagination token. The value is a 32-character string.
        # You do not need to set this parameter for the first search request. When the search request matches data, the server returns this parameter value, which records the current position of the search data. Record the returned value and set this parameter in the next search request based on the following requirements or recommendations:
        # - If SearchType is set to **video** or **audio** and you need to traverse all data that matches the search conditions, this parameter is required.
        # - If PageNo exceeds **200**, set this parameter to optimize search performance.
        self.scroll_token = scroll_token
        # The type of media asset to search. Valid values:
        # 
        # - **video** (default): video.
        # - **audio**: audio.
        # - **image**: image.
        # - **attached**: auxiliary media asset.
        # 
        # > If this parameter is set to **video** or **audio** and you need to traverse all data that matches the search conditions, you must set the ScrollToken parameter.
        self.search_type = search_type
        # The sort field and sort order. Separate multiple values with commas (,). Valid values:
        # - **CreationTime:Desc** (default): sorts by creation time in descending order.
        # - **CreationTime:Asc**: sorts by creation time in ascending order.
        # 
        # > - For sort field examples, see [Sort fields](https://help.aliyun.com/document_detail/99179.html).
        # > - When retrieving the first 5,000 records of search results, up to three sort fields are supported.
        # > - When retrieving all data that matches the search conditions, only one sort field is supported.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        if self.match is not None:
            result['Match'] = self.match

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token

        if self.search_type is not None:
            result['SearchType'] = self.search_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Match') is not None:
            self.match = m.get('Match')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')

        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

