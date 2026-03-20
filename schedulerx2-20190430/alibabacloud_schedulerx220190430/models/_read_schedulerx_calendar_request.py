# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadSchedulerxCalendarRequest(DaraModel):
    def __init__(
        self,
        calendar_name: str = None,
        fetch_calendar_detail: bool = None,
        fetch_system_calendar: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        year: int = None,
    ):
        # The calendar name.
        self.calendar_name = calendar_name
        # Specifies whether to retrieve calendar details. The default value is false.
        # 
        # *   false: Returns only basic information without the detailed list of days for each month.
        # *   true: Returns the detailed list of days for each month.
        self.fetch_calendar_detail = fetch_calendar_detail
        # Specifies whether to retrieve system calendars. The default value is false.
        # 
        # *   false: Returns only user-defined calendars.
        # *   true: Returns both system calendars and user-defined calendars.
        self.fetch_system_calendar = fetch_system_calendar
        # The maximum number of entries to return on this call. The default value is 20.
        self.max_results = max_results
        # A token that specifies the starting position for retrieving the next page of data. You do not need to provide this parameter for the first request. An empty value indicates that all data has been read.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The year.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_name is not None:
            result['CalendarName'] = self.calendar_name

        if self.fetch_calendar_detail is not None:
            result['FetchCalendarDetail'] = self.fetch_calendar_detail

        if self.fetch_system_calendar is not None:
            result['FetchSystemCalendar'] = self.fetch_system_calendar

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarName') is not None:
            self.calendar_name = m.get('CalendarName')

        if m.get('FetchCalendarDetail') is not None:
            self.fetch_calendar_detail = m.get('FetchCalendarDetail')

        if m.get('FetchSystemCalendar') is not None:
            self.fetch_system_calendar = m.get('FetchSystemCalendar')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

