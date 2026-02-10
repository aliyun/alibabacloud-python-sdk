# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyScaItemResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribePropertyScaItemResponseBodyPageInfo = None,
        property_items: List[main_models.DescribePropertyScaItemResponseBodyPropertyItems] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # An array that consists of the information about middleware fingerprints.
        self.property_items = property_items
        # The ID of the request, which is used to locate and troubleshoot issues.
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
            temp_model = main_models.DescribePropertyScaItemResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.property_items = []
        if m.get('PropertyItems') is not None:
            for k1 in m.get('PropertyItems'):
                temp_model = main_models.DescribePropertyScaItemResponseBodyPropertyItems()
                self.property_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePropertyScaItemResponseBodyPropertyItems(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        count: int = None,
        name: str = None,
        type_display: str = None,
    ):
        # The type of the middleware, database, or web service. Valid values:
        # 
        # *   **system_service**: system service
        # *   **software_library**: software library
        # *   **docker_component**: container component
        # *   **database**: database
        # *   **web_container**: web container
        # *   **jar**: JAR package
        # *   **web_framework**: web framework
        self.biz_type = biz_type
        # The number of servers on which the middleware is run.
        self.count = count
        # The name of the middleware.
        self.name = name
        # The display name of the middleware type.
        self.type_display = type_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        if self.type_display is not None:
            result['TypeDisplay'] = self.type_display

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TypeDisplay') is not None:
            self.type_display = m.get('TypeDisplay')

        return self

class DescribePropertyScaItemResponseBodyPageInfo(DaraModel):
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

