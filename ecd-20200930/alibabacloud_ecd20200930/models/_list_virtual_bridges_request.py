# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVirtualBridgesRequest(DaraModel):
    def __init__(
        self,
        bridge_id: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The list of virtual bridge IDs.
        self.bridge_id = bridge_id
        # The maximum number of entries to return. Valid values: 1 to 500.
        # Default value: 500.
        self.max_results = max_results
        # The token for the next query. If NextToken is empty, no more results exist.
        self.next_token = next_token
        # The office network ID.
        # 
        # > The `DirectoryId` parameter will be deprecated. Use this parameter instead.
        self.office_site_id = office_site_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Wuying Workspace.
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
        if self.bridge_id is not None:
            result['BridgeId'] = self.bridge_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BridgeId') is not None:
            self.bridge_id = m.get('BridgeId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

