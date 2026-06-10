# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOfficeSiteUsersRequest(DaraModel):
    def __init__(
        self,
        assigned_info: str = None,
        filter: str = None,
        include_assigned_user: bool = None,
        max_results: int = None,
        next_token: str = None,
        oupath: str = None,
        office_site_id: str = None,
        region_id: str = None,
        sort_type: str = None,
    ):
        self.assigned_info = assigned_info
        # The query string for fuzzy matching.
        self.filter = filter
        self.include_assigned_user = include_assigned_user
        # The number of entries to return on each page.
        # 
        # - Maximum value: 100.
        # 
        # - Default value: 10.
        self.max_results = max_results
        # The token for the next page of results. Leave this empty for the first query. For subsequent queries, use the NextToken value from the previous response.
        self.next_token = next_token
        # The path of the organizational unit (OU) in the AD domain.
        self.oupath = oupath
        # The office network ID. Only office networks that use enterprise AD accounts are supported.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID. Call [DescribeRegions](~~DescribeRegions~~) to get a list of regions where WUYING Workspace is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_info is not None:
            result['AssignedInfo'] = self.assigned_info

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.include_assigned_user is not None:
            result['IncludeAssignedUser'] = self.include_assigned_user

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.oupath is not None:
            result['OUPath'] = self.oupath

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedInfo') is not None:
            self.assigned_info = m.get('AssignedInfo')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('IncludeAssignedUser') is not None:
            self.include_assigned_user = m.get('IncludeAssignedUser')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OUPath') is not None:
            self.oupath = m.get('OUPath')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

