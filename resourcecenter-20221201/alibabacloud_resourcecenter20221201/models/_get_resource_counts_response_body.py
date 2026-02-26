# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetResourceCountsResponseBody(DaraModel):
    def __init__(
        self,
        filters: List[main_models.GetResourceCountsResponseBodyFilters] = None,
        group_by_key: str = None,
        request_id: str = None,
        resource_counts: List[main_models.GetResourceCountsResponseBodyResourceCounts] = None,
    ):
        # The filter conditions.
        self.filters = filters
        # The dimension by which the queried resources are grouped.
        self.group_by_key = group_by_key
        # The request ID.
        self.request_id = request_id
        # The list of resource counts.
        self.resource_counts = resource_counts

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()
        if self.resource_counts:
            for v1 in self.resource_counts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceCounts'] = []
        if self.resource_counts is not None:
            for k1 in self.resource_counts:
                result['ResourceCounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.GetResourceCountsResponseBodyFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_counts = []
        if m.get('ResourceCounts') is not None:
            for k1 in m.get('ResourceCounts'):
                temp_model = main_models.GetResourceCountsResponseBodyResourceCounts()
                self.resource_counts.append(temp_model.from_map(k1))

        return self

class GetResourceCountsResponseBodyResourceCounts(DaraModel):
    def __init__(
        self,
        count: int = None,
        group_name: str = None,
    ):
        # The number of resources.
        self.count = count
        # The group name.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class GetResourceCountsResponseBodyFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The values of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

