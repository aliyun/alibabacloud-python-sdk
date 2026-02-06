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
        # The media asset fields to return in the query results.
        # 
        # By default, only the basic media asset fields are returned. You can specify additional media asset fields that need to be returned in the request. For more information, see the "API examples" section of the [Search for media asset information](https://help.aliyun.com/document_detail/99179.html) topic.
        self.fields = fields
        # The filter condition. For more information about the syntax, see [Protocol for media asset search](https://help.aliyun.com/document_detail/86991.html).
        self.match = match
        # The number of the page to return. Default value: **1**.
        # 
        # > If the value of this parameter exceeds **200**, we recommend that you set the ScrollToken parameter as well.
        self.page_no = page_no
        # The number of entries to return on each page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The pagination identifier. The password must be 32 characters in length The first time you call this operation for each new search, you do not need to specify this parameter. The value of this parameter is returned each time data records that meet the specified filter condition are found. The value is used to record the current position of queried data. Record the returned parameter value and set this parameter according to the following requirements during the next search:
        # 
        # *   If SearchType is set to **video** or **audio** and you need to traverse all data that meets the filter criteria, you must set the ScrollToken parameter.
        # *   If the value of the PageNo parameter exceeds **200**, we recommend that you set this parameter to optimize search performance.
        self.scroll_token = scroll_token
        # The type of the media asset that you want to query. Default value: video. Valid values:
        # 
        # *   **video**
        # *   **audio**
        # *   **image**
        # *   **attached**
        # 
        # > If this parameter is set to **video** or **audio** and you want to traverse all data that meets the filter criteria, you must set the ScrollToken parameter.
        self.search_type = search_type
        # The sort field and order. Separate multiple values with commas (,). Default value: CreationTime:Desc. Valid values:
        # 
        # *   **CreationTime:Desc**: The results are sorted in reverse chronological order based on the creation time.
        # *   **CreationTime:Asc**: The results are sorted in chronological order based on the creation time.
        # 
        # > * For more information about the sort field, see "Sort field" in the [Search for media asset information](https://help.aliyun.com/document_detail/99179.html) topic.
        # > * To obtain the first 5,000 data records that meet the specified filter criteria, you can specify a maximum of three sort fields.
        # > * To obtain all the data records that meet the specified filter criteria, you can specify only one sort field.
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

