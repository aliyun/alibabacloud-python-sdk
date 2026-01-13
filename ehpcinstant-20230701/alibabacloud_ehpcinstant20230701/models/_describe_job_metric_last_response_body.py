# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class DescribeJobMetricLastResponseBody(DaraModel):
    def __init__(
        self,
        metrics: List[main_models.DescribeJobMetricLastResponseBodyMetrics] = None,
        request_id: str = None,
    ):
        # The list of the JobMetric details.
        self.metrics = metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.DescribeJobMetricLastResponseBodyMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeJobMetricLastResponseBodyMetrics(DaraModel):
    def __init__(
        self,
        array_index: int = None,
        metric: str = None,
    ):
        # The index of the array job.
        self.array_index = array_index
        # The monitoring item information corresponding to the array job index.
        self.metric = metric

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index

        if self.metric is not None:
            result['Metric'] = self.metric

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        return self

