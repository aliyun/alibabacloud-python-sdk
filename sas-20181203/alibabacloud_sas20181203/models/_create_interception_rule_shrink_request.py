# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInterceptionRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        dst_target_list_shrink: str = None,
        intercept_type: int = None,
        order_index: int = None,
        rule_name: str = None,
        rule_switch: int = None,
        rule_type: str = None,
        src_target_shrink: str = None,
    ):
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The information about the destination network object. The value of this parameter contains the following fields:
        # 
        # *   targetId: the ID of the destination network object. You can call the [ListInterceptionTargetPage](~~ListInterceptionTargetPage~~) operation to query the ID.
        # *   ports: the destination port ranges.
        self.dst_target_list_shrink = dst_target_list_shrink
        # The action on traffic. Valid values:
        # 
        # *   **1**: blocks traffic.
        # *   **2**: allows traffic and generates alerts.
        # *   **3**: allows traffic and does not generate alerts.
        # 
        # This parameter is required.
        self.intercept_type = intercept_type
        # The priority of the defense rule. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.order_index = order_index
        # The name of the defense rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Specifies the status of the defense rule. Valid values:
        # 
        # *   **0**: disables the rule.
        # *   **1**: enables the rule.
        # 
        # This parameter is required.
        self.rule_switch = rule_switch
        # The type of the defense rule. Valid values:
        # 
        # *   customize: custom rule
        self.rule_type = rule_type
        # The source network object. The value of this parameter contains the following field:
        # 
        # *   targetId: the ID of the source network object. You can call the [ListInterceptionTargetPage](~~ListInterceptionTargetPage~~) operation to query the ID.
        self.src_target_shrink = src_target_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.dst_target_list_shrink is not None:
            result['DstTargetList'] = self.dst_target_list_shrink

        if self.intercept_type is not None:
            result['InterceptType'] = self.intercept_type

        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.src_target_shrink is not None:
            result['SrcTarget'] = self.src_target_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DstTargetList') is not None:
            self.dst_target_list_shrink = m.get('DstTargetList')

        if m.get('InterceptType') is not None:
            self.intercept_type = m.get('InterceptType')

        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SrcTarget') is not None:
            self.src_target_shrink = m.get('SrcTarget')

        return self

