# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridMonitorDataListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        time_series: List[main_models.DescribeHybridMonitorDataListResponseBodyTimeSeries] = None,
    ):
        # The response code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The returned monitoring data.
        self.time_series = time_series

    def validate(self):
        if self.time_series:
            for v1 in self.time_series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TimeSeries'] = []
        if self.time_series is not None:
            for k1 in self.time_series:
                result['TimeSeries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.time_series = []
        if m.get('TimeSeries') is not None:
            for k1 in m.get('TimeSeries'):
                temp_model = main_models.DescribeHybridMonitorDataListResponseBodyTimeSeries()
                self.time_series.append(temp_model.from_map(k1))

        return self

class DescribeHybridMonitorDataListResponseBodyTimeSeries(DaraModel):
    def __init__(
        self,
        labels: List[main_models.DescribeHybridMonitorDataListResponseBodyTimeSeriesLabels] = None,
        metric_name: str = None,
        values: List[main_models.DescribeHybridMonitorDataListResponseBodyTimeSeriesValues] = None,
    ):
        # The tags of the time dimension.
        self.labels = labels
        # The metric name.
        self.metric_name = metric_name
        # The metric values that are collected at different timestamps.
        self.values = values

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DescribeHybridMonitorDataListResponseBodyTimeSeriesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.DescribeHybridMonitorDataListResponseBodyTimeSeriesValues()
                self.values.append(temp_model.from_map(k1))

        return self

class DescribeHybridMonitorDataListResponseBodyTimeSeriesValues(DaraModel):
    def __init__(
        self,
        ts: str = None,
        v: str = None,
    ):
        # The timestamp that indicates the time when the metric value is collected.
        # 
        # Unit: seconds.
        self.ts = ts
        # The metric value.
        self.v = v

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ts is not None:
            result['Ts'] = self.ts

        if self.v is not None:
            result['V'] = self.v

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        if m.get('V') is not None:
            self.v = m.get('V')

        return self

class DescribeHybridMonitorDataListResponseBodyTimeSeriesLabels(DaraModel):
    def __init__(
        self,
        k: str = None,
        v: str = None,
    ):
        # The tag key.
        self.k = k
        # The tag value.
        self.v = v

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.k is not None:
            result['K'] = self.k

        if self.v is not None:
            result['V'] = self.v

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K') is not None:
            self.k = m.get('K')

        if m.get('V') is not None:
            self.v = m.get('V')

        return self

