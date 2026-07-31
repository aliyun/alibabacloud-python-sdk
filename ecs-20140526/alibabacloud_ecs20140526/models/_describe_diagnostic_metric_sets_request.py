# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDiagnosticMetricSetsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        metric_set_ids: List[str] = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
        type: str = None,
    ):
        # The number of entries per page for a paged query. Maximum value: 100.
        # 
        # Default value:
        # 
        # - If this parameter is not specified, the default value is 10.
        # - If the specified value is greater than 100, the default value is 100.
        self.max_results = max_results
        # The list of diagnostic metric set IDs.
        self.metric_set_ids = metric_set_ids
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource type.
        self.resource_type = resource_type
        # The type of the diagnostic metric set. Valid values:
        # 
        # - User: user.
        # - Common: common.
        # 
        # Default value: User.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.metric_set_ids is not None:
            result['MetricSetIds'] = self.metric_set_ids

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MetricSetIds') is not None:
            self.metric_set_ids = m.get('MetricSetIds')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

