# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeBasicSearchPageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeBasicSearchPageListResponseBodyResultObject = None,
    ):
        # Request ID
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeBasicSearchPageListResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeBasicSearchPageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[Dict[str, Any]] = None,
        header: List[main_models.DescribeBasicSearchPageListResponseBodyResultObjectHeader] = None,
        page_size: int = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Current page number in pagination queries.
        self.current_page = current_page
        # Returned data object
        self.data = data
        # Table header
        self.header = header
        # Page size, with a default value of 10
        self.page_size = page_size
        # Total number of items
        self.total_item = total_item
        # Total number of pages
        self.total_page = total_page

    def validate(self):
        if self.header:
            for v1 in self.header:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.data is not None:
            result['data'] = self.data

        result['header'] = []
        if self.header is not None:
            for k1 in self.header:
                result['header'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('data') is not None:
            self.data = m.get('data')

        self.header = []
        if m.get('header') is not None:
            for k1 in m.get('header'):
                temp_model = main_models.DescribeBasicSearchPageListResponseBodyResultObjectHeader()
                self.header.append(temp_model.from_map(k1))

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeBasicSearchPageListResponseBodyResultObjectHeader(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_title: str = None,
        is_default: bool = None,
    ):
        # Field name
        self.field_name = field_name
        # Field title.
        self.field_title = field_title
        # Whether it is a default display field (displayed in the response, not used as a parameter)
        # - true: Yes
        # - false: No
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.field_title is not None:
            result['fieldTitle'] = self.field_title

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldTitle') is not None:
            self.field_title = m.get('fieldTitle')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        return self

