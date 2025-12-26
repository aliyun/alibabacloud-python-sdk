# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BindingPolicy(DaraModel):
    def __init__(
        self,
        exclude_nodes: List[str] = None,
        include_nodes: List[str] = None,
        node_spec_count: int = None,
    ):
        self.exclude_nodes = exclude_nodes
        self.include_nodes = include_nodes
        self.node_spec_count = node_spec_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes

        if self.include_nodes is not None:
            result['IncludeNodes'] = self.include_nodes

        if self.node_spec_count is not None:
            result['NodeSpecCount'] = self.node_spec_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')

        if m.get('IncludeNodes') is not None:
            self.include_nodes = m.get('IncludeNodes')

        if m.get('NodeSpecCount') is not None:
            self.node_spec_count = m.get('NodeSpecCount')

        return self

