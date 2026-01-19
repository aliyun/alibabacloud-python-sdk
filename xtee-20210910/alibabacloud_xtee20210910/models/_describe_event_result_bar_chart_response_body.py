# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventResultBarChartResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeEventResultBarChartResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned object
        self.result_object = result_object
        # Whether the request was successful.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeEventResultBarChartResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DescribeEventResultBarChartResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        series: List[main_models.DescribeEventResultBarChartResponseBodyResultObjectSeries] = None,
        xaxis: main_models.DescribeEventResultBarChartResponseBodyResultObjectXaxis = None,
    ):
        # Chart data
        self.series = series
        # xaxis interface configuration.
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
                temp_model = main_models.DescribeEventResultBarChartResponseBodyResultObjectSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('xaxis') is not None:
            temp_model = main_models.DescribeEventResultBarChartResponseBodyResultObjectXaxis()
            self.xaxis = temp_model.from_map(m.get('xaxis'))

        return self

class DescribeEventResultBarChartResponseBodyResultObjectXaxis(DaraModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        # Returned data object
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

class DescribeEventResultBarChartResponseBodyResultObjectSeries(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeEventResultBarChartResponseBodyResultObjectSeriesData] = None,
        name: str = None,
        stack: str = None,
    ):
        # Returned data object
        self.data = data
        # Series name.
        self.name = name
        # Label key
        self.stack = stack

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

        if self.stack is not None:
            result['stack'] = self.stack

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeEventResultBarChartResponseBodyResultObjectSeriesData()
                self.data.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('stack') is not None:
            self.stack = m.get('stack')

        return self

class DescribeEventResultBarChartResponseBodyResultObjectSeriesData(DaraModel):
    def __init__(
        self,
        num: int = None,
        scale: str = None,
    ):
        # Number.
        self.num = num
        # Scale
        self.scale = scale

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.num is not None:
            result['num'] = self.num

        if self.scale is not None:
            result['scale'] = self.scale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('num') is not None:
            self.num = m.get('num')

        if m.get('scale') is not None:
            self.scale = m.get('scale')

        return self

