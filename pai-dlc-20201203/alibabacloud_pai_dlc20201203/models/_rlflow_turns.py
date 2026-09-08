# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowTurns(DaraModel):
    def __init__(
        self,
        avg: float = None,
        count: int = None,
        max: int = None,
        p_50: int = None,
        p_90: int = None,
    ):
        # 平均生成轮数
        self.avg = avg
        # 参与统计的轨迹数
        self.count = count
        # 最大生成轮数
        self.max = max
        # 生成轮数 P50
        self.p_50 = p_50
        # 生成轮数 P90
        self.p_90 = p_90

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg is not None:
            result['Avg'] = self.avg

        if self.count is not None:
            result['Count'] = self.count

        if self.max is not None:
            result['Max'] = self.max

        if self.p_50 is not None:
            result['P50'] = self.p_50

        if self.p_90 is not None:
            result['P90'] = self.p_90

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avg') is not None:
            self.avg = m.get('Avg')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('P50') is not None:
            self.p_50 = m.get('P50')

        if m.get('P90') is not None:
            self.p_90 = m.get('P90')

        return self

