# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class AssignNodeSpec(DaraModel):
    def __init__(
        self,
        anti_affinity_hyper_nodes: List[main_models.HyperNodeSpec] = None,
        anti_affinity_node_names: str = None,
        enable_assign_node: bool = None,
        hyper_nodes: List[main_models.HyperNodeSpec] = None,
        node_names: str = None,
    ):
        self.anti_affinity_hyper_nodes = anti_affinity_hyper_nodes
        self.anti_affinity_node_names = anti_affinity_node_names
        self.enable_assign_node = enable_assign_node
        self.hyper_nodes = hyper_nodes
        self.node_names = node_names

    def validate(self):
        if self.anti_affinity_hyper_nodes:
            for v1 in self.anti_affinity_hyper_nodes:
                 if v1:
                    v1.validate()
        if self.hyper_nodes:
            for v1 in self.hyper_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AntiAffinityHyperNodes'] = []
        if self.anti_affinity_hyper_nodes is not None:
            for k1 in self.anti_affinity_hyper_nodes:
                result['AntiAffinityHyperNodes'].append(k1.to_map() if k1 else None)

        if self.anti_affinity_node_names is not None:
            result['AntiAffinityNodeNames'] = self.anti_affinity_node_names

        if self.enable_assign_node is not None:
            result['EnableAssignNode'] = self.enable_assign_node

        result['HyperNodes'] = []
        if self.hyper_nodes is not None:
            for k1 in self.hyper_nodes:
                result['HyperNodes'].append(k1.to_map() if k1 else None)

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anti_affinity_hyper_nodes = []
        if m.get('AntiAffinityHyperNodes') is not None:
            for k1 in m.get('AntiAffinityHyperNodes'):
                temp_model = main_models.HyperNodeSpec()
                self.anti_affinity_hyper_nodes.append(temp_model.from_map(k1))

        if m.get('AntiAffinityNodeNames') is not None:
            self.anti_affinity_node_names = m.get('AntiAffinityNodeNames')

        if m.get('EnableAssignNode') is not None:
            self.enable_assign_node = m.get('EnableAssignNode')

        self.hyper_nodes = []
        if m.get('HyperNodes') is not None:
            for k1 in m.get('HyperNodes'):
                temp_model = main_models.HyperNodeSpec()
                self.hyper_nodes.append(temp_model.from_map(k1))

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        return self

