# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetResourceCountsRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.GetResourceCountsRequestFilter] = None,
        group_by_key: str = None,
        include_deleted_resources: bool = None,
        search_expression: str = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The dimension by which the queried resources are grouped. Valid values:
        # 
        # - ResourceType: The resource type.
        # 
        # - RegionId: The region.
        # 
        # - ResourceGroupId: The resource group ID.
        self.group_by_key = group_by_key
        # Specifies whether to include deleted resources. Valid values:
        # 
        # - true
        # 
        # - false
        self.include_deleted_resources = include_deleted_resources
        # The search keyword. Resource Center filters the search results based on relevance.
        self.search_expression = search_expression

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key

        if self.include_deleted_resources is not None:
            result['IncludeDeletedResources'] = self.include_deleted_resources

        if self.search_expression is not None:
            result['SearchExpression'] = self.search_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.GetResourceCountsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')

        if m.get('IncludeDeletedResources') is not None:
            self.include_deleted_resources = m.get('IncludeDeletedResources')

        if m.get('SearchExpression') is not None:
            self.search_expression = m.get('SearchExpression')

        return self

class GetResourceCountsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For information about valid values, see the "`Supported filter parameters`" section below.
        self.key = key
        # The matching method.
        # 
        # Set this parameter to `Equals`, which means an equal match.
        self.match_type = match_type
        # The values of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

