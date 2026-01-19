# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApisByBackendResponseBody(DaraModel):
    def __init__(
        self,
        api_info_list: main_models.DescribeApisByBackendResponseBodyApiInfoList = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the returned API list.
        self.api_info_list = api_info_list
        # The number of the current page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.api_info_list:
            self.api_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_info_list is not None:
            result['ApiInfoList'] = self.api_info_list.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfoList') is not None:
            temp_model = main_models.DescribeApisByBackendResponseBodyApiInfoList()
            self.api_info_list = temp_model.from_map(m.get('ApiInfoList'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisByBackendResponseBodyApiInfoList(DaraModel):
    def __init__(
        self,
        api_info: List[main_models.DescribeApisByBackendResponseBodyApiInfoListApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for v1 in self.api_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k1 in self.api_info:
                result['ApiInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k1 in m.get('ApiInfo'):
                temp_model = main_models.DescribeApisByBackendResponseBodyApiInfoListApiInfo()
                self.api_info.append(temp_model.from_map(k1))

        return self

class DescribeApisByBackendResponseBodyApiInfoListApiInfo(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        method: str = None,
        path: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The description of the API.
        self.description = description
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The request method of the API.
        self.method = method
        # The request path of the API.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.method is not None:
            result['Method'] = self.method

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

