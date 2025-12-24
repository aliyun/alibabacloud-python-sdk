# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOfficeSiteOverviewRequest(DaraModel):
    def __init__(
        self,
        force_refresh: bool = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: List[str] = None,
        query_range: int = None,
        region_id: str = None,
    ):
        # Specifies whether to refresh the cache.
        self.force_refresh = force_refresh
        # The number of entries to return on each page.
        # 
        # *   Valid values: 1 to 100
        # *   Default value: 10
        self.max_results = max_results
        # The token that determines the start point of the next query. If this is your first query or no next query is to be sent, skip this parameter. If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The office network IDs. You can specify IDs of 1 to 100 office networks.
        self.office_site_id = office_site_id
        # The query scope. Cloud computers in a cloud computer pool are pooled cloud computers.
        # 
        # Default values:
        # 
        # *   1 (default): queries non-pooled cloud computers in the office network.
        # *   2: queries pooled cloud computers in the office network.
        # *   3: queries all cloud computers in the office network.
        self.query_range = query_range
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
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
        if self.force_refresh is not None:
            result['ForceRefresh'] = self.force_refresh

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.query_range is not None:
            result['QueryRange'] = self.query_range

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceRefresh') is not None:
            self.force_refresh = m.get('ForceRefresh')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('QueryRange') is not None:
            self.query_range = m.get('QueryRange')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

