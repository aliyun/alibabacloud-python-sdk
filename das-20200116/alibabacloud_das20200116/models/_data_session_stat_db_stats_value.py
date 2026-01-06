# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataSessionStatDbStatsValue(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        total_count: int = None,
    ):
        # The number of active namespaces.
        self.active_count = active_count
        # The total number of namespaces.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

