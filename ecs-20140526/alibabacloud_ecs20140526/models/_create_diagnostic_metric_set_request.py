# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateDiagnosticMetricSetRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        metric_ids: List[str] = None,
        metric_set_name: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The description of the diagnostic metric set.
        self.description = description
        # The IDs of diagnostic metrics. You can specify up to 100 diagnostic metric IDs.
        # 
        # This parameter is required.
        self.metric_ids = metric_ids
        # The name of the diagnostic metric set.
        self.metric_set_name = metric_set_name
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the resource.
        # 
        # Default value: instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.metric_ids is not None:
            result['MetricIds'] = self.metric_ids

        if self.metric_set_name is not None:
            result['MetricSetName'] = self.metric_set_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MetricIds') is not None:
            self.metric_ids = m.get('MetricIds')

        if m.get('MetricSetName') is not None:
            self.metric_set_name = m.get('MetricSetName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

