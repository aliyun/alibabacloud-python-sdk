# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSystemEventHistogramRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_type: str = None,
        group_id: str = None,
        level: str = None,
        name: str = None,
        product: str = None,
        region_id: str = None,
        search_keywords: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The end time.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The event type.
        # 
        # >  You can call the [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html) operation to query the types of system events.
        self.event_type = event_type
        # The ID of the application group.
        self.group_id = group_id
        # The level of the event. Valid values:
        # 
        # *   CRITICAL
        # *   WARN
        # *   INFO
        self.level = level
        # The event name.
        # 
        # >  You can call the [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html) operation to query the names of system events.
        self.name = name
        # The abbreviation of the service name.
        # 
        # >  You can call the [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html) operation to query the abbreviations of service names.
        self.product = product
        self.region_id = region_id
        # The keywords that are used to search for the system event. Valid values:
        # 
        # *   If you want to search for the system event whose content contains a and b, set the value to `a and b`.
        # *   If you want to search for the system event whose content contains a or b, set the value to `a or b`.
        self.search_keywords = search_keywords
        # The start time.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The event status.
        # 
        # >  You can call the [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html) operation to query the status of system events.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_keywords is not None:
            result['SearchKeywords'] = self.search_keywords

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchKeywords') is not None:
            self.search_keywords = m.get('SearchKeywords')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

