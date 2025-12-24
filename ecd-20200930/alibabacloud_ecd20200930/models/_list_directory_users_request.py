# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDirectoryUsersRequest(DaraModel):
    def __init__(
        self,
        assigned_info: str = None,
        directory_id: str = None,
        filter: str = None,
        include_assigned_user: bool = None,
        max_results: int = None,
        next_token: str = None,
        oupath: str = None,
        region_id: str = None,
        sort_type: str = None,
    ):
        # > This parameter is not publicly available. The value can be 1 or left empty.
        self.assigned_info = assigned_info
        # The ID of the AD directory.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The query string for fuzzy match. If you specify this parameter, the system returns all results that contain the string.
        self.filter = filter
        # Specifies whether to return the users with assigned cloud computers only.
        self.include_assigned_user = include_assigned_user
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token used to start the next query. If the value of this parameter is empty, all results are returned.
        self.next_token = next_token
        # The organizational unit (OU) in the specified AD domain.
        self.oupath = oupath
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The sort type.
        # 
        # Valide values:
        # 
        # - asc: cloud computers assigned to users on bottom
        # - desc: cloud computers assigned to users on top
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

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedInfo') is not None:
            self.assigned_info = m.get('AssignedInfo')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

