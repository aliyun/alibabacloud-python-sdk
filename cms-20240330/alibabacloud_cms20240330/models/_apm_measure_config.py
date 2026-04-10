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
        # 分组维度
        self.group_by = group_by
        # 指标代码
        # 
        # This parameter is required.
        self.measure_code = measure_code
        # 查询时间窗口（秒）
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

