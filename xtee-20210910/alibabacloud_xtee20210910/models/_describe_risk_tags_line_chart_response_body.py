# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskTagsLineChartResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeRiskTagsLineChartResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code. Note: 200 indicates success.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object
        # Indicates whether the request was successful.
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
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeRiskTagsLineChartResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeRiskTagsLineChartResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        percent: List[float] = None,
        series: List[main_models.DescribeRiskTagsLineChartResponseBodyResultObjectSeries] = None,
        total: List[int] = None,
        xaxis: main_models.DescribeRiskTagsLineChartResponseBodyResultObjectXaxis = None,
    ):
        # Call percentage, represented as a decimal
        self.percent = percent
        # Chart data
        self.series = series
        # Total number of records.
        self.total = total
        # X-axis data of the chart
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
        if self.percent is not None:
            result['Percent'] = self.percent

        result['Series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['Series'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        if self.xaxis is not None:
            result['Xaxis'] = self.xaxis.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        self.series = []
        if m.get('Series') is not None:
            for k1 in m.get('Series'):
                temp_model = main_models.DescribeRiskTagsLineChartResponseBodyResultObjectSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Xaxis') is not None:
            temp_model = main_models.DescribeRiskTagsLineChartResponseBodyResultObjectXaxis()
            self.xaxis = temp_model.from_map(m.get('Xaxis'))

        return self

class DescribeRiskTagsLineChartResponseBodyResultObjectXaxis(DaraModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        # Data returned by the chart
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

class DescribeRiskTagsLineChartResponseBodyResultObjectSeries(DaraModel):
    def __init__(
        self,
        data: float = None,
        name: str = None,
    ):
        # Data
        self.data = data
        # Name
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

