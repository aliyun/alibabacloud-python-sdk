# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListComputeJobsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        search: str = None,
        sort_direction: str = None,
        sort_field: str = None,
    ):
        # The compute instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of jobs to return in the current request. Default value: 10. Maximum value: 1000. If you set this parameter to 0, the default value is used.
        self.max_results = max_results
        # The pagination token. Do not specify this parameter in the first request. For subsequent requests, use the `NextToken` value returned in the previous response.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The keyword used to search for jobs by name or remark.
        self.search = search
        # The sort direction. The value is not case-sensitive. Valid values: `ASC` and `DESC`.
        self.sort_direction = sort_direction
        # The sort field. Valid values: `createTime`, `cuReserved`, `cuLimit`, `cuUsed`, `status`, and `jobName`.
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search is not None:
            result['Search'] = self.search

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        return self

