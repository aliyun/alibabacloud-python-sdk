# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class PutAutoScalingPolicyRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraints: main_models.ScalingConstraints = None,
        node_group_id: str = None,
        region_id: str = None,
        scaling_rules: List[main_models.ScalingRule] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The maximum and minimum size constraints for the node group.
        self.constraints = constraints
        # The node group ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The scaling rules. The number of elements in the array can be from 0 to 100.
        self.scaling_rules = scaling_rules

    def validate(self):
        if self.constraints:
            self.constraints.validate()
        if self.scaling_rules:
            for v1 in self.scaling_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ScalingRules'] = []
        if self.scaling_rules is not None:
            for k1 in self.scaling_rules:
                result['ScalingRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Constraints') is not None:
            temp_model = main_models.ScalingConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.scaling_rules = []
        if m.get('ScalingRules') is not None:
            for k1 in m.get('ScalingRules'):
                temp_model = main_models.ScalingRule()
                self.scaling_rules.append(temp_model.from_map(k1))

        return self

