# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StatisticsDetails(DaraModel):
    def __init__(
        self,
        count: int = None,
        idle_num: int = None,
    ):
        self.count = count
        self.idle_num = idle_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.idle_num is not None:
            result['IdleNum'] = self.idle_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('IdleNum') is not None:
            self.idle_num = m.get('IdleNum')

        return self

