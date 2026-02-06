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
        # The ID of the category. If you specify this parameter, the system queries the category based on the ID. You can specify only one category ID. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). Choose **Configuration Management** > **Media Management** > **Categories**. On the Audio and Video / Image Category or Short Video Material Category tab, view the category ID.
        # *   Obtain the category ID from the response to the [AddCategory](~~AddCategory~~) operation.
        self.cate_id = cate_id
        # The number of the page where the subcategories to be returned are listed. Default value: **1**.
        self.page_no = page_no
        # The number of entries to return on each page of the subcategory list. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The sorting method of the results. Valid values:
        # 
        # *   **CreationTime:Desc** (default): The results are sorted in reverse chronological order based on the creation time.
        # *   **CreationTime:Asc**: The results are sorted in chronological order based on the creation time.
        self.sort_by = sort_by
        # The type of the category. If you specify this parameter, the system queries the category based on the type. Valid values:
        # 
        # *   **default** (default): audio, video, and image files
        # *   **material**: short video materials
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

