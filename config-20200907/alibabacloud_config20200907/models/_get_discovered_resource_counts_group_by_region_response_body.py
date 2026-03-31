# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetDiscoveredResourceCountsGroupByRegionResponseBody(DaraModel):
    def __init__(
        self,
        discovered_resource_counts_summary: List[main_models.GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary] = None,
        request_id: str = None,
    ):
        # The statistics on the resources.
        self.discovered_resource_counts_summary = discovered_resource_counts_summary
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_counts_summary:
            for v1 in self.discovered_resource_counts_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k1 in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k1 in m.get('DiscoveredResourceCountsSummary'):
                temp_model = main_models.GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        region: str = None,
        resource_count: int = None,
    ):
        # The dimension by which statistics are collected.
        # 
        # >  In most cases, the `Region` parameter instead of the GroupName parameter is returned.
        self.group_name = group_name
        # The ID of the region by which statistics are collected.
        self.region = region
        # The total number of resources.
        self.resource_count = resource_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        return self

