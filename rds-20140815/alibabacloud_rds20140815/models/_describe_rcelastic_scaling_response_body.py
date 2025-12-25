# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCElasticScalingResponseBody(DaraModel):
    def __init__(
        self,
        acu_type: str = None,
        instance_id: str = None,
        request_id: str = None,
        scaling_enabled: bool = None,
        scaling_supported: bool = None,
        scheduled_rule: str = None,
        scheduled_rule_templates: main_models.DescribeRCElasticScalingResponseBodyScheduledRuleTemplates = None,
        target_instance_type: str = None,
    ):
        self.acu_type = acu_type
        self.instance_id = instance_id
        self.request_id = request_id
        self.scaling_enabled = scaling_enabled
        self.scaling_supported = scaling_supported
        self.scheduled_rule = scheduled_rule
        self.scheduled_rule_templates = scheduled_rule_templates
        self.target_instance_type = target_instance_type

    def validate(self):
        if self.scheduled_rule_templates:
            self.scheduled_rule_templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acu_type is not None:
            result['AcuType'] = self.acu_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_enabled is not None:
            result['ScalingEnabled'] = self.scaling_enabled

        if self.scaling_supported is not None:
            result['ScalingSupported'] = self.scaling_supported

        if self.scheduled_rule is not None:
            result['ScheduledRule'] = self.scheduled_rule

        if self.scheduled_rule_templates is not None:
            result['ScheduledRuleTemplates'] = self.scheduled_rule_templates.to_map()

        if self.target_instance_type is not None:
            result['TargetInstanceType'] = self.target_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcuType') is not None:
            self.acu_type = m.get('AcuType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingEnabled') is not None:
            self.scaling_enabled = m.get('ScalingEnabled')

        if m.get('ScalingSupported') is not None:
            self.scaling_supported = m.get('ScalingSupported')

        if m.get('ScheduledRule') is not None:
            self.scheduled_rule = m.get('ScheduledRule')

        if m.get('ScheduledRuleTemplates') is not None:
            temp_model = main_models.DescribeRCElasticScalingResponseBodyScheduledRuleTemplates()
            self.scheduled_rule_templates = temp_model.from_map(m.get('ScheduledRuleTemplates'))

        if m.get('TargetInstanceType') is not None:
            self.target_instance_type = m.get('TargetInstanceType')

        return self

class DescribeRCElasticScalingResponseBodyScheduledRuleTemplates(DaraModel):
    def __init__(
        self,
        items: List[str] = None,
    ):
        self.items = items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['items'] = self.items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            self.items = m.get('items')

        return self

