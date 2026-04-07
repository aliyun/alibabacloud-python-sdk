# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetSuccessInstanceTrendResponseBody(DaraModel):
    def __init__(
        self,
        instance_status_trend: main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrend = None,
        request_id: str = None,
    ):
        # The trend of statistics on the instance status in different time periods.
        self.instance_status_trend = instance_status_trend
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_status_trend:
            self.instance_status_trend.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_status_trend is not None:
            result['InstanceStatusTrend'] = self.instance_status_trend.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceStatusTrend') is not None:
            temp_model = main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrend()
            self.instance_status_trend = temp_model.from_map(m.get('InstanceStatusTrend'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSuccessInstanceTrendResponseBodyInstanceStatusTrend(DaraModel):
    def __init__(
        self,
        avg_trend: List[main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrendAvgTrend] = None,
        today_trend: List[main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrendTodayTrend] = None,
        yesterday_trend: List[main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrendYesterdayTrend] = None,
    ):
        # The average trend.
        self.avg_trend = avg_trend
        # The trend on the current day.
        self.today_trend = today_trend
        # The trend on the previous day.
        self.yesterday_trend = yesterday_trend

    def validate(self):
        if self.avg_trend:
            for v1 in self.avg_trend:
                 if v1:
                    v1.validate()
        if self.today_trend:
            for v1 in self.today_trend:
                 if v1:
                    v1.validate()
        if self.yesterday_trend:
            for v1 in self.yesterday_trend:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvgTrend'] = []
        if self.avg_trend is not None:
            for k1 in self.avg_trend:
                result['AvgTrend'].append(k1.to_map() if k1 else None)

        result['TodayTrend'] = []
        if self.today_trend is not None:
            for k1 in self.today_trend:
                result['TodayTrend'].append(k1.to_map() if k1 else None)

        result['YesterdayTrend'] = []
        if self.yesterday_trend is not None:
            for k1 in self.yesterday_trend:
                result['YesterdayTrend'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.avg_trend = []
        if m.get('AvgTrend') is not None:
            for k1 in m.get('AvgTrend'):
                temp_model = main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrendAvgTrend()
                self.avg_trend.append(temp_model.from_map(k1))

        self.today_trend = []
        if m.get('TodayTrend') is not None:
            for k1 in m.get('TodayTrend'):
                temp_model = main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrendTodayTrend()
                self.today_trend.append(temp_model.from_map(k1))

        self.yesterday_trend = []
        if m.get('YesterdayTrend') is not None:
            for k1 in m.get('YesterdayTrend'):
                temp_model = main_models.GetSuccessInstanceTrendResponseBodyInstanceStatusTrendYesterdayTrend()
                self.yesterday_trend.append(temp_model.from_map(k1))

        return self

class GetSuccessInstanceTrendResponseBodyInstanceStatusTrendYesterdayTrend(DaraModel):
    def __init__(
        self,
        count: int = None,
        time_point: str = None,
    ):
        # The number of instances.
        self.count = count
        # The point in time. Valid values: 00:00 to 23:00.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

class GetSuccessInstanceTrendResponseBodyInstanceStatusTrendTodayTrend(DaraModel):
    def __init__(
        self,
        count: int = None,
        time_point: str = None,
    ):
        # The number of instances.
        self.count = count
        # The point in time. Valid values: 00:00 to 23:00.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

class GetSuccessInstanceTrendResponseBodyInstanceStatusTrendAvgTrend(DaraModel):
    def __init__(
        self,
        count: int = None,
        time_point: str = None,
    ):
        # The number of instances.
        self.count = count
        # The point in time. Valid values: 00:00 to 23:00.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

