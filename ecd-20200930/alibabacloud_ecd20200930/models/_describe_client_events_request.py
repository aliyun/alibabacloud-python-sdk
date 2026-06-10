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
        # The ID of the cloud desktop. If you omit this parameter, the operation returns events for all cloud desktops in the region.
        self.desktop_id = desktop_id
        # The IP address of the cloud desktop. If you omit this parameter, the operation returns events for all cloud desktops in the region.
        self.desktop_ip = desktop_ip
        # The name of the cloud desktop.
        self.desktop_name = desktop_name
        # > This parameter is not in use.
        self.directory_id = directory_id
        # The end of the time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.<br>
        # If you omit this parameter, the operation uses the current time.<br>
        self.end_time = end_time
        # The ID of the end user, which can be a RAM user ID or an AD username. If you omit this parameter, the operation returns events for all users in the region.
        self.end_user_id = end_user_id
        # The event type to query. If EventTypes is specified, this parameter is ignored. If you omit both this parameter and EventTypes, the operation returns all events.
        self.event_type = event_type
        # An array of event types to query. The operation returns events that match any of the specified types.
        self.event_types = event_types
        self.fill_hardware_info = fill_hardware_info
        self.language = language
        # The maximum number of entries to return on each page.<br>
        # Default value: 100.<br>
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous response to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the office network to which the cloud desktop belongs. If you omit this parameter, the operation returns events for users in all office networks in the region.
        self.office_site_id = office_site_id
        # The name of the office network.
        self.office_site_name = office_site_name
        # The ID of the region. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start of the time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.<br>
        # If you omit this parameter, the query returns events that occurred before the time specified by `EndTime`.<br>
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

