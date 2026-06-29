# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskStatisticsRequest(DaraModel):
    def __init__(
        self,
        stat_type: str = None,
    ):
        # Statistics Type. Valid values:
        # - OPERATORCELL: Operation cell.
        # - ITEM: Single item.
        self.stat_type = stat_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stat_type is not None:
            result['StatType'] = self.stat_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatType') is not None:
            self.stat_type = m.get('StatType')

        return self

