# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class GetResolveStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        data_points: main_models.GetResolveStatisticsResponseBodyDataPoints = None,
        request_id: str = None,
    ):
        self.data_points = data_points
        self.request_id = request_id

    def validate(self):
        if self.data_points:
            self.data_points.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_points is not None:
            result['DataPoints'] = self.data_points.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPoints') is not None:
            temp_model = main_models.GetResolveStatisticsResponseBodyDataPoints()
            self.data_points = temp_model.from_map(m.get('DataPoints'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetResolveStatisticsResponseBodyDataPoints(DaraModel):
    def __init__(
        self,
        data_point: List[main_models.GetResolveStatisticsResponseBodyDataPointsDataPoint] = None,
    ):
        self.data_point = data_point

    def validate(self):
        if self.data_point:
            for v1 in self.data_point:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataPoint'] = []
        if self.data_point is not None:
            for k1 in self.data_point:
                result['DataPoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_point = []
        if m.get('DataPoint') is not None:
            for k1 in m.get('DataPoint'):
                temp_model = main_models.GetResolveStatisticsResponseBodyDataPointsDataPoint()
                self.data_point.append(temp_model.from_map(k1))

        return self

class GetResolveStatisticsResponseBodyDataPointsDataPoint(DaraModel):
    def __init__(
        self,
        count: int = None,
        time: int = None,
    ):
        self.count = count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

