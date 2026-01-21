# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class MetricStat(DaraModel):
    def __init__(
        self,
        associated: Dict[str, str] = None,
        dimensions: List[main_models.Dimension] = None,
        log_time: int = None,
        measurements: Dict[str, Any] = None,
        metric: str = None,
        namespace: str = None,
        period: int = None,
        timestamp: int = None,
    ):
        self.associated = associated
        self.dimensions = dimensions
        self.log_time = log_time
        self.measurements = measurements
        self.metric = metric
        self.namespace = namespace
        self.period = period
        self.timestamp = timestamp

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated is not None:
            result['Associated'] = self.associated

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.measurements is not None:
            result['Measurements'] = self.measurements

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.period is not None:
            result['Period'] = self.period

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Associated') is not None:
            self.associated = m.get('Associated')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.Dimension()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('Measurements') is not None:
            self.measurements = m.get('Measurements')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

