# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEventTrendsResponseBody(DaraModel):
    def __init__(
        self,
        aggregate_interval: str = None,
        points: List[main_models.DescribeAiEngineEventTrendsResponseBodyPoints] = None,
        request_id: str = None,
    ):
        # The aggregation interval, which is automatically selected based on the query time range. Valid values:
        # 
        # - **1m**: 1 minute
        # - **5m**: 5 minutes
        # - **15m**: 15 minutes
        # - **1h**: 1 hour
        # - **1d**: 1 day
        self.aggregate_interval = aggregate_interval
        # The time series data of events aggregated by first discovery time, sorted in ascending order of time.
        self.points = points
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.points:
            for v1 in self.points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate_interval is not None:
            result['AggregateInterval'] = self.aggregate_interval

        result['Points'] = []
        if self.points is not None:
            for k1 in self.points:
                result['Points'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateInterval') is not None:
            self.aggregate_interval = m.get('AggregateInterval')

        self.points = []
        if m.get('Points') is not None:
            for k1 in m.get('Points'):
                temp_model = main_models.DescribeAiEngineEventTrendsResponseBodyPoints()
                self.points.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAiEngineEventTrendsResponseBodyPoints(DaraModel):
    def __init__(
        self,
        event_count: int = None,
        risk_counts: main_models.DescribeAiEngineEventTrendsResponseBodyPointsRiskCounts = None,
        time: int = None,
    ):
        # The number of events first discovered within the time period.
        self.event_count = event_count
        # The number of events within the time period, aggregated by risk level.
        self.risk_counts = risk_counts
        # The start time of the statistical period in the UNIX timestamp format. Unit: milliseconds.
        self.time = time

    def validate(self):
        if self.risk_counts:
            self.risk_counts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.risk_counts is not None:
            result['RiskCounts'] = self.risk_counts.to_map()

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('RiskCounts') is not None:
            temp_model = main_models.DescribeAiEngineEventTrendsResponseBodyPointsRiskCounts()
            self.risk_counts = temp_model.from_map(m.get('RiskCounts'))

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class DescribeAiEngineEventTrendsResponseBodyPointsRiskCounts(DaraModel):
    def __init__(
        self,
        critical: int = None,
        high: int = None,
        low: int = None,
        medium: int = None,
    ):
        # The number of critical events.
        self.critical = critical
        # The number of high-risk events.
        self.high = high
        # The number of low-risk events.
        self.low = low
        # The number of medium-risk events.
        self.medium = medium

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical

        if self.high is not None:
            result['High'] = self.high

        if self.low is not None:
            result['Low'] = self.low

        if self.medium is not None:
            result['Medium'] = self.medium

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            self.critical = m.get('Critical')

        if m.get('High') is not None:
            self.high = m.get('High')

        if m.get('Low') is not None:
            self.low = m.get('Low')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        return self

