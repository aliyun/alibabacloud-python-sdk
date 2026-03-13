# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnschedulableNodeDetail(DaraModel):
    def __init__(
        self,
        nodes: List[str] = None,
        reason: str = None,
    ):
        self.nodes = nodes
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nodes is not None:
            result['Nodes'] = self.nodes

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

