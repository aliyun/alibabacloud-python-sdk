# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class CostQueryTrendDTO(DaraModel):
    def __init__(
        self,
        default_metric: str = None,
        granularity: str = None,
        metrics: List[main_models.MetricDefRespDTO] = None,
        points: List[main_models.TrendPointDTO] = None,
    ):
        self.default_metric = default_metric
        self.granularity = granularity
        self.metrics = metrics
        self.points = points

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.points:
            for v1 in self.points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_metric is not None:
            result['defaultMetric'] = self.default_metric

        if self.granularity is not None:
            result['granularity'] = self.granularity

        result['metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['metrics'].append(k1.to_map() if k1 else None)

        result['points'] = []
        if self.points is not None:
            for k1 in self.points:
                result['points'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultMetric') is not None:
            self.default_metric = m.get('defaultMetric')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        self.metrics = []
        if m.get('metrics') is not None:
            for k1 in m.get('metrics'):
                temp_model = main_models.MetricDefRespDTO()
                self.metrics.append(temp_model.from_map(k1))

        self.points = []
        if m.get('points') is not None:
            for k1 in m.get('points'):
                temp_model = main_models.TrendPointDTO()
                self.points.append(temp_model.from_map(k1))

        return self

