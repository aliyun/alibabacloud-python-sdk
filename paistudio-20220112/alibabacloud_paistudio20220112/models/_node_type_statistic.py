# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NodeTypeStatistic(DaraModel):
    def __init__(
        self,
        can_be_bound_count: int = None,
        node_type: str = None,
        total_count: int = None,
    ):
        self.can_be_bound_count = can_be_bound_count
        self.node_type = node_type
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_be_bound_count is not None:
            result['CanBeBoundCount'] = self.can_be_bound_count

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBeBoundCount') is not None:
            self.can_be_bound_count = m.get('CanBeBoundCount')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

