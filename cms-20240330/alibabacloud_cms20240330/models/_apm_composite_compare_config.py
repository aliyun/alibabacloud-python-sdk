# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApmCompositeCompareConfig(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        operator: str = None,
        threshold: float = None,
    ):
        # 聚合函数
        # 
        # This parameter is required.
        self.aggregate = aggregate
        # 比较操作符
        # 
        # This parameter is required.
        self.operator = operator
        # 单阈值
        # 
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate

        if self.operator is not None:
            result['operator'] = self.operator

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

