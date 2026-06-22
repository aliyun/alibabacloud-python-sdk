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
        # The ID of the cluster that you want to modify.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The list of rule IDs to operate on. Separate multiple IDs with commas (,).
        # > You can call the [ListInterceptionRulePage](~~ListInterceptionRulePage~~) operation to obtain this parameter.
        self.rule_ids = rule_ids
        # The switch status of the rule. Valid values:
        # 
        # - **1**: Enabled.
        # - **0**: Disabled.
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

