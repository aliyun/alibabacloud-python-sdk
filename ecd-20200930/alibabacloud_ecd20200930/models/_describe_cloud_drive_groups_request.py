# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCloudDriveGroupsRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        directory_id: str = None,
        directory_name: str = None,
        drive_status: str = None,
        drive_type: str = None,
        group_id: List[str] = None,
        group_name: str = None,
        group_type: str = None,
        max_results: int = None,
        next_token: str = None,
        parent_group_id: str = None,
        region_id: str = None,
    ):
        # The enterprise cloud drive ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The office network ID.
        self.directory_id = directory_id
        # The office network name.
        self.directory_name = directory_name
        # The team space status.
        self.drive_status = drive_status
        # Specifies whether a space is added. Default value: empty, which indicates that all types are queried.
        self.drive_type = drive_type
        # The list of team space IDs.
        self.group_id = group_id
        # The team space name. Fuzzy match is supported.
        self.group_name = group_name
        # The team type. Default value: empty, which indicates that all types are queried.
        self.group_type = group_type
        # The number of entries per page for a paged query.
        # 
        # - Maximum value: 100.
        # - Default value: 20.
        self.max_results = max_results
        # The pagination token. Set this parameter to the value of `NextToken` that was returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        # The ID of the parent node of the object to query. To query the root node, set this parameter to `root`.
        # 
        # Default value: empty, which indicates that all team spaces are queried.
        self.parent_group_id = parent_group_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
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
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.drive_status is not None:
            result['DriveStatus'] = self.drive_status

        if self.drive_type is not None:
            result['DriveType'] = self.drive_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_group_id is not None:
            result['ParentGroupId'] = self.parent_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('DriveStatus') is not None:
            self.drive_status = m.get('DriveStatus')

        if m.get('DriveType') is not None:
            self.drive_type = m.get('DriveType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentGroupId') is not None:
            self.parent_group_id = m.get('ParentGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

