# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeClientEventsRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_ip: str = None,
        desktop_name: str = None,
        directory_id: str = None,
        end_time: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        event_type: str = None,
        event_types: List[str] = None,
        fill_hardware_info: bool = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cloud computer ID. If you do not specify this parameter, all cloud computers in the region are queried.
        self.desktop_id = desktop_id
        # The IP address of the cloud computer. If you do not specify this parameter, events of all cloud computers in the region are queried.
        self.desktop_ip = desktop_ip
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # > This parameter is not publicly available.
        self.directory_id = directory_id
        # The end time. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC+0. If you do not specify this parameter, the current time is used.
        self.end_time = end_time
        # The logon user information, which is a Resource Access Management (RAM) user ID or AD username. If you do not specify this parameter, events of all users in the region are queried.
        self.end_user_id = end_user_id
        self.end_user_ids = end_user_ids
        # The event type to query. If EventTypes is not empty, the EventTypes combination is used as the query filter condition. If both EventTypes and EventType are empty, all events are queried.
        self.event_type = event_type
        # The combination of event types to query. You can specify multiple event types. The query results include events of all specified types.
        self.event_types = event_types
        self.fill_hardware_info = fill_hardware_info
        self.language = language
        # The number of entries per page for a paged query. Default value: 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the value of NextToken returned in the previous API call.
        self.next_token = next_token
        # The ID of the office network to which the cloud computer belongs. If you do not specify this parameter, user events in all office networks in the region are queried.
        self.office_site_id = office_site_id
        # The name of the office network.
        self.office_site_name = office_site_name
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC+0. If you do not specify this parameter, events are queried backward from the time specified by `EndTime`.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        if self.fill_hardware_info is not None:
            result['FillHardwareInfo'] = self.fill_hardware_info

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        if m.get('FillHardwareInfo') is not None:
            self.fill_hardware_info = m.get('FillHardwareInfo')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

