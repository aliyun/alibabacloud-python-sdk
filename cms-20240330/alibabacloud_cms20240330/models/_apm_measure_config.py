# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ApmMeasureConfig(DaraModel):
    def __init__(
        self,
        group_by: List[str] = None,
        measure_code: str = None,
        window_secs: int = None,
    ):
        # An array of dimension keys used to group the results.
        self.group_by = group_by
        # The unique code that identifies the metric.
        # 
        # This parameter is required.
        self.measure_code = measure_code
        # The aggregation period in seconds, which determines the time granularity of data points.
        # 
        # This parameter is required.
        self.window_secs = window_secs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.measure_code is not None:
            result['measureCode'] = self.measure_code

        if self.window_secs is not None:
            result['windowSecs'] = self.window_secs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('measureCode') is not None:
            self.measure_code = m.get('measureCode')

        if m.get('windowSecs') is not None:
            self.window_secs = m.get('windowSecs')

        return self

