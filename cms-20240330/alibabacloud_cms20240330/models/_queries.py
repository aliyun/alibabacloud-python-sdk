# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class Queries(DaraModel):
    def __init__(
        self,
        end: int = None,
        expr: str = None,
        label_filters: List[main_models.LabelFilters] = None,
        metric: str = None,
        metric_set: str = None,
        name: str = None,
        start: int = None,
        time_unit: str = None,
        window: int = None,
    ):
        self.end = end
        self.expr = expr
        self.label_filters = label_filters
        self.metric = metric
        self.metric_set = metric_set
        self.name = name
        self.start = start
        self.time_unit = time_unit
        self.window = window

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
        if self.end is not None:
            result['end'] = self.end

        if self.expr is not None:
            result['expr'] = self.expr

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

        if self.start is not None:
            result['start'] = self.start

        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit

        if self.window is not None:
            result['window'] = self.window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        self.label_filters = []
        if m.get('labelFilters') is not None:
            for k1 in m.get('labelFilters'):
                temp_model = main_models.LabelFilters()
                self.label_filters.append(temp_model.from_map(k1))

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('metricSet') is not None:
            self.metric_set = m.get('metricSet')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')

        if m.get('window') is not None:
            self.window = m.get('window')

        return self

