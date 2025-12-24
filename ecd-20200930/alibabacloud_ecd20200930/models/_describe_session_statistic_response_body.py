# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeSessionStatisticResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: List[main_models.DescribeSessionStatisticResponseBodyStatistic] = None,
        total_count: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics.
        self.statistic = statistic
        # The total number of sessions returned.
        self.total_count = total_count

    def validate(self):
        if self.statistic:
            for v1 in self.statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Statistic'] = []
        if self.statistic is not None:
            for k1 in self.statistic:
                result['Statistic'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.statistic = []
        if m.get('Statistic') is not None:
            for k1 in m.get('Statistic'):
                temp_model = main_models.DescribeSessionStatisticResponseBodyStatistic()
                self.statistic.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSessionStatisticResponseBodyStatistic(DaraModel):
    def __init__(
        self,
        count: int = None,
        time_point: int = None,
    ):
        # The total number of sessions in the time range.
        self.count = count
        # The point in time.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

