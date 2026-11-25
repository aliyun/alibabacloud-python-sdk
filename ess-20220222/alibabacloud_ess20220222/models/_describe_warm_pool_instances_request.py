# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWarmPoolInstancesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        scaling_group_id: str = None,
    ):
        # The maximum number of entries per page for a paged query. Valid values: 1 to 50. Default value: 10.
        self.max_results = max_results
        # The query token. Set the value to the NextToken value returned from the previous call. You do not need to specify this parameter for the first call. An empty NextToken value indicates that no more results are available.
        self.next_token = next_token
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

