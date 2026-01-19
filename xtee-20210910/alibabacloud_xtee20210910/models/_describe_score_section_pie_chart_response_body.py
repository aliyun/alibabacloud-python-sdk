# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeScoreSectionPieChartResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeScoreSectionPieChartResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeScoreSectionPieChartResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeScoreSectionPieChartResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        animation: bool = None,
        grid: main_models.DescribeScoreSectionPieChartResponseBodyResultObjectGrid = None,
        series: List[main_models.DescribeScoreSectionPieChartResponseBodyResultObjectSeries] = None,
    ):
        # Chart field, default true
        self.animation = animation
        # Belongs to grid.
        self.grid = grid
        # Data list
        self.series = series

    def validate(self):
        if self.grid:
            self.grid.validate()
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.animation is not None:
            result['animation'] = self.animation

        if self.grid is not None:
            result['grid'] = self.grid.to_map()

        result['series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('animation') is not None:
            self.animation = m.get('animation')

        if m.get('grid') is not None:
            temp_model = main_models.DescribeScoreSectionPieChartResponseBodyResultObjectGrid()
            self.grid = temp_model.from_map(m.get('grid'))

        self.series = []
        if m.get('series') is not None:
            for k1 in m.get('series'):
                temp_model = main_models.DescribeScoreSectionPieChartResponseBodyResultObjectSeries()
                self.series.append(temp_model.from_map(k1))

        return self

class DescribeScoreSectionPieChartResponseBodyResultObjectSeries(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeScoreSectionPieChartResponseBodyResultObjectSeriesData] = None,
        name: str = None,
        rose_type: bool = None,
    ):
        # Chart data list
        self.data = data
        # Category name.
        self.name = name
        # Chart field, default false
        self.rose_type = rose_type

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.rose_type is not None:
            result['roseType'] = self.rose_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeScoreSectionPieChartResponseBodyResultObjectSeriesData()
                self.data.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('roseType') is not None:
            self.rose_type = m.get('roseType')

        return self

class DescribeScoreSectionPieChartResponseBodyResultObjectSeriesData(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # Category item name.
        self.name = name
        # Result value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeScoreSectionPieChartResponseBodyResultObjectGrid(DaraModel):
    def __init__(
        self,
        show: bool = None,
    ):
        # Chart field, default false
        self.show = show

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show is not None:
            result['show'] = self.show

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('show') is not None:
            self.show = m.get('show')

        return self

