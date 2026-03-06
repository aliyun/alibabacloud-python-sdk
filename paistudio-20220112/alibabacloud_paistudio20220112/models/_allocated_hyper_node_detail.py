# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocatedHyperNodeDetail(DaraModel):
    def __init__(
        self,
        allocated_node_num: int = None,
        empty_node_num: int = None,
        hyper_node_name: str = None,
        total_node_num: int = None,
    ):
        self.allocated_node_num = allocated_node_num
        self.empty_node_num = empty_node_num
        self.hyper_node_name = hyper_node_name
        self.total_node_num = total_node_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_node_num is not None:
            result['AllocatedNodeNum'] = self.allocated_node_num

        if self.empty_node_num is not None:
            result['EmptyNodeNum'] = self.empty_node_num

        if self.hyper_node_name is not None:
            result['HyperNodeName'] = self.hyper_node_name

        if self.total_node_num is not None:
            result['TotalNodeNum'] = self.total_node_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatedNodeNum') is not None:
            self.allocated_node_num = m.get('AllocatedNodeNum')

        if m.get('EmptyNodeNum') is not None:
            self.empty_node_num = m.get('EmptyNodeNum')

        if m.get('HyperNodeName') is not None:
            self.hyper_node_name = m.get('HyperNodeName')

        if m.get('TotalNodeNum') is not None:
            self.total_node_num = m.get('TotalNodeNum')

        return self

