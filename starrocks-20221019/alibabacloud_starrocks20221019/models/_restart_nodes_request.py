# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class RestartNodesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        restart_node_groups: List[main_models.RestartNodesRequestRestartNodeGroups] = None,
    ):
        self.instance_id = instance_id
        self.restart_node_groups = restart_node_groups

    def validate(self):
        if self.restart_node_groups:
            for v1 in self.restart_node_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['RestartNodeGroups'] = []
        if self.restart_node_groups is not None:
            for k1 in self.restart_node_groups:
                result['RestartNodeGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.restart_node_groups = []
        if m.get('RestartNodeGroups') is not None:
            for k1 in m.get('RestartNodeGroups'):
                temp_model = main_models.RestartNodesRequestRestartNodeGroups()
                self.restart_node_groups.append(temp_model.from_map(k1))

        return self

class RestartNodesRequestRestartNodeGroups(DaraModel):
    def __init__(
        self,
        fast_mode: bool = None,
        node_group_id: str = None,
        node_ids: List[str] = None,
    ):
        self.fast_mode = fast_mode
        self.node_group_id = node_group_id
        self.node_ids = node_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        return self

