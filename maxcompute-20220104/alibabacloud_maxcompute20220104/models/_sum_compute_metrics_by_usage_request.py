# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SumComputeMetricsByUsageRequest(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        project_names: List[str] = None,
        start_date: int = None,
        usage_type: str = None,
    ):
        self.end_date = end_date
        self.project_names = project_names
        self.start_date = start_date
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.project_names is not None:
            result['projectNames'] = self.project_names

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.usage_type is not None:
            result['usageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('projectNames') is not None:
            self.project_names = m.get('projectNames')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('usageType') is not None:
            self.usage_type = m.get('usageType')

        return self

