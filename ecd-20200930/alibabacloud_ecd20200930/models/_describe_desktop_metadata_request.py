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
        self.creation_time_start = creation_time_start
        self.desktop_ids = desktop_ids
        self.group_id = group_id
        self.host_name = host_name
        self.image_id = image_id
        self.include_desktop_group = include_desktop_group
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.operation_time_start = operation_time_start
        self.region_id = region_id
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

