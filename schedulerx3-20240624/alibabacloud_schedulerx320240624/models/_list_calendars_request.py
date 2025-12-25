# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCalendarsRequest(DaraModel):
    def __init__(
        self,
        calendar_name: str = None,
        cluster_id: str = None,
        fetch_calendar_detail: bool = None,
        max_results: int = None,
        next_token: str = None,
        year: int = None,
    ):
        self.calendar_name = calendar_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.fetch_calendar_detail = fetch_calendar_detail
        self.max_results = max_results
        self.next_token = next_token
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

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.fetch_calendar_detail is not None:
            result['FetchCalendarDetail'] = self.fetch_calendar_detail

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarName') is not None:
            self.calendar_name = m.get('CalendarName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('FetchCalendarDetail') is not None:
            self.fetch_calendar_detail = m.get('FetchCalendarDetail')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

