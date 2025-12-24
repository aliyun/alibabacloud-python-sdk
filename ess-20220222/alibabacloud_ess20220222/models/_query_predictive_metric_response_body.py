# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class QueryPredictiveMetricResponseBody(DaraModel):
    def __init__(
        self,
        predictive_metrics: main_models.QueryPredictiveMetricResponseBodyPredictiveMetrics = None,
        request_id: str = None,
    ):
        self.predictive_metrics = predictive_metrics
        self.request_id = request_id

    def validate(self):
        if self.predictive_metrics:
            self.predictive_metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.predictive_metrics is not None:
            result['PredictiveMetrics'] = self.predictive_metrics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredictiveMetrics') is not None:
            temp_model = main_models.QueryPredictiveMetricResponseBodyPredictiveMetrics()
            self.predictive_metrics = temp_model.from_map(m.get('PredictiveMetrics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPredictiveMetricResponseBodyPredictiveMetrics(DaraModel):
    def __init__(
        self,
        predictive_metric: List[main_models.QueryPredictiveMetricResponseBodyPredictiveMetricsPredictiveMetric] = None,
    ):
        self.predictive_metric = predictive_metric

    def validate(self):
        if self.predictive_metric:
            for v1 in self.predictive_metric:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PredictiveMetric'] = []
        if self.predictive_metric is not None:
            for k1 in self.predictive_metric:
                result['PredictiveMetric'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predictive_metric = []
        if m.get('PredictiveMetric') is not None:
            for k1 in m.get('PredictiveMetric'):
                temp_model = main_models.QueryPredictiveMetricResponseBodyPredictiveMetricsPredictiveMetric()
                self.predictive_metric.append(temp_model.from_map(k1))

        return self

class QueryPredictiveMetricResponseBodyPredictiveMetricsPredictiveMetric(DaraModel):
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

