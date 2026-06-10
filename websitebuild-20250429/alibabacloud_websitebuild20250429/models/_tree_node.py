# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class TreeNode(DaraModel):
    def __init__(
        self,
        children: List[main_models.TreeNode] = None,
        final_step_no: int = None,
        finish_time: int = None,
        is_container_node: bool = None,
        node_id: str = None,
        node_name: str = None,
        node_status: str = None,
        operator_role: str = None,
        parent_node_id: str = None,
        step_no: int = None,
    ):
        self.children = children
        self.final_step_no = final_step_no
        self.finish_time = finish_time
        self.is_container_node = is_container_node
        self.node_id = node_id
        self.node_name = node_name
        self.node_status = node_status
        self.operator_role = operator_role
        self.parent_node_id = parent_node_id
        self.step_no = step_no

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.is_container_node is not None:
            result['IsContainerNode'] = self.is_container_node

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role

        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id

        if self.step_no is not None:
            result['StepNo'] = self.step_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.TreeNode()
                self.children.append(temp_model.from_map(k1))

        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('IsContainerNode') is not None:
            self.is_container_node = m.get('IsContainerNode')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')

        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')

        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')

        return self

