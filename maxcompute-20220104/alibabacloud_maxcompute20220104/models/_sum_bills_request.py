# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SumBillsRequest(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        project_names: List[str] = None,
        start_date: int = None,
        stats_type: str = None,
        top_n: int = None,
    ):
        self.end_date = end_date
        self.project_names = project_names
        self.start_date = start_date
        self.stats_type = stats_type
        self.top_n = top_n

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

        if self.stats_type is not None:
            result['statsType'] = self.stats_type

        if self.top_n is not None:
            result['topN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('projectNames') is not None:
            self.project_names = m.get('projectNames')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('statsType') is not None:
            self.stats_type = m.get('statsType')

        if m.get('topN') is not None:
            self.top_n = m.get('topN')

        return self

