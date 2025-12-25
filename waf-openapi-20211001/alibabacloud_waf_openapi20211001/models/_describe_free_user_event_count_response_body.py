# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeFreeUserEventCountResponseBody(DaraModel):
    def __init__(
        self,
        event: main_models.DescribeFreeUserEventCountResponseBodyEvent = None,
        request_id: str = None,
    ):
        # The information about the security events that are detected by using the basic detection feature.
        self.event = event
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.event:
            self.event.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            temp_model = main_models.DescribeFreeUserEventCountResponseBodyEvent()
            self.event = temp_model.from_map(m.get('Event'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFreeUserEventCountResponseBodyEvent(DaraModel):
    def __init__(
        self,
        event_high: int = None,
        event_low: int = None,
        event_medium: int = None,
        event_total: int = None,
    ):
        # The number of high-risk events.
        self.event_high = event_high
        # The number of low-risk events.
        self.event_low = event_low
        # The number of medium-risk events.
        self.event_medium = event_medium
        # The total number of security events.
        self.event_total = event_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_high is not None:
            result['EventHigh'] = self.event_high

        if self.event_low is not None:
            result['EventLow'] = self.event_low

        if self.event_medium is not None:
            result['EventMedium'] = self.event_medium

        if self.event_total is not None:
            result['EventTotal'] = self.event_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventHigh') is not None:
            self.event_high = m.get('EventHigh')

        if m.get('EventLow') is not None:
            self.event_low = m.get('EventLow')

        if m.get('EventMedium') is not None:
            self.event_medium = m.get('EventMedium')

        if m.get('EventTotal') is not None:
            self.event_total = m.get('EventTotal')

        return self

