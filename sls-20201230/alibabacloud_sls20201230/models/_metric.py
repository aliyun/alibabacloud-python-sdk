# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Metric(DaraModel):
    def __init__(
        self,
        aggregator: str = None,
        data_format: str = None,
        description: str = None,
        display_name: str = None,
        generator: str = None,
        golden_metric: bool = None,
        interval_us: List[int] = None,
        name: str = None,
        query_mode: str = None,
        type: str = None,
        unit: str = None,
    ):
        # The aggregation method of the metric (such as avg or sum). If the metric is already aggregated by the same dimensions (such as avg(rate(cpu_core_usage_seconds_total{}[1m]))), configuration is not required. Metrics based on log aggregation generally do not require configuration either.
        self.aggregator = aggregator
        # The numeric or display formatting method, such as KMB (thousand/million/billion), percent, ms, or dthms (hours:minutes:seconds).
        self.data_format = data_format
        # The business description of the metric.
        self.description = description
        # The display name for UI presentation, which can contain Chinese characters.
        self.display_name = display_name
        # The generation method of the metric. In PromQL mode, this is a PromQL expression (such as rate(request_count{}[1m]), which can be combined with aggregator to compute sum(...) by (label1, label2)). In SQL/SPL mode, this is an aggregation expression (such as count(1)) that is incorporated into the generated query statement.
        self.generator = generator
        # Indicates whether the metric is a golden metric (core metrics such as latency, traffic, error count, and saturation).
        self.golden_metric = golden_metric
        # The collection interval of the metric in microseconds. Multiple values indicate that multiple collection interval precisions are supported.
        self.interval_us = interval_us
        # The metric name, which is unique within the MetricSet.
        self.name = name
        # The expected query mode of the metric: range (range query), instant (instant query), or both.
        self.query_mode = query_mode
        # The metric type. Metrics that do not require secondary processing are fixed as gauge.
        self.type = type
        # The metric unit, which is used for display only without automatic conversion. For example, ms is not automatically converted to s.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator is not None:
            result['aggregator'] = self.aggregator

        if self.data_format is not None:
            result['data_format'] = self.data_format

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['display_name'] = self.display_name

        if self.generator is not None:
            result['generator'] = self.generator

        if self.golden_metric is not None:
            result['golden_metric'] = self.golden_metric

        if self.interval_us is not None:
            result['interval_us'] = self.interval_us

        if self.name is not None:
            result['name'] = self.name

        if self.query_mode is not None:
            result['query_mode'] = self.query_mode

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregator') is not None:
            self.aggregator = m.get('aggregator')

        if m.get('data_format') is not None:
            self.data_format = m.get('data_format')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        if m.get('generator') is not None:
            self.generator = m.get('generator')

        if m.get('golden_metric') is not None:
            self.golden_metric = m.get('golden_metric')

        if m.get('interval_us') is not None:
            self.interval_us = m.get('interval_us')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('query_mode') is not None:
            self.query_mode = m.get('query_mode')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

