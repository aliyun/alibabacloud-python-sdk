# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class GetResourceCategoryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetResourceCategoryResponseBodyData = None,
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
            temp_model = main_models.GetResourceCategoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetResourceCategoryResponseBodyData(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        resource_category_id: str = None,
        resource_category_name: str = None,
        resource_category_type: str = None,
        resource_count: List[main_models.GetResourceCategoryResponseBodyDataResourceCount] = None,
        resource_matcher: str = None,
        resource_type: str = None,
    ):
        # Applicable product type. If empty, matches all products.
        self.product_type = product_type
        # Resource category ID, globally unique.
        self.resource_category_id = resource_category_id
        # Resource name, unique within the namespace.
        self.resource_category_name = resource_category_name
        # Resource category type. Valid values:
        # 
        # - DEFAULT: default group, created by the system, cannot be deleted.
        # 
        # - CUSTOM: custom group, can be deleted.
        self.resource_category_type = resource_category_type
        # Number of resources by type.
        self.resource_count = resource_count
        # Resource matcher. If empty, no resources are matched.
        self.resource_matcher = resource_matcher
        # Applicable resource type. If empty, matches all resources.
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
                temp_model = main_models.GetResourceCategoryResponseBodyDataResourceCount()
                self.resource_count.append(temp_model.from_map(k1))

        if m.get('ResourceMatcher') is not None:
            self.resource_matcher = m.get('ResourceMatcher')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetResourceCategoryResponseBodyDataResourceCount(DaraModel):
    def __init__(
        self,
        count: int = None,
        resource_type: str = None,
    ):
        # Number of resources by type.
        self.count = count
        # Resource type.
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

