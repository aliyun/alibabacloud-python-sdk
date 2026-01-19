# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeQueryVariablePageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeQueryVariablePageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Pagination parameter, current page.
        self.current_page = current_page
        # Page size, default value is 10
        self.page_size = page_size
        # Return object
        self.result_object = result_object
        # Total items
        self.total_item = total_item
        # Total pages
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeQueryVariablePageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeQueryVariablePageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        data_source_code: int = None,
        data_source_name: str = None,
        description: str = None,
        event_name: str = None,
        field_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        name: str = None,
        status: str = None,
        total: int = None,
        version: int = None,
    ):
        # Data source code.
        self.data_source_code = data_source_code
        # Data source name.
        self.data_source_name = data_source_name
        # Description information.
        self.description = description
        # Event name.
        self.event_name = event_name
        # Return value type
        self.field_type = field_type
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time
        self.gmt_modified = gmt_modified
        # Query variable primary key ID
        self.id = id
        # Query variable name
        self.name = name
        # Status.
        self.status = status
        # Total count
        self.total = total
        # Version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_code is not None:
            result['dataSourceCode'] = self.data_source_code

        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name

        if self.description is not None:
            result['description'] = self.description

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.total is not None:
            result['total'] = self.total

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceCode') is not None:
            self.data_source_code = m.get('dataSourceCode')

        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

