# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeVersionPageListResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeVersionPageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # The maximum amount of data to be read in this call, with a default value of 10.
        self.max_results = max_results
        # 用来表示当前调用返回读取到的位置。空代表数据已经读取完毕。
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Number of items per page, with a default value of 10.
        self.page_size = page_size
        # Returned object.
        self.result_object = result_object
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeVersionPageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeVersionPageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        content: str = None,
        creator: str = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        modifier: str = None,
        object_code: str = None,
        object_id: int = None,
        region: str = None,
        type: str = None,
        user_id: int = None,
        version: int = None,
    ):
        # Change content.
        self.content = content
        # Creator.
        self.creator = creator
        # Variable description.
        self.description = description
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary key ID of the version.
        self.id = id
        # Modifier.
        self.modifier = modifier
        # Name of the variable.
        self.object_code = object_code
        # Primary key ID of the variable.
        self.object_id = object_id
        # Region ID.
        self.region = region
        # Variable type.
        self.type = type
        # User UID.
        self.user_id = user_id
        # Version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.object_code is not None:
            result['objectCode'] = self.object_code

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.region is not None:
            result['region'] = self.region

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('objectCode') is not None:
            self.object_code = m.get('objectCode')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

