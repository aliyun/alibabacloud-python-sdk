# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCategoriesRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        type: str = None,
    ):
        # The category ID. If you specify this parameter, the information about the specified category is returned. Only a single category ID is supported. You can obtain the category ID by using the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Asset Management Configuration** > **Category Management** to view the category ID.
        # - Obtain the category ID from the response of the [AddCategory](~~AddCategory~~) operation when you create a category.
        self.cate_id = cate_id
        # The page number of the subcategory list. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page of the subcategory list. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The method for sorting the query results. Valid values:
        # 
        # - **CreationTime:Desc** (default): sorts the results by creation time in descending order.
        # - **CreationTime:Asc**: sorts the results by creation time in ascending order.
        self.sort_by = sort_by
        # The categorization type. If you specify this parameter, a filtered query is performed to return categories of the specified type. Valid values:
        # - **default**: audio, video, and image categorization.
        # - **material**: short video material categorization.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

