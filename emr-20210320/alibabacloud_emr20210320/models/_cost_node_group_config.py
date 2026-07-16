# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class CostNodeGroupConfig(DaraModel):
    def __init__(
        self,
        instance_types: List[main_models.CostInstanceType] = None,
        maximal_node_count: int = None,
        minimal_node_count: int = None,
        node_count: int = None,
        node_group_name: str = None,
        node_group_type: str = None,
        payment_type: str = None,
    ):
        # 实例类型列表。
        self.instance_types = instance_types
        # 最大节点数限制。
        self.maximal_node_count = maximal_node_count
        # 最小节点数限制。
        self.minimal_node_count = minimal_node_count
        # 节点数。
        self.node_count = node_count
        self.node_group_name = node_group_name
        # 节点组类型。取值范围：
        # - MASTER：管理类型节点组。
        # - CORE：存储类型节点组。
        # - TASK：计算类型节点组。
        self.node_group_type = node_group_type
        # 付费类型。
        self.payment_type = payment_type

    def validate(self):
        if self.instance_types:
            for v1 in self.instance_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k1 in self.instance_types:
                result['InstanceTypes'].append(k1.to_map() if k1 else None)

        if self.maximal_node_count is not None:
            result['MaximalNodeCount'] = self.maximal_node_count

        if self.minimal_node_count is not None:
            result['MinimalNodeCount'] = self.minimal_node_count

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k1 in m.get('InstanceTypes'):
                temp_model = main_models.CostInstanceType()
                self.instance_types.append(temp_model.from_map(k1))

        if m.get('MaximalNodeCount') is not None:
            self.maximal_node_count = m.get('MaximalNodeCount')

        if m.get('MinimalNodeCount') is not None:
            self.minimal_node_count = m.get('MinimalNodeCount')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        return self

