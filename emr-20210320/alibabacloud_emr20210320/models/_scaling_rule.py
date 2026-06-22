# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ScalingRule(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        adjustment_value: int = None,
        metrics_trigger: main_models.MetricsTrigger = None,
        min_adjustment_value: int = None,
        rule_name: str = None,
        time_trigger: main_models.TimeTrigger = None,
        trigger_type: str = None,
    ):
        # The type of the scaling activity. This parameter is required. Valid values:
        # 
        # - SCALE_OUT: scale-out.
        # 
        # - SCALE_IN: scale-in.
        # 
        # This parameter is required.
        self.activity_type = activity_type
        # The adjustment value. This parameter is required and must be a positive integer. It specifies the number of instances to add for a scale-out activity or remove for a scale-in activity.
        # 
        # This parameter is required.
        self.adjustment_value = adjustment_value
        # The configurations for load-based scaling.
        self.metrics_trigger = metrics_trigger
        # The minimum number of instances to add during a scale-out activity.
        self.min_adjustment_value = min_adjustment_value
        # The name of the rule. This parameter is required and cannot be an empty string.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The configurations for time-based scaling.
        self.time_trigger = time_trigger
        # The type of the scaling rule. This parameter is required. Valid values:
        # 
        # - TIME_TRIGGER: time-based scaling.
        # 
        # - METRICS_TRIGGER: load-based scaling.
        # 
        # This parameter is required.
        self.trigger_type = trigger_type

    def validate(self):
        if self.metrics_trigger:
            self.metrics_trigger.validate()
        if self.time_trigger:
            self.time_trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value

        if self.metrics_trigger is not None:
            result['MetricsTrigger'] = self.metrics_trigger.to_map()

        if self.min_adjustment_value is not None:
            result['MinAdjustmentValue'] = self.min_adjustment_value

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.time_trigger is not None:
            result['TimeTrigger'] = self.time_trigger.to_map()

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')

        if m.get('MetricsTrigger') is not None:
            temp_model = main_models.MetricsTrigger()
            self.metrics_trigger = temp_model.from_map(m.get('MetricsTrigger'))

        if m.get('MinAdjustmentValue') is not None:
            self.min_adjustment_value = m.get('MinAdjustmentValue')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TimeTrigger') is not None:
            temp_model = main_models.TimeTrigger()
            self.time_trigger = temp_model.from_map(m.get('TimeTrigger'))

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

