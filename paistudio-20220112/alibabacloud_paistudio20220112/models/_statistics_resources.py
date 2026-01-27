# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StatisticsResources(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        hyper_node_num: int = None,
        memory: str = None,
        node_num: int = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.hyper_node_num = hyper_node_num
        self.memory = memory
        self.node_num = node_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.hyper_node_num is not None:
            result['HyperNodeNum'] = self.hyper_node_num

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('HyperNodeNum') is not None:
            self.hyper_node_num = m.get('HyperNodeNum')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        return self

