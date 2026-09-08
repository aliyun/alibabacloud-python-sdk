# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressMicro(DaraModel):
    def __init__(
        self,
        current: int = None,
        total: int = None,
    ):
        # 当前 micro-batch 序号
        self.current = current
        # micro-batch 总数
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

