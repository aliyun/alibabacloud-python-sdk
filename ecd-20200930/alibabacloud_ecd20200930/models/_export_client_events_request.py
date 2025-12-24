# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportClientEventsRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        end_time: str = None,
        end_user_id: str = None,
        event_type: str = None,
        event_types: List[str] = None,
        lang_type: str = None,
        max_results: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The end of the time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # 
        # If you do not specify a value for this parameter, the current time is used.
        self.end_time = end_time
        # The ID of the endpoint user.
        self.end_user_id = end_user_id
        # The type of the event that you want to query. If you provide multiple values for EventTypes, the response will include events of all the specified types. If you provide no values for EventTypes and EventType, the response will include all events in the designated region.
        # 
        # Valid values:
        # 
        # *   DESKTOP_STOP: the shutdown event.
        # *   GET_LITE_CONNECTION_TICKET: the event of retrieving the connection ticket.
        # *   DESKTOP_DISCONNECT: the session disconnection event.
        # *   CLIENT_LOGIN: the user logon event.
        # *   GET_CONNECTION_TICKET: the connection credential retrieval event.
        # *   DESKTOP_REBOOT: the restart event.
        # *   DESKTOP_CONNECT: the session establishment event.
        # *   DESKTOP_START: the start event.
        self.event_type = event_type
        # The types of the events that you want to query. You can include multiple event types, and the response will return events matching the specified types or all events if none are specified.
        self.event_types = event_types
        # The language displayed on the frontend page. The backend uses this setting to define the language of exported files.
        # 
        # Valid values:
        # 
        # *   zh-CN: Simplified Chinese.
        # *   en-GB: British English.
        self.lang_type = lang_type
        # The number of entries to return on each page.
        # 
        # *   Maximum value: 5000.
        # *   Default value: 5000.
        self.max_results = max_results
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # 
        # If you do not specify a value for this parameter, all events that occurred before the point in time that you specify for `EndTime` are queried.
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

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        if self.lang_type is not None:
            result['LangType'] = self.lang_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

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

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        if m.get('LangType') is not None:
            self.lang_type = m.get('LangType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

