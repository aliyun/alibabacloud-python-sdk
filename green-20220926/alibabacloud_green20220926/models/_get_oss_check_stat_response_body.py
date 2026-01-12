# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetOssCheckStatResponseBody(DaraModel):
    def __init__(
        self,
        bar_chart: main_models.GetOssCheckStatResponseBodyBarChart = None,
        request_id: str = None,
    ):
        # Bar chart
        self.bar_chart = bar_chart
        # ID assigned by the backend, used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.bar_chart:
            self.bar_chart.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bar_chart is not None:
            result['BarChart'] = self.bar_chart.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BarChart') is not None:
            temp_model = main_models.GetOssCheckStatResponseBodyBarChart()
            self.bar_chart = temp_model.from_map(m.get('BarChart'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetOssCheckStatResponseBodyBarChart(DaraModel):
    def __init__(
        self,
        x: List[str] = None,
        y: List[main_models.GetOssCheckStatResponseBodyBarChartY] = None,
    ):
        # X values of the coordinates.
        self.x = x
        # Y values of the coordinates.
        self.y = y

    def validate(self):
        if self.y:
            for v1 in self.y:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        result['Y'] = []
        if self.y is not None:
            for k1 in self.y:
                result['Y'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        self.y = []
        if m.get('Y') is not None:
            for k1 in m.get('Y'):
                temp_model = main_models.GetOssCheckStatResponseBodyBarChartY()
                self.y.append(temp_model.from_map(k1))

        return self

class GetOssCheckStatResponseBodyBarChartY(DaraModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        # Data.
        self.data = data
        # Name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

