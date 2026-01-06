# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class OperatorNode(DaraModel):
    def __init__(
        self,
        children: List[main_models.OperatorNode] = None,
        id: int = None,
        level_width: int = None,
        node_depth: int = None,
        node_name: str = None,
        node_width: int = None,
        parent_id: int = None,
        stats: main_models.OperatorNodeStats = None,
    ):
        self.children = children
        self.id = id
        self.level_width = level_width
        self.node_depth = node_depth
        self.node_name = node_name
        self.node_width = node_width
        self.parent_id = parent_id
        self.stats = stats

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()
        if self.stats:
            self.stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['children'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['id'] = self.id

        if self.level_width is not None:
            result['levelWidth'] = self.level_width

        if self.node_depth is not None:
            result['nodeDepth'] = self.node_depth

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.node_width is not None:
            result['nodeWidth'] = self.node_width

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.stats is not None:
            result['stats'] = self.stats.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k1 in m.get('children'):
                temp_model = main_models.OperatorNode()
                self.children.append(temp_model.from_map(k1))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('levelWidth') is not None:
            self.level_width = m.get('levelWidth')

        if m.get('nodeDepth') is not None:
            self.node_depth = m.get('nodeDepth')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('nodeWidth') is not None:
            self.node_width = m.get('nodeWidth')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('stats') is not None:
            temp_model = main_models.OperatorNodeStats()
            self.stats = temp_model.from_map(m.get('stats'))

        return self

class OperatorNodeStats(DaraModel):
    def __init__(
        self,
        bytes: int = None,
        output_rows: int = None,
        parameters: str = None,
        peak_memory: int = None,
        time_cost: int = None,
    ):
        self.bytes = bytes
        self.output_rows = output_rows
        self.parameters = parameters
        self.peak_memory = peak_memory
        self.time_cost = time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes is not None:
            result['bytes'] = self.bytes

        if self.output_rows is not None:
            result['outputRows'] = self.output_rows

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.peak_memory is not None:
            result['peakMemory'] = self.peak_memory

        if self.time_cost is not None:
            result['timeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bytes') is not None:
            self.bytes = m.get('bytes')

        if m.get('outputRows') is not None:
            self.output_rows = m.get('outputRows')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('peakMemory') is not None:
            self.peak_memory = m.get('peakMemory')

        if m.get('timeCost') is not None:
            self.time_cost = m.get('timeCost')

        return self

