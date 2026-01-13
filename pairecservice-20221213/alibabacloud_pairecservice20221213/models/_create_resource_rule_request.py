# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class CreateResourceRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        metric_operation_type: str = None,
        metric_pull_info: str = None,
        metric_pull_period: str = None,
        name: str = None,
        rule_computing_definition: str = None,
        rule_items: List[main_models.CreateResourceRuleRequestRuleItems] = None,
    ):
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.metric_operation_type = metric_operation_type
        self.metric_pull_info = metric_pull_info
        self.metric_pull_period = metric_pull_period
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.rule_computing_definition = rule_computing_definition
        # This parameter is required.
        self.rule_items = rule_items

    def validate(self):
        if self.rule_items:
            for v1 in self.rule_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.metric_operation_type is not None:
            result['MetricOperationType'] = self.metric_operation_type

        if self.metric_pull_info is not None:
            result['MetricPullInfo'] = self.metric_pull_info

        if self.metric_pull_period is not None:
            result['MetricPullPeriod'] = self.metric_pull_period

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_computing_definition is not None:
            result['RuleComputingDefinition'] = self.rule_computing_definition

        result['RuleItems'] = []
        if self.rule_items is not None:
            for k1 in self.rule_items:
                result['RuleItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MetricOperationType') is not None:
            self.metric_operation_type = m.get('MetricOperationType')

        if m.get('MetricPullInfo') is not None:
            self.metric_pull_info = m.get('MetricPullInfo')

        if m.get('MetricPullPeriod') is not None:
            self.metric_pull_period = m.get('MetricPullPeriod')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleComputingDefinition') is not None:
            self.rule_computing_definition = m.get('RuleComputingDefinition')

        self.rule_items = []
        if m.get('RuleItems') is not None:
            for k1 in m.get('RuleItems'):
                temp_model = main_models.CreateResourceRuleRequestRuleItems()
                self.rule_items.append(temp_model.from_map(k1))

        return self

class CreateResourceRuleRequestRuleItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        max_value: float = None,
        min_value: float = None,
        name: str = None,
        value: float = None,
    ):
        self.description = description
        # This parameter is required.
        self.max_value = max_value
        # This parameter is required.
        self.min_value = min_value
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

