# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowSankeyColumn(DaraModel):
    def __init__(
        self,
        count: int = None,
        key: str = None,
        label: str = None,
    ):
        # The number of trajectories in the column. The value is monotonized: reaching a later stage implies having passed through all preceding stages.
        self.count = count
        # The column identifier. Valid values: gen, run, rollout, sampled, and trained.
        self.key = key
        # The Chinese name of the column. Valid values: 轨迹生成, Agent 启动, Rollout 完成, 采样入批, and 完成训练.
        self.label = label

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

