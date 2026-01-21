# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomEventCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        custom_event_counts: main_models.DescribeCustomEventCountResponseBodyCustomEventCounts = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The details of the custom event.
        self.custom_event_counts = custom_event_counts
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.custom_event_counts:
            self.custom_event_counts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.custom_event_counts is not None:
            result['CustomEventCounts'] = self.custom_event_counts.to_map()

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

        if m.get('CustomEventCounts') is not None:
            temp_model = main_models.DescribeCustomEventCountResponseBodyCustomEventCounts()
            self.custom_event_counts = temp_model.from_map(m.get('CustomEventCounts'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomEventCountResponseBodyCustomEventCounts(DaraModel):
    def __init__(
        self,
        custom_event_count: List[main_models.DescribeCustomEventCountResponseBodyCustomEventCountsCustomEventCount] = None,
    ):
        self.custom_event_count = custom_event_count

    def validate(self):
        if self.custom_event_count:
            for v1 in self.custom_event_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomEventCount'] = []
        if self.custom_event_count is not None:
            for k1 in self.custom_event_count:
                result['CustomEventCount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_event_count = []
        if m.get('CustomEventCount') is not None:
            for k1 in m.get('CustomEventCount'):
                temp_model = main_models.DescribeCustomEventCountResponseBodyCustomEventCountsCustomEventCount()
                self.custom_event_count.append(temp_model.from_map(k1))

        return self

class DescribeCustomEventCountResponseBodyCustomEventCountsCustomEventCount(DaraModel):
    def __init__(
        self,
        name: str = None,
        num: int = None,
        time: int = None,
    ):
        # The event name.
        self.name = name
        # The number of times that the custom event occurred.
        self.num = num
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
        if self.name is not None:
            result['Name'] = self.name

        if self.num is not None:
            result['Num'] = self.num

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

