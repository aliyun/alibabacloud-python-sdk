# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class RecommendScalingRule(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        adjustment_value: int = None,
        instance_type: str = None,
        max_save: float = None,
        metrics_trigger: main_models.MetricsTrigger = None,
        rule_name: str = None,
        time_trigger: main_models.TimeTrigger = None,
        trigger_type: str = None,
    ):
        # 伸缩活动类型。取值范围：
        # - SCALE_OUT：扩容。
        # - SCALE_IN：缩容。
        # 
        # This parameter is required.
        self.activity_type = activity_type
        # 调整值。需要为正数，代表需要扩容或者缩容的实例数量。
        # 
        # This parameter is required.
        self.adjustment_value = adjustment_value
        # 推荐的规格类型。
        self.instance_type = instance_type
        # 最大节约成本。
        self.max_save = max_save
        # 按照负载伸缩描述。
        # <p>
        self.metrics_trigger = metrics_trigger
        # 规则名称。
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # 按照时间伸缩描述。
        # <p>
        self.time_trigger = time_trigger
        # 伸缩规则类型。 取值范围：
        # - TIME_TRIGGER: 按时间伸缩。
        # - METRICS_TRIGGER: 按负载伸缩。
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

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_save is not None:
            result['MaxSave'] = self.max_save

        if self.metrics_trigger is not None:
            result['MetricsTrigger'] = self.metrics_trigger.to_map()

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

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxSave') is not None:
            self.max_save = m.get('MaxSave')

        if m.get('MetricsTrigger') is not None:
            temp_model = main_models.MetricsTrigger()
            self.metrics_trigger = temp_model.from_map(m.get('MetricsTrigger'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TimeTrigger') is not None:
            temp_model = main_models.TimeTrigger()
            self.time_trigger = temp_model.from_map(m.get('TimeTrigger'))

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

