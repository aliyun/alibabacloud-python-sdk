# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class NodeSelector(DaraModel):
    def __init__(
        self,
        node_group_id: str = None,
        node_group_ids: List[str] = None,
        node_group_name: str = None,
        node_group_names: List[str] = None,
        node_group_types: List[str] = None,
        node_names: List[str] = None,
        node_select_type: str = None,
    ):
        # > This parameter is deprecated. Use `NodeGroupIds` instead.
        self.node_group_id = node_group_id
        # The IDs of the node groups to select.
        self.node_group_ids = node_group_ids
        # > This parameter is deprecated. Use `NodeGroupNames` instead.
        self.node_group_name = node_group_name
        # The names of the node groups to select.
        self.node_group_names = node_group_names
        # The types of node groups to select. This parameter applies only when `NodeSelectType` is set to `NODE_GROUP` and `NodeGroupIds` is not specified. The array can contain up to 10 elements.
        self.node_group_types = node_group_types
        # The names of the nodes to select. This parameter applies only when `NodeSelectType` is set to `NODE`.
        self.node_names = node_names
        # The node selection type. Valid values:
        # 
        # - `CLUSTER`: Selects all nodes in the cluster.
        # 
        # - `NODE_GROUP`: Selects nodes by their node group.
        # 
        # - `NODE`: Selects specific nodes by name.
        # 
        # This parameter is required.
        self.node_select_type = node_select_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_group_names is not None:
            result['NodeGroupNames'] = self.node_group_names

        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        if self.node_select_type is not None:
            result['NodeSelectType'] = self.node_select_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeGroupNames') is not None:
            self.node_group_names = m.get('NodeGroupNames')

        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        if m.get('NodeSelectType') is not None:
            self.node_select_type = m.get('NodeSelectType')

        return self

