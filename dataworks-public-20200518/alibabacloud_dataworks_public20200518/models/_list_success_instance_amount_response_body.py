# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListSuccessInstanceAmountResponseBody(DaraModel):
    def __init__(
        self,
        instance_status_trend: main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrend = None,
        request_id: str = None,
    ):
        # The trend data of successfully completed instance counts at different hours on the business date.
        self.instance_status_trend = instance_status_trend
        # The request ID. You can use this ID to troubleshoot issues.
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
            temp_model = main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrend()
            self.instance_status_trend = temp_model.from_map(m.get('InstanceStatusTrend'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSuccessInstanceAmountResponseBodyInstanceStatusTrend(DaraModel):
    def __init__(
        self,
        avg_trend: List[main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrendAvgTrend] = None,
        today_trend: List[main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrendTodayTrend] = None,
        yesterday_trend: List[main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrendYesterdayTrend] = None,
    ):
        # The historical average trend.
        self.avg_trend = avg_trend
        # The trend for the current business date.
        self.today_trend = today_trend
        # The trend for the day before the business date.
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
                temp_model = main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrendAvgTrend()
                self.avg_trend.append(temp_model.from_map(k1))

        self.today_trend = []
        if m.get('TodayTrend') is not None:
            for k1 in m.get('TodayTrend'):
                temp_model = main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrendTodayTrend()
                self.today_trend.append(temp_model.from_map(k1))

        self.yesterday_trend = []
        if m.get('YesterdayTrend') is not None:
            for k1 in m.get('YesterdayTrend'):
                temp_model = main_models.ListSuccessInstanceAmountResponseBodyInstanceStatusTrendYesterdayTrend()
                self.yesterday_trend.append(temp_model.from_map(k1))

        return self

class ListSuccessInstanceAmountResponseBodyInstanceStatusTrendYesterdayTrend(DaraModel):
    def __init__(
        self,
        count: int = None,
        time_point: str = None,
    ):
        # The number of successfully completed instances.
        self.count = count
        # The time point. Valid values: hours on the hour from 00:00 to 23:00, such as 00:00, 01:00, and 02:00.
        # 
        # Format: `HH:mm`. Example: `01:00`.
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

class ListSuccessInstanceAmountResponseBodyInstanceStatusTrendTodayTrend(DaraModel):
    def __init__(
        self,
        count: int = None,
        time_point: str = None,
    ):
        # The number of successfully completed instances.
        self.count = count
        # The time point. Valid values: hours on the hour from 00:00 to 23:00, such as 00:00, 01:00, and 02:00.
        # 
        # Format: `HH:mm`. Example: `01:00`.
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

class ListSuccessInstanceAmountResponseBodyInstanceStatusTrendAvgTrend(DaraModel):
    def __init__(
        self,
        count: int = None,
        time_point: str = None,
    ):
        # The number of successfully completed instances.
        self.count = count
        # The time point. Valid values: hours on the hour from 00:00 to 23:00, such as 00:00, 01:00, and 02:00.
        # 
        # Format: `HH:mm`. Example: `01:00`.
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

