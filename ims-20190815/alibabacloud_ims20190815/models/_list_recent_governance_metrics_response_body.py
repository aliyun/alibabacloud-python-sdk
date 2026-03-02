# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListRecentGovernanceMetricsResponseBody(DaraModel):
    def __init__(
        self,
        generate_time: str = None,
        governance_metrics: main_models.ListRecentGovernanceMetricsResponseBodyGovernanceMetrics = None,
        request_id: str = None,
    ):
        # The time when the report was generated.
        self.generate_time = generate_time
        self.governance_metrics = governance_metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.governance_metrics:
            self.governance_metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_time is not None:
            result['GenerateTime'] = self.generate_time

        if self.governance_metrics is not None:
            result['GovernanceMetrics'] = self.governance_metrics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateTime') is not None:
            self.generate_time = m.get('GenerateTime')

        if m.get('GovernanceMetrics') is not None:
            temp_model = main_models.ListRecentGovernanceMetricsResponseBodyGovernanceMetrics()
            self.governance_metrics = temp_model.from_map(m.get('GovernanceMetrics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRecentGovernanceMetricsResponseBodyGovernanceMetrics(DaraModel):
    def __init__(
        self,
        governance_metric: List[main_models.ListRecentGovernanceMetricsResponseBodyGovernanceMetricsGovernanceMetric] = None,
    ):
        self.governance_metric = governance_metric

    def validate(self):
        if self.governance_metric:
            for v1 in self.governance_metric:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GovernanceMetric'] = []
        if self.governance_metric is not None:
            for k1 in self.governance_metric:
                result['GovernanceMetric'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.governance_metric = []
        if m.get('GovernanceMetric') is not None:
            for k1 in m.get('GovernanceMetric'):
                temp_model = main_models.ListRecentGovernanceMetricsResponseBodyGovernanceMetricsGovernanceMetric()
                self.governance_metric.append(temp_model.from_map(k1))

        return self

class ListRecentGovernanceMetricsResponseBodyGovernanceMetricsGovernanceMetric(DaraModel):
    def __init__(
        self,
        governance_item: str = None,
        metric_type: str = None,
        metric_value: Any = None,
    ):
        self.governance_item = governance_item
        self.metric_type = metric_type
        self.metric_value = metric_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.governance_item is not None:
            result['GovernanceItem'] = self.governance_item

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GovernanceItem') is not None:
            self.governance_item = m.get('GovernanceItem')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')

        return self

