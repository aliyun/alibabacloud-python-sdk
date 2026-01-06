# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class QueryTracedEventByEventIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryTracedEventByEventIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # Success: The request was successful.
        # 
        # Other codes: The request failed. For information about error codes, see Error codes.
        self.code = code
        # The total number of entries returned.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. If the operation was successful, the value true is returned.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryTracedEventByEventIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryTracedEventByEventIdResponseBodyData(DaraModel):
    def __init__(
        self,
        events: List[main_models.QueryTracedEventByEventIdResponseBodyDataEvents] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The events.
        self.events = events
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.QueryTracedEventByEventIdResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryTracedEventByEventIdResponseBodyDataEvents(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_received_time: int = None,
        event_source: str = None,
        event_type: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id
        # The time when the event was delivered to the event bus.
        self.event_received_time = event_received_time
        # The name of the event source.
        self.event_source = event_source
        # The event type.
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_received_time is not None:
            result['EventReceivedTime'] = self.event_received_time

        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.event_type is not None:
            result['EventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventReceivedTime') is not None:
            self.event_received_time = m.get('EventReceivedTime')

        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        return self

