# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ModifyInterceptionRuleRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        dst_target: Dict[str, Any] = None,
        intercept_type: int = None,
        order_index: int = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_switch: int = None,
        src_target: Dict[str, Any] = None,
    ):
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](https://help.aliyun.com/document_detail/182997.html) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The destination objects of the rule. The following parameters are included:
        # 
        # *   targetId: the ID of the destination object. You can call the [ListInterceptionTargetPage](~~ListInterceptionTargetPage~~) operation to query the ID.
        # *   ports: the destination port ranges.
        self.dst_target = dst_target
        # The interception mode. Valid values:
        # 
        # *   **1**: block
        # *   **2**: alert
        # *   **3**: allow
        self.intercept_type = intercept_type
        # The priority of the rule. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        self.order_index = order_index
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # Specifies whether the rule is enabled. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.rule_switch = rule_switch
        # The source object of the rule. The following parameters are included:
        # 
        # *   targetId: the ID of the source object. You can call the [ListInterceptionTargetPage](~~ListInterceptionTargetPage~~) operation to query the ID.
        self.src_target = src_target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.dst_target is not None:
            result['DstTarget'] = self.dst_target

        if self.intercept_type is not None:
            result['InterceptType'] = self.intercept_type

        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch

        if self.src_target is not None:
            result['SrcTarget'] = self.src_target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DstTarget') is not None:
            self.dst_target = m.get('DstTarget')

        if m.get('InterceptType') is not None:
            self.intercept_type = m.get('InterceptType')

        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')

        if m.get('SrcTarget') is not None:
            self.src_target = m.get('SrcTarget')

        return self

