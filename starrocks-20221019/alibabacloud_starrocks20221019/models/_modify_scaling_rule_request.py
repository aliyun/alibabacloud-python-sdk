# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScalingRuleRequest(DaraModel):
    def __init__(
        self,
        new_trigger_type: str = None,
        node_group_id: str = None,
        old_trigger_type: str = None,
        rule: str = None,
        scaling_rule_id: str = None,
    ):
        # This parameter is required.
        self.new_trigger_type = new_trigger_type
        # This parameter is required.
        self.node_group_id = node_group_id
        # This parameter is required.
        self.old_trigger_type = old_trigger_type
        # This parameter is required.
        self.rule = rule
        # This parameter is required.
        self.scaling_rule_id = scaling_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_trigger_type is not None:
            result['NewTriggerType'] = self.new_trigger_type

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.old_trigger_type is not None:
            result['OldTriggerType'] = self.old_trigger_type

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewTriggerType') is not None:
            self.new_trigger_type = m.get('NewTriggerType')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('OldTriggerType') is not None:
            self.old_trigger_type = m.get('OldTriggerType')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')

        return self

