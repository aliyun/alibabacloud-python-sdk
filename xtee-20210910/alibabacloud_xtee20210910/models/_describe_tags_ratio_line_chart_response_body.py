# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeTagsRatioLineChartResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeTagsRatioLineChartResponseBodyResultObject = None,
    ):
        # Request ID
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
            temp_model = main_models.DescribeTagsRatioLineChartResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeTagsRatioLineChartResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        series: List[main_models.DescribeTagsRatioLineChartResponseBodyResultObjectSeries] = None,
        xaxis: main_models.DescribeTagsRatioLineChartResponseBodyResultObjectXaxis = None,
    ):
        # Data list
        self.series = series
        # xaxis node.
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
                temp_model = main_models.DescribeTagsRatioLineChartResponseBodyResultObjectSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('xaxis') is not None:
            temp_model = main_models.DescribeTagsRatioLineChartResponseBodyResultObjectXaxis()
            self.xaxis = temp_model.from_map(m.get('xaxis'))

        return self

class DescribeTagsRatioLineChartResponseBodyResultObjectXaxis(DaraModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        # X-axis data
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

class DescribeTagsRatioLineChartResponseBodyResultObjectSeries(DaraModel):
    def __init__(
        self,
        data: List[str] = None,
        name: str = None,
    ):
        # Result data.
        self.data = data
        # Series name.
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

