# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceEventResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.DescribeServiceEventResponseBodyEvents] = None,
        page_num: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page_num: int = None,
    ):
        # The events.
        self.events = events
        # The page number.
        self.page_num = page_num
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The total number of pages returned.
        self.total_page_num = total_page_num

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

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.DescribeServiceEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class DescribeServiceEventResponseBodyEvents(DaraModel):
    def __init__(
        self,
        message: str = None,
        reason: str = None,
        time: str = None,
        type: str = None,
    ):
        # The returned message. The message is formatted and returned in the JSON format.
        self.message = message
        # The cause of the event. The information about the change in the service status is returned.
        self.reason = reason
        # The time when the event occurred. The time must be in UTC.
        self.time = time
        # The event type. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

