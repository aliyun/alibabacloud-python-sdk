# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowFunnelStage(DaraModel):
    def __init__(
        self,
        count: int = None,
        key: str = None,
        label: str = None,
        pct: float = None,
    ):
        # The number of trajectories that reach this level.
        self.count = count
        # The level identifier. Valid values: traj, dispatch, run, rollout, reward, sampled, and trained.
        self.key = key
        # The Chinese name of the level. Valid values: 生成轨迹, 下发到 Worker, Agent 启动, Rollout 完成, reward 打分, 采样入批, and 完成训练.
        self.label = label
        # The percentage relative to the first traj level.
        self.pct = pct

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        if self.pct is not None:
            result['Pct'] = self.pct

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Pct') is not None:
            self.pct = m.get('Pct')

        return self

