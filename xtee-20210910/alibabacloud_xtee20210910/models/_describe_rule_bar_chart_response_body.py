# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleBarChartResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeRuleBarChartResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID.
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
            temp_model = main_models.DescribeRuleBarChartResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DescribeRuleBarChartResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        series: List[main_models.DescribeRuleBarChartResponseBodyResultObjectSeries] = None,
        yaxis: main_models.DescribeRuleBarChartResponseBodyResultObjectYaxis = None,
    ):
        # Data list
        self.series = series
        # yaxis related results.
        self.yaxis = yaxis

    def validate(self):
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()
        if self.yaxis:
            self.yaxis.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        if self.yaxis is not None:
            result['yaxis'] = self.yaxis.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.series = []
        if m.get('series') is not None:
            for k1 in m.get('series'):
                temp_model = main_models.DescribeRuleBarChartResponseBodyResultObjectSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('yaxis') is not None:
            temp_model = main_models.DescribeRuleBarChartResponseBodyResultObjectYaxis()
            self.yaxis = temp_model.from_map(m.get('yaxis'))

        return self

class DescribeRuleBarChartResponseBodyResultObjectYaxis(DaraModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        # yaxis data items
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

class DescribeRuleBarChartResponseBodyResultObjectSeries(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeRuleBarChartResponseBodyResultObjectSeriesData] = None,
        type: str = None,
    ):
        # Response data.
        self.data = data
        # Bar chart type
        self.type = type

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

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeRuleBarChartResponseBodyResultObjectSeriesData()
                self.data.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeRuleBarChartResponseBodyResultObjectSeriesData(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        num: int = None,
        rule_name: str = None,
        status: str = None,
    ):
        # Event name.
        self.event_name = event_name
        # Number.
        self.num = num
        # Policy name
        self.rule_name = rule_name
        # Status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.num is not None:
            result['num'] = self.num

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('num') is not None:
            self.num = m.get('num')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

