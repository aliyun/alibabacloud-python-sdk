# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupResourceCountsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_counts: List[main_models.GetResourceGroupResourceCountsResponseBodyResourceCounts] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The numbers of the resources.
        self.resource_counts = resource_counts

    def validate(self):
        if self.resource_counts:
            for v1 in self.resource_counts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceCounts'] = []
        if self.resource_counts is not None:
            for k1 in self.resource_counts:
                result['ResourceCounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_counts = []
        if m.get('ResourceCounts') is not None:
            for k1 in m.get('ResourceCounts'):
                temp_model = main_models.GetResourceGroupResourceCountsResponseBodyResourceCounts()
                self.resource_counts.append(temp_model.from_map(k1))

        return self

class GetResourceGroupResourceCountsResponseBodyResourceCounts(DaraModel):
    def __init__(
        self,
        count: int = None,
        group_by_key: str = None,
        resource_group_id: str = None,
    ):
        # The number of the resources.
        self.count = count
        # The dimension by which resources are queried.
        self.group_by_key = group_by_key
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

