# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDiagnosticMetricSetsRequest(DaraModel):
    def __init__(
        self,
        metric_set_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of diagnostic metric sets. You can specify up to 10 set IDs.
        # 
        # This parameter is required.
        self.metric_set_ids = metric_set_ids
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_set_ids is not None:
            result['MetricSetIds'] = self.metric_set_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricSetIds') is not None:
            self.metric_set_ids = m.get('MetricSetIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

