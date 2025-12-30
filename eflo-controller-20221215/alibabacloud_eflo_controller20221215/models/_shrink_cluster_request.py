# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ShrinkClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        node_groups: List[main_models.ShrinkClusterRequestNodeGroups] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The node groups.
        self.node_groups = node_groups

    def validate(self):
        if self.node_groups:
            for v1 in self.node_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k1 in self.node_groups:
                result['NodeGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.ShrinkClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k1))

        return self

class ShrinkClusterRequestNodeGroups(DaraModel):
    def __init__(
        self,
        hyper_nodes: List[main_models.ShrinkClusterRequestNodeGroupsHyperNodes] = None,
        node_group_id: str = None,
        nodes: List[main_models.ShrinkClusterRequestNodeGroupsNodes] = None,
    ):
        self.hyper_nodes = hyper_nodes
        # The node group ID.
        self.node_group_id = node_group_id
        # The nodes.
        self.nodes = nodes

    def validate(self):
        if self.hyper_nodes:
            for v1 in self.hyper_nodes:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HyperNodes'] = []
        if self.hyper_nodes is not None:
            for k1 in self.hyper_nodes:
                result['HyperNodes'].append(k1.to_map() if k1 else None)

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hyper_nodes = []
        if m.get('HyperNodes') is not None:
            for k1 in m.get('HyperNodes'):
                temp_model = main_models.ShrinkClusterRequestNodeGroupsHyperNodes()
                self.hyper_nodes.append(temp_model.from_map(k1))

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ShrinkClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class ShrinkClusterRequestNodeGroupsNodes(DaraModel):
    def __init__(
        self,
        node_id: str = None,
    ):
        # The node ID.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class ShrinkClusterRequestNodeGroupsHyperNodes(DaraModel):
    def __init__(
        self,
        hyper_node_id: str = None,
    ):
        self.hyper_node_id = hyper_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        return self

