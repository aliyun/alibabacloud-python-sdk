# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeDeductionStatisticRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids: List[str] = None,
        periods: List[main_models.DescribeDeductionStatisticRequestPeriods] = None,
        resource_types: List[str] = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_ids = instance_ids
        self.periods = periods
        self.resource_types = resource_types
        self.start_time = start_time

    def validate(self):
        if self.periods:
            for v1 in self.periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        result['Periods'] = []
        if self.periods is not None:
            for k1 in self.periods:
                result['Periods'].append(k1.to_map() if k1 else None)

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        self.periods = []
        if m.get('Periods') is not None:
            for k1 in m.get('Periods'):
                temp_model = main_models.DescribeDeductionStatisticRequestPeriods()
                self.periods.append(temp_model.from_map(k1))

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDeductionStatisticRequestPeriods(DaraModel):
    def __init__(
        self,
        base_time: str = None,
        period_unit: str = None,
    ):
        self.base_time = base_time
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_time is not None:
            result['BaseTime'] = self.base_time

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseTime') is not None:
            self.base_time = m.get('BaseTime')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        return self

