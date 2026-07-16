# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class MetricSetNamedQueryEntry(DaraModel):
    def __init__(
        self,
        label_filters: List[main_models.UmodelLabelFilter] = None,
        metric: str = None,
        metric_set: str = None,
        name: str = None,
    ):
        self.label_filters = label_filters
        self.metric = metric
        self.metric_set = metric_set
        self.name = name

    def validate(self):
        if self.label_filters:
            for v1 in self.label_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['labelFilters'] = []
        if self.label_filters is not None:
            for k1 in self.label_filters:
                result['labelFilters'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['metric'] = self.metric

        if self.metric_set is not None:
            result['metricSet'] = self.metric_set

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_filters = []
        if m.get('labelFilters') is not None:
            for k1 in m.get('labelFilters'):
                temp_model = main_models.UmodelLabelFilter()
                self.label_filters.append(temp_model.from_map(k1))

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('metricSet') is not None:
            self.metric_set = m.get('metricSet')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

