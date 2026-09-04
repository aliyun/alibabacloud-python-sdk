# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class MetricSetSpec(DaraModel):
    def __init__(
        self,
        labels: main_models.MetricSetSpecLabels = None,
        metrics: List[main_models.Metric] = None,
        needs_processing: bool = None,
        query_type: str = None,
    ):
        # The label definitions for the metric set. Labels are recommended to be automatically generated using the dynamic method. MetricSet defines only common labels. Defining additional labels under individual Metrics is not recommended.
        self.labels = labels
        # The list of metrics included in the metric set.
        self.metrics = metrics
        # Specifies whether the metric requires secondary processing before use. For example, Prometheus counter/summary/histogram metrics require calculations such as rate before they can be used directly.
        self.needs_processing = needs_processing
        # The query syntax for the metrics. Valid values: prom (PromQL), spl, and cms (CloudMonitor).
        self.query_type = query_type

    def validate(self):
        if self.labels:
            self.labels.validate()
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['labels'] = self.labels.to_map()

        result['metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['metrics'].append(k1.to_map() if k1 else None)

        if self.needs_processing is not None:
            result['needs_processing'] = self.needs_processing

        if self.query_type is not None:
            result['query_type'] = self.query_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labels') is not None:
            temp_model = main_models.MetricSetSpecLabels()
            self.labels = temp_model.from_map(m.get('labels'))

        self.metrics = []
        if m.get('metrics') is not None:
            for k1 in m.get('metrics'):
                temp_model = main_models.Metric()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('needs_processing') is not None:
            self.needs_processing = m.get('needs_processing')

        if m.get('query_type') is not None:
            self.query_type = m.get('query_type')

        return self

class MetricSetSpecLabels(DaraModel):
    def __init__(
        self,
        dynamic: bool = None,
        keys: List[str] = None,
    ):
        # Specifies whether to automatically extract (dynamically generate) labels based on data. Set this parameter to true in most cases.
        self.dynamic = dynamic
        # The static label key list. This parameter takes effect when dynamic is set to false.
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic is not None:
            result['dynamic'] = self.dynamic

        if self.keys is not None:
            result['keys'] = self.keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dynamic') is not None:
            self.dynamic = m.get('dynamic')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        return self

