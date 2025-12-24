# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNASFileSystemsRequest(DaraModel):
    def __init__(
        self,
        file_system_id: List[str] = None,
        match_compatible_profile: bool = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The IDs of the NAS file systems.
        self.file_system_id = file_system_id
        # Specifies whether to include only NAS file systems that support the User Profile Management (UPM) feature in the query results.
        self.match_compatible_profile = match_compatible_profile
        # The number of entries to return on each page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that determines the start point of the query.
        self.next_token = next_token
        # The ID of the office network.
        self.office_site_id = office_site_id
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.match_compatible_profile is not None:
            result['MatchCompatibleProfile'] = self.match_compatible_profile

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
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MatchCompatibleProfile') is not None:
            self.match_compatible_profile = m.get('MatchCompatibleProfile')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

