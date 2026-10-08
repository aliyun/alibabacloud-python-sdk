# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationScalingRuleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_behaviour: str = None,
        scaling_rule_enable: bool = None,
        scaling_rule_metric: str = None,
        scaling_rule_name: str = None,
        scaling_rule_timer: str = None,
        scaling_rule_trigger: str = None,
        scaling_rule_type: str = None,
    ):
        # The ID of the application. Call the [ListApplication](https://help.aliyun.com/document_detail/149390.html) operation to obtain this ID.
        self.app_id = app_id
        # The configuration of custom scaling behaviors. For more information about the data structure, see the example.
        self.scaling_behaviour = scaling_behaviour
        # The status of the Auto Scaling policy.
        # 
        # - **true**: enabled
        # 
        # - **false**: disabled
        self.scaling_rule_enable = scaling_rule_enable
        # This parameter is deprecated.
        self.scaling_rule_metric = scaling_rule_metric
        # The name of the Auto Scaling policy.
        self.scaling_rule_name = scaling_rule_name
        # This parameter is deprecated.
        self.scaling_rule_timer = scaling_rule_timer
        # The trigger policy, which is a JSON string of a ScalingRuleTriggerDTO object. For more information about the format, see the Additional information about request parameters section.
        self.scaling_rule_trigger = scaling_rule_trigger
        # The type of the Auto Scaling policy. Only the following type is supported:
        # 
        # - trigger: a trigger-based policy.
        self.scaling_rule_type = scaling_rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.scaling_behaviour is not None:
            result['ScalingBehaviour'] = self.scaling_behaviour

        if self.scaling_rule_enable is not None:
            result['ScalingRuleEnable'] = self.scaling_rule_enable

        if self.scaling_rule_metric is not None:
            result['ScalingRuleMetric'] = self.scaling_rule_metric

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer

        if self.scaling_rule_trigger is not None:
            result['ScalingRuleTrigger'] = self.scaling_rule_trigger

        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ScalingBehaviour') is not None:
            self.scaling_behaviour = m.get('ScalingBehaviour')

        if m.get('ScalingRuleEnable') is not None:
            self.scaling_rule_enable = m.get('ScalingRuleEnable')

        if m.get('ScalingRuleMetric') is not None:
            self.scaling_rule_metric = m.get('ScalingRuleMetric')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')

        if m.get('ScalingRuleTrigger') is not None:
            self.scaling_rule_trigger = m.get('ScalingRuleTrigger')

        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')

        return self

