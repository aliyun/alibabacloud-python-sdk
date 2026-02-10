# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInterceptionRuleSwitchRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        rule_ids: str = None,
        rule_switch: int = None,
    ):
        # The ID of the cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The IDs of the rules whose status you want to change. Separate multiple IDs with commas (,).
        # 
        # > You can call the [ListInterceptionRulePage](https://help.aliyun.com/document_detail/182997.html) operation to query the IDs of rules.
        self.rule_ids = rule_ids
        # Specifies whether the rule is enabled. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.rule_switch = rule_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')

        return self

