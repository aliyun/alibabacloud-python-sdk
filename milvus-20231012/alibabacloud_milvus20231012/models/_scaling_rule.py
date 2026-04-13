# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class ScalingRule(DaraModel):
    def __init__(
        self,
        adjust_infos: List[main_models.ScalingRuleAdjustInfos] = None,
        cron_str: str = None,
        disabled: bool = None,
        end_time: int = None,
        rule_id: str = None,
        scaling_rule_name: str = None,
        start_time: int = None,
        time_zone: str = None,
    ):
        self.adjust_infos = adjust_infos
        self.cron_str = cron_str
        self.disabled = disabled
        self.end_time = end_time
        self.rule_id = rule_id
        self.scaling_rule_name = scaling_rule_name
        self.start_time = start_time
        self.time_zone = time_zone

    def validate(self):
        if self.adjust_infos:
            for v1 in self.adjust_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['adjustInfos'] = []
        if self.adjust_infos is not None:
            for k1 in self.adjust_infos:
                result['adjustInfos'].append(k1.to_map() if k1 else None)

        if self.cron_str is not None:
            result['cronStr'] = self.cron_str

        if self.disabled is not None:
            result['disabled'] = self.disabled

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.scaling_rule_name is not None:
            result['scalingRuleName'] = self.scaling_rule_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.adjust_infos = []
        if m.get('adjustInfos') is not None:
            for k1 in m.get('adjustInfos'):
                temp_model = main_models.ScalingRuleAdjustInfos()
                self.adjust_infos.append(temp_model.from_map(k1))

        if m.get('cronStr') is not None:
            self.cron_str = m.get('cronStr')

        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('scalingRuleName') is not None:
            self.scaling_rule_name = m.get('scalingRuleName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

class ScalingRuleAdjustInfos(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        target_value: str = None,
    ):
        self.component_type = component_type
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.target_value is not None:
            result['targetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('targetValue') is not None:
            self.target_value = m.get('targetValue')

        return self

