# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListProductDimensionGroupsResponseBody(DaraModel):
    def __init__(
        self,
        dimension_groups: List[main_models.ListProductDimensionGroupsResponseBodyDimensionGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The dimension groups.
        self.dimension_groups = dimension_groups
        # The maximum number of entries returned on each page.
        self.max_results = max_results
        # The token that marks the position where the returned query results end. An empty value indicates that all data is returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries that match the query.
        self.total_count = total_count

    def validate(self):
        if self.dimension_groups:
            for v1 in self.dimension_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DimensionGroups'] = []
        if self.dimension_groups is not None:
            for k1 in self.dimension_groups:
                result['DimensionGroups'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimension_groups = []
        if m.get('DimensionGroups') is not None:
            for k1 in m.get('DimensionGroups'):
                temp_model = main_models.ListProductDimensionGroupsResponseBodyDimensionGroups()
                self.dimension_groups.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProductDimensionGroupsResponseBodyDimensionGroups(DaraModel):
    def __init__(
        self,
        dimension_keys: List[str] = None,
        group_code: str = None,
        group_name: str = None,
        product_code: str = None,
    ):
        # The keys of the dimension group.
        self.dimension_keys = dimension_keys
        # The code of the dimension group.
        self.group_code = group_code
        # The name of the dimension group.
        self.group_name = group_name
        # The code of the Alibaba Cloud service.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension_keys is not None:
            result['DimensionKeys'] = self.dimension_keys

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKeys') is not None:
            self.dimension_keys = m.get('DimensionKeys')

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

