# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomEventHistogramRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_id: str = None,
        group_id: str = None,
        level: str = None,
        name: str = None,
        region_id: str = None,
        search_keywords: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The event ID.
        self.event_id = event_id
        # The ID of the application group.
        self.group_id = group_id
        # The severity level of the event. Valid values:
        # 
        # *   CRITICAL
        # *   WARN
        # *   INFO
        self.level = level
        # The event name.
        self.name = name
        self.region_id = region_id
        # The keywords that are used to search for the event.
        # 
        # *   If you need to query the custom event whose content contains a and b, set the value to "a and b".
        # *   If you need to query the custom event whose content contains a or b, set the value to "a or b".
        self.search_keywords = search_keywords
        # The beginning of the time range to query.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_keywords is not None:
            result['SearchKeywords'] = self.search_keywords

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchKeywords') is not None:
            self.search_keywords = m.get('SearchKeywords')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

