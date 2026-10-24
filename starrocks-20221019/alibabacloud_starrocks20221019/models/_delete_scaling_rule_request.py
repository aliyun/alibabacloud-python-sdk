# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteScalingRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        scaling_rule_id: str = None,
        trigger_type: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The node group ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The ID of the scaling rule to be deleted.
        # 
        # This parameter is required.
        self.scaling_rule_id = scaling_rule_id
        # The trigger type.
        # 
        # This parameter is required.
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

