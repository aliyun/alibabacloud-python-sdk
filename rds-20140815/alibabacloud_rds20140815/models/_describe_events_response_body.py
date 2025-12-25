# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeEventsResponseBody(DaraModel):
    def __init__(
        self,
        event_items: main_models.DescribeEventsResponseBodyEventItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The events.
        self.event_items = event_items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.event_items:
            self.event_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_items is not None:
            result['EventItems'] = self.event_items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventItems') is not None:
            temp_model = main_models.DescribeEventsResponseBodyEventItems()
            self.event_items = temp_model.from_map(m.get('EventItems'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeEventsResponseBodyEventItems(DaraModel):
    def __init__(
        self,
        event_items: List[main_models.DescribeEventsResponseBodyEventItemsEventItems] = None,
    ):
        self.event_items = event_items

    def validate(self):
        if self.event_items:
            for v1 in self.event_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventItems'] = []
        if self.event_items is not None:
            for k1 in self.event_items:
                result['EventItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_items = []
        if m.get('EventItems') is not None:
            for k1 in m.get('EventItems'):
                temp_model = main_models.DescribeEventsResponseBodyEventItemsEventItems()
                self.event_items.append(temp_model.from_map(k1))

        return self

class DescribeEventsResponseBodyEventItemsEventItems(DaraModel):
    def __init__(
        self,
        caller_uid: int = None,
        event_id: int = None,
        event_name: str = None,
        event_payload: str = None,
        event_reason: str = None,
        event_record_time: str = None,
        event_time: str = None,
        event_type: str = None,
        event_user_type: str = None,
        region_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The ID of the user who executed the event.
        self.caller_uid = caller_uid
        # The event ID.
        self.event_id = event_id
        # The event name.
        self.event_name = event_name
        # The request or context parameters of the event.
        self.event_payload = event_payload
        # The source of the event.
        self.event_reason = event_reason
        # The time when the event was recorded. The time is slightly later than the time the event occurred.
        self.event_record_time = event_record_time
        # The time when the event occurred.
        self.event_time = event_time
        # The event type.
        self.event_type = event_type
        # The type of the user who executed the event.
        self.event_user_type = event_user_type
        # The region ID.
        self.region_id = region_id
        # The name of the resource associated with the event. Only instance IDs are supported for this parameter.
        self.resource_name = resource_name
        # The type of the resource associated with the event. Only instances are supported for this parameter.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_payload is not None:
            result['EventPayload'] = self.event_payload

        if self.event_reason is not None:
            result['EventReason'] = self.event_reason

        if self.event_record_time is not None:
            result['EventRecordTime'] = self.event_record_time

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.event_user_type is not None:
            result['EventUserType'] = self.event_user_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventPayload') is not None:
            self.event_payload = m.get('EventPayload')

        if m.get('EventReason') is not None:
            self.event_reason = m.get('EventReason')

        if m.get('EventRecordTime') is not None:
            self.event_record_time = m.get('EventRecordTime')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('EventUserType') is not None:
            self.event_user_type = m.get('EventUserType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

