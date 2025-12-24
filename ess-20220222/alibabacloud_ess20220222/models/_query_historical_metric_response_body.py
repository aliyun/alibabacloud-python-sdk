# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class QueryHistoricalMetricResponseBody(DaraModel):
    def __init__(
        self,
        historical_metrics: main_models.QueryHistoricalMetricResponseBodyHistoricalMetrics = None,
        request_id: str = None,
    ):
        self.historical_metrics = historical_metrics
        self.request_id = request_id

    def validate(self):
        if self.historical_metrics:
            self.historical_metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.historical_metrics is not None:
            result['HistoricalMetrics'] = self.historical_metrics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoricalMetrics') is not None:
            temp_model = main_models.QueryHistoricalMetricResponseBodyHistoricalMetrics()
            self.historical_metrics = temp_model.from_map(m.get('HistoricalMetrics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryHistoricalMetricResponseBodyHistoricalMetrics(DaraModel):
    def __init__(
        self,
        historical_metric: List[main_models.QueryHistoricalMetricResponseBodyHistoricalMetricsHistoricalMetric] = None,
    ):
        self.historical_metric = historical_metric

    def validate(self):
        if self.historical_metric:
            for v1 in self.historical_metric:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HistoricalMetric'] = []
        if self.historical_metric is not None:
            for k1 in self.historical_metric:
                result['HistoricalMetric'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.historical_metric = []
        if m.get('HistoricalMetric') is not None:
            for k1 in m.get('HistoricalMetric'):
                temp_model = main_models.QueryHistoricalMetricResponseBodyHistoricalMetricsHistoricalMetric()
                self.historical_metric.append(temp_model.from_map(k1))

        return self

class QueryHistoricalMetricResponseBodyHistoricalMetricsHistoricalMetric(DaraModel):
    def __init__(
        self,
        metric_value: str = None,
        time: str = None,
    ):
        self.metric_value = metric_value
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

