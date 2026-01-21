# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomEventAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        custom_events: main_models.DescribeCustomEventAttributeResponseBodyCustomEvents = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The event details.
        self.custom_events = custom_events
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.custom_events:
            self.custom_events.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.custom_events is not None:
            result['CustomEvents'] = self.custom_events.to_map()

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

        if m.get('CustomEvents') is not None:
            temp_model = main_models.DescribeCustomEventAttributeResponseBodyCustomEvents()
            self.custom_events = temp_model.from_map(m.get('CustomEvents'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomEventAttributeResponseBodyCustomEvents(DaraModel):
    def __init__(
        self,
        custom_event: List[main_models.DescribeCustomEventAttributeResponseBodyCustomEventsCustomEvent] = None,
    ):
        self.custom_event = custom_event

    def validate(self):
        if self.custom_event:
            for v1 in self.custom_event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomEvent'] = []
        if self.custom_event is not None:
            for k1 in self.custom_event:
                result['CustomEvent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_event = []
        if m.get('CustomEvent') is not None:
            for k1 in m.get('CustomEvent'):
                temp_model = main_models.DescribeCustomEventAttributeResponseBodyCustomEventsCustomEvent()
                self.custom_event.append(temp_model.from_map(k1))

        return self

class DescribeCustomEventAttributeResponseBodyCustomEventsCustomEvent(DaraModel):
    def __init__(
        self,
        content: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        time: str = None,
    ):
        # The content of the event.
        self.content = content
        # The ID of the application group.
        self.group_id = group_id
        # The event ID.
        self.id = id
        # The event name.
        self.name = name
        # The time when the event occurred.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

