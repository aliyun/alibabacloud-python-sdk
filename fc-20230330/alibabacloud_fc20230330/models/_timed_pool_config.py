# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class TimedPoolConfig(DaraModel):
    def __init__(
        self,
        effective_end_date: str = None,
        effective_start_date: str = None,
        elastic_intervals: List[main_models.ElasticInterval] = None,
        time_zone: str = None,
    ):
        self.effective_end_date = effective_end_date
        self.effective_start_date = effective_start_date
        self.elastic_intervals = elastic_intervals
        self.time_zone = time_zone

    def validate(self):
        if self.elastic_intervals:
            for v1 in self.elastic_intervals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_end_date is not None:
            result['effectiveEndDate'] = self.effective_end_date

        if self.effective_start_date is not None:
            result['effectiveStartDate'] = self.effective_start_date

        result['elasticIntervals'] = []
        if self.elastic_intervals is not None:
            for k1 in self.elastic_intervals:
                result['elasticIntervals'].append(k1.to_map() if k1 else None)

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effectiveEndDate') is not None:
            self.effective_end_date = m.get('effectiveEndDate')

        if m.get('effectiveStartDate') is not None:
            self.effective_start_date = m.get('effectiveStartDate')

        self.elastic_intervals = []
        if m.get('elasticIntervals') is not None:
            for k1 in m.get('elasticIntervals'):
                temp_model = main_models.ElasticInterval()
                self.elastic_intervals.append(temp_model.from_map(k1))

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

