# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSystemEventCountRequest(DaraModel):
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
        # The timestamp of the end time for the event query. Unit: milliseconds.
        self.end_time = end_time
        # The event type.
        # 
        # Call the DescribeSystemEventMetaList operation to obtain the value of the `EventType` response parameter, which provides the event types for all Alibaba Cloud services under the current Alibaba Cloud account. For more information, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
        self.event_type = event_type
        # The application group ID.
        self.group_id = group_id
        # The event level. Valid values:
        # 
        # - Critical: critical.
        # 
        # - Warn: warning.
        # 
        # - Info: information.
        # 
        # Call the DescribeSystemEventMetaList operation to obtain the value of the `Level` response parameter, which provides the event levels for all Alibaba Cloud services under the current Alibaba Cloud account. For more information, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
        self.level = level
        # The event name.
        # 
        # Call the DescribeSystemEventMetaList operation to obtain the value of the `Name` response parameter, which provides the event names for all Alibaba Cloud services under the current Alibaba Cloud account. For more information, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
        self.name = name
        # The name of the Alibaba Cloud service.
        # 
        # Call the DescribeSystemEventMetaList operation to obtain the value of the `Product` response parameter, which provides the Alibaba Cloud service names for all events under the current Alibaba Cloud account. For more information, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
        self.product = product
        self.region_id = region_id
        # The keywords contained in the event content for searching. Valid values:
        # 
        # - To search for event content that contains both a and b, search for `a and b`.
        # 
        # - To search for event content that contains either a or b, search for `a or b`.
        self.search_keywords = search_keywords
        # The timestamp of the start time for the event query. Unit: milliseconds.
        self.start_time = start_time
        # The event status.
        # 
        # Call the DescribeSystemEventMetaList operation to obtain the value of the `Status` response parameter, which provides the event statuses for all Alibaba Cloud services under the current Alibaba Cloud account. For more information, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
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

