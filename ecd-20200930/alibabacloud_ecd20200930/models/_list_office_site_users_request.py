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
        # The query string for fuzzy query.
        self.filter = filter
        self.include_assigned_user = include_assigned_user
        # The number of entries per page.
        # 
        # *   Valid values: 1 to 100.
        # *   Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request or if no next query exists. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The organizational unit (OU) of the specified AD domain.
        self.oupath = oupath
        # The office network ID. The office network must be of the enterprise AD account type.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
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

