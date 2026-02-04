# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListTrafficStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_statistics: List[main_models.ListTrafficStatisticsResponseBodyTrafficStatistics] = None,
    ):
        self.request_id = request_id
        self.traffic_statistics = traffic_statistics

    def validate(self):
        if self.traffic_statistics:
            for v1 in self.traffic_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TrafficStatistics'] = []
        if self.traffic_statistics is not None:
            for k1 in self.traffic_statistics:
                result['TrafficStatistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.traffic_statistics = []
        if m.get('TrafficStatistics') is not None:
            for k1 in m.get('TrafficStatistics'):
                temp_model = main_models.ListTrafficStatisticsResponseBodyTrafficStatistics()
                self.traffic_statistics.append(temp_model.from_map(k1))

        return self

class ListTrafficStatisticsResponseBodyTrafficStatistics(DaraModel):
    def __init__(
        self,
        traffic_statistic_data: List[main_models.ListTrafficStatisticsResponseBodyTrafficStatisticsTrafficStatisticData] = None,
        traffic_statistic_target: str = None,
    ):
        self.traffic_statistic_data = traffic_statistic_data
        self.traffic_statistic_target = traffic_statistic_target

    def validate(self):
        if self.traffic_statistic_data:
            for v1 in self.traffic_statistic_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TrafficStatisticData'] = []
        if self.traffic_statistic_data is not None:
            for k1 in self.traffic_statistic_data:
                result['TrafficStatisticData'].append(k1.to_map() if k1 else None)

        if self.traffic_statistic_target is not None:
            result['TrafficStatisticTarget'] = self.traffic_statistic_target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_statistic_data = []
        if m.get('TrafficStatisticData') is not None:
            for k1 in m.get('TrafficStatisticData'):
                temp_model = main_models.ListTrafficStatisticsResponseBodyTrafficStatisticsTrafficStatisticData()
                self.traffic_statistic_data.append(temp_model.from_map(k1))

        if m.get('TrafficStatisticTarget') is not None:
            self.traffic_statistic_target = m.get('TrafficStatisticTarget')

        return self

class ListTrafficStatisticsResponseBodyTrafficStatisticsTrafficStatisticData(DaraModel):
    def __init__(
        self,
        traffic_statistic_time: int = None,
        traffic_statistic_value: float = None,
    ):
        self.traffic_statistic_time = traffic_statistic_time
        self.traffic_statistic_value = traffic_statistic_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic_statistic_time is not None:
            result['TrafficStatisticTime'] = self.traffic_statistic_time

        if self.traffic_statistic_value is not None:
            result['TrafficStatisticValue'] = self.traffic_statistic_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficStatisticTime') is not None:
            self.traffic_statistic_time = m.get('TrafficStatisticTime')

        if m.get('TrafficStatisticValue') is not None:
            self.traffic_statistic_value = m.get('TrafficStatisticValue')

        return self

