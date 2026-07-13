# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class ListResourceCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListResourceCategoriesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The unique ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListResourceCategoriesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListResourceCategoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListResourceCategoriesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The collection of records returned in this request.
        self.content = content
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # Indicates the position where the current call returns data from. An empty value indicates that all data has been read.
        self.next_token = next_token
        # The total number of data entries under the current request conditions. This parameter is optional and can be left unspecified by default.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListResourceCategoriesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourceCategoriesResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        resource_category_id: str = None,
        resource_category_name: str = None,
        resource_category_type: str = None,
        resource_count: List[main_models.ListResourceCategoriesResponseBodyDataContentResourceCount] = None,
        resource_matcher: str = None,
        resource_type: str = None,
    ):
        # The applicable product type. If this parameter is empty, all products are matched.
        self.product_type = product_type
        # The resource category ID, which is globally unique.
        self.resource_category_id = resource_category_id
        # The resource name, which is unique within the namespace.
        self.resource_category_name = resource_category_name
        # The resource category type. Valid values:
        # 
        # - DEFAULT: default group created by the system, cannot be deleted.
        # 
        # - CUSTOM: custom group, can be deleted.
        self.resource_category_type = resource_category_type
        # The number of resources of each type.
        self.resource_count = resource_count
        # The resource matcher. If this parameter is empty, no resources are matched.
        self.resource_matcher = resource_matcher
        # The applicable resource type. If this parameter is empty, all resources are matched.
        self.resource_type = resource_type

    def validate(self):
        if self.resource_count:
            for v1 in self.resource_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        if self.resource_category_name is not None:
            result['ResourceCategoryName'] = self.resource_category_name

        if self.resource_category_type is not None:
            result['ResourceCategoryType'] = self.resource_category_type

        result['ResourceCount'] = []
        if self.resource_count is not None:
            for k1 in self.resource_count:
                result['ResourceCount'].append(k1.to_map() if k1 else None)

        if self.resource_matcher is not None:
            result['ResourceMatcher'] = self.resource_matcher

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        if m.get('ResourceCategoryName') is not None:
            self.resource_category_name = m.get('ResourceCategoryName')

        if m.get('ResourceCategoryType') is not None:
            self.resource_category_type = m.get('ResourceCategoryType')

        self.resource_count = []
        if m.get('ResourceCount') is not None:
            for k1 in m.get('ResourceCount'):
                temp_model = main_models.ListResourceCategoriesResponseBodyDataContentResourceCount()
                self.resource_count.append(temp_model.from_map(k1))

        if m.get('ResourceMatcher') is not None:
            self.resource_matcher = m.get('ResourceMatcher')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class ListResourceCategoriesResponseBodyDataContentResourceCount(DaraModel):
    def __init__(
        self,
        count: int = None,
        resource_type: str = None,
    ):
        # The number of resources of each type.
        self.count = count
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

