# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeNameListPageListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        page_size: str = None,
        request_id: str = None,
        result_object: List[main_models.DescribeNameListPageListResponseBodyResultObject] = None,
        total_item: str = None,
        total_page: str = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Returned object
        self.result_object = result_object
        # Total number of items
        self.total_item = total_item
        # Total number of pages
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
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

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
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeNameListPageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeNameListPageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        memo: str = None,
        name: str = None,
        name_list_type: str = None,
        title: str = None,
        user_id: str = None,
        value: str = None,
        variable_id: int = None,
    ):
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # ID of the list variable content data
        self.id = id
        # NameList Content memo
        self.memo = memo
        # Variable name
        self.name = name
        # Variable type
        self.name_list_type = name_list_type
        # Title.
        self.title = title
        # User UID
        self.user_id = user_id
        # Variable value
        self.value = value
        # Variable ID.
        self.variable_id = variable_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.memo is not None:
            result['memo'] = self.memo

        if self.name is not None:
            result['name'] = self.name

        if self.name_list_type is not None:
            result['nameListType'] = self.name_list_type

        if self.title is not None:
            result['title'] = self.title

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.value is not None:
            result['value'] = self.value

        if self.variable_id is not None:
            result['variableId'] = self.variable_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameListType') is not None:
            self.name_list_type = m.get('nameListType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('variableId') is not None:
            self.variable_id = m.get('variableId')

        return self

