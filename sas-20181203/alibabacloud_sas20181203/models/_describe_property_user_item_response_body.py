# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyUserItemResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribePropertyUserItemResponseBodyPageInfo = None,
        property_items: List[main_models.DescribePropertyUserItemResponseBodyPropertyItems] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # An array that consists of the account information returned.
        self.property_items = property_items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.property_items:
            for v1 in self.property_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['PropertyItems'] = []
        if self.property_items is not None:
            for k1 in self.property_items:
                result['PropertyItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribePropertyUserItemResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.property_items = []
        if m.get('PropertyItems') is not None:
            for k1 in m.get('PropertyItems'):
                temp_model = main_models.DescribePropertyUserItemResponseBodyPropertyItems()
                self.property_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePropertyUserItemResponseBodyPropertyItems(DaraModel):
    def __init__(
        self,
        count: int = None,
        user: str = None,
    ):
        # The number of servers that belong to the account.
        self.count = count
        # The name of the account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class DescribePropertyUserItemResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

