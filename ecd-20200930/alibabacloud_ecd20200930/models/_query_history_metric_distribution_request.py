# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryHistoryMetricDistributionRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        metric_name: str = None,
        ranges: List[main_models.QueryHistoryMetricDistributionRequestRanges] = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.metric_name = metric_name
        self.ranges = ranges
        self.start_date = start_date

    def validate(self):
        if self.ranges:
            for v1 in self.ranges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['Ranges'] = []
        if self.ranges is not None:
            for k1 in self.ranges:
                result['Ranges'].append(k1.to_map() if k1 else None)

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.ranges = []
        if m.get('Ranges') is not None:
            for k1 in m.get('Ranges'):
                temp_model = main_models.QueryHistoryMetricDistributionRequestRanges()
                self.ranges.append(temp_model.from_map(k1))

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

class QueryHistoryMetricDistributionRequestRanges(DaraModel):
    def __init__(
        self,
        include_max: bool = None,
        include_min: bool = None,
        label: str = None,
        max: float = None,
        min: float = None,
    ):
        self.include_max = include_max
        self.include_min = include_min
        self.label = label
        self.max = max
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_max is not None:
            result['IncludeMax'] = self.include_max

        if self.include_min is not None:
            result['IncludeMin'] = self.include_min

        if self.label is not None:
            result['Label'] = self.label

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeMax') is not None:
            self.include_max = m.get('IncludeMax')

        if m.get('IncludeMin') is not None:
            self.include_min = m.get('IncludeMin')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

