# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowSankeyExit(DaraModel):
    def __init__(
        self,
        count: int = None,
        from_: str = None,
        from_idx: int = None,
        label: str = None,
    ):
        # The number of trajectories on the outflow edge.
        self.count = count
        # The key of the outflow source column.
        self.from_ = from_
        # The index of the outflow source column (0-based).
        self.from_idx = from_idx
        # The Chinese name of the outflow destination. Valid values vary by the column where the outflow is located: 在途·未下发 / 在途·生成中 / 在途·待采样 / 在途·待训练.
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

        if self.from_ is not None:
            result['From'] = self.from_

        if self.from_idx is not None:
            result['FromIdx'] = self.from_idx

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('FromIdx') is not None:
            self.from_idx = m.get('FromIdx')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

