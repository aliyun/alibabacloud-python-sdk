# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListCategoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCategoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListCategoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCategoryResponseBodyData(DaraModel):
    def __init__(
        self,
        category_list: List[main_models.ListCategoryResponseBodyDataCategoryList] = None,
        has_next: bool = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.category_list = category_list
        self.has_next = has_next
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.category_list:
            for v1 in self.category_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CategoryList'] = []
        if self.category_list is not None:
            for k1 in self.category_list:
                result['CategoryList'].append(k1.to_map() if k1 else None)

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_list = []
        if m.get('CategoryList') is not None:
            for k1 in m.get('CategoryList'):
                temp_model = main_models.ListCategoryResponseBodyDataCategoryList()
                self.category_list.append(temp_model.from_map(k1))

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCategoryResponseBodyDataCategoryList(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        category_type: str = None,
        is_default: bool = None,
        parent_category_id: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type
        self.is_default = is_default
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        return self

