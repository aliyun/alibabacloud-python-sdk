# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeUserEventTrendResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trend: List[main_models.DescribeUserEventTrendResponseBodyTrend] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The trends of attacks.
        self.trend = trend

    def validate(self):
        if self.trend:
            for v1 in self.trend:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Trend'] = []
        if self.trend is not None:
            for k1 in self.trend:
                result['Trend'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.trend = []
        if m.get('Trend') is not None:
            for k1 in m.get('Trend'):
                temp_model = main_models.DescribeUserEventTrendResponseBodyTrend()
                self.trend.append(temp_model.from_map(k1))

        return self

class DescribeUserEventTrendResponseBodyTrend(DaraModel):
    def __init__(
        self,
        event_high: int = None,
        event_low: int = None,
        event_medium: int = None,
        time_stamp: int = None,
        timestamp: int = None,
    ):
        # The number of high-risk events.
        self.event_high = event_high
        # The number of low-risk events.
        self.event_low = event_low
        # The number of medium-risk events.
        self.event_medium = event_medium
        # The time at which the API was called. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        # >Notice: The parameter has been deprecated, it is recommended to use the Timestamp parameter.
        self.time_stamp = time_stamp
        # The time at which the API was called. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.timestamp = timestamp

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

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventHigh') is not None:
            self.event_high = m.get('EventHigh')

        if m.get('EventLow') is not None:
            self.event_low = m.get('EventLow')

        if m.get('EventMedium') is not None:
            self.event_medium = m.get('EventMedium')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

