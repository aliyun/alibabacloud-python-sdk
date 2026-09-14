# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDedicatedBlockStorageClusterDisksRequest(DaraModel):
    def __init__(
        self,
        dbsc_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The dedicated block storage cluster ID.
        # 
        # This parameter is required.
        self.dbsc_id = dbsc_id
        # The maximum number of entries per page for a paged query. Maximum value: 500.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        # The region ID of the dedicated block storage cluster. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
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
        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

