# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskCheckItemResultResponseBody(DaraModel):
    def __init__(
        self,
        page_content_resource: main_models.DescribeRiskCheckItemResultResponseBodyPageContentResource = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_content_resource = page_content_resource
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.page_content_resource:
            self.page_content_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_content_resource is not None:
            result['PageContentResource'] = self.page_content_resource.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageContentResource') is not None:
            temp_model = main_models.DescribeRiskCheckItemResultResponseBodyPageContentResource()
            self.page_content_resource = temp_model.from_map(m.get('PageContentResource'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRiskCheckItemResultResponseBodyPageContentResource(DaraModel):
    def __init__(
        self,
        content_resource: Dict[str, Any] = None,
        count: int = None,
        current_page: int = None,
        page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data of the affected assets on each page in a dynamic table.
        self.content_resource = content_resource
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The total number of pages returned.
        self.page_count = page_count
        # The number of entries returned on each page.
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
        if self.content_resource is not None:
            result['ContentResource'] = self.content_resource

        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentResource') is not None:
            self.content_resource = m.get('ContentResource')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

