# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregatedDesktopsRequest(DaraModel):
    def __init__(
        self,
        aggregation_factor: str = None,
        region_id: str = None,
        search_region_id: str = None,
    ):
        # The aggregation factor.
        self.aggregation_factor = aggregation_factor
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the list of regions supported by WUYING Workspace.
        self.region_id = region_id
        # The search region ID. Used to filter desktop information for a specified region.
        self.search_region_id = search_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_factor is not None:
            result['AggregationFactor'] = self.aggregation_factor

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationFactor') is not None:
            self.aggregation_factor = m.get('AggregationFactor')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        return self

