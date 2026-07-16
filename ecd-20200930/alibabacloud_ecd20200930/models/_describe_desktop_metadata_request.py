# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDesktopMetadataRequest(DaraModel):
    def __init__(
        self,
        creation_time_start: str = None,
        desktop_ids: List[str] = None,
        end_user_id: str = None,
        group_id: str = None,
        host_name: str = None,
        image_id: str = None,
        include_desktop_group: bool = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        operation_time_start: str = None,
        region_id: str = None,
        search_region_id: str = None,
    ):
        # The creation time of the cloud computer. The time must be in the `yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\"` format and in UTC.
        self.creation_time_start = creation_time_start
        # A list of cloud computer IDs.
        self.desktop_ids = desktop_ids
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The ID of the cloud computer share.
        self.group_id = group_id
        # The hostname.
        self.host_name = host_name
        # The ID of the image.
        self.image_id = image_id
        # Specifies whether to include cloud computers in cloud computer shares in the response.
        self.include_desktop_group = include_desktop_group
        # > This parameter is not yet available.
        self.keyword = keyword
        # The maximum number of entries to return per page. Maximum: 100. Default: 10.
        self.max_results = max_results
        # The token returned from the previous call to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the office network.
        self.office_site_id = office_site_id
        # The start of the time range to query for operations. The time must be in the `yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\"` format and in UTC.
        self.operation_time_start = operation_time_start
        # The region ID.
        self.region_id = region_id
        # The ID of the region to search.
        self.search_region_id = search_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time_start is not None:
            result['CreationTimeStart'] = self.creation_time_start

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.include_desktop_group is not None:
            result['IncludeDesktopGroup'] = self.include_desktop_group

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.operation_time_start is not None:
            result['OperationTimeStart'] = self.operation_time_start

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTimeStart') is not None:
            self.creation_time_start = m.get('CreationTimeStart')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('IncludeDesktopGroup') is not None:
            self.include_desktop_group = m.get('IncludeDesktopGroup')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OperationTimeStart') is not None:
            self.operation_time_start = m.get('OperationTimeStart')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        return self

