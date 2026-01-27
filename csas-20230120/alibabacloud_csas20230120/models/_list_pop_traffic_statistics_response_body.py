# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListPopTrafficStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_data: List[main_models.ListPopTrafficStatisticsResponseBodyTrafficData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.traffic_data = traffic_data

    def validate(self):
        if self.traffic_data:
            for v1 in self.traffic_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TrafficData'] = []
        if self.traffic_data is not None:
            for k1 in self.traffic_data:
                result['TrafficData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.traffic_data = []
        if m.get('TrafficData') is not None:
            for k1 in m.get('TrafficData'):
                temp_model = main_models.ListPopTrafficStatisticsResponseBodyTrafficData()
                self.traffic_data.append(temp_model.from_map(k1))

        return self

class ListPopTrafficStatisticsResponseBodyTrafficData(DaraModel):
    def __init__(
        self,
        datapoints: List[main_models.ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints] = None,
        metric_name: str = None,
    ):
        self.datapoints = datapoints
        self.metric_name = metric_name

    def validate(self):
        if self.datapoints:
            for v1 in self.datapoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Datapoints'] = []
        if self.datapoints is not None:
            for k1 in self.datapoints:
                result['Datapoints'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datapoints = []
        if m.get('Datapoints') is not None:
            for k1 in m.get('Datapoints'):
                temp_model = main_models.ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints()
                self.datapoints.append(temp_model.from_map(k1))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        return self

class ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints(DaraModel):
    def __init__(
        self,
        average: float = None,
        date_time: str = None,
    ):
        self.average = average
        self.date_time = date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average is not None:
            result['Average'] = self.average

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        return self

