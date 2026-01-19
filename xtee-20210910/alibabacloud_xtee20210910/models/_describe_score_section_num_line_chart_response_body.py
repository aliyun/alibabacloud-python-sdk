# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeScoreSectionNumLineChartResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeScoreSectionNumLineChartResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object
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
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeScoreSectionNumLineChartResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeScoreSectionNumLineChartResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        series: List[main_models.DescribeScoreSectionNumLineChartResponseBodyResultObjectSeries] = None,
        xaxis: main_models.DescribeScoreSectionNumLineChartResponseBodyResultObjectXaxis = None,
    ):
        # Data list
        self.series = series
        # Details of xaxis node.
        self.xaxis = xaxis

    def validate(self):
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()
        if self.xaxis:
            self.xaxis.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        if self.xaxis is not None:
            result['xaxis'] = self.xaxis.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.series = []
        if m.get('series') is not None:
            for k1 in m.get('series'):
                temp_model = main_models.DescribeScoreSectionNumLineChartResponseBodyResultObjectSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('xaxis') is not None:
            temp_model = main_models.DescribeScoreSectionNumLineChartResponseBodyResultObjectXaxis()
            self.xaxis = temp_model.from_map(m.get('xaxis'))

        return self

class DescribeScoreSectionNumLineChartResponseBodyResultObjectXaxis(DaraModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        # Data structure.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        return self

class DescribeScoreSectionNumLineChartResponseBodyResultObjectSeries(DaraModel):
    def __init__(
        self,
        data: List[str] = None,
        name: str = None,
    ):
        # List of current category results.
        self.data = data
        # Category name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

