# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        metric_operation_type: str = None,
        metric_pull_info: str = None,
        metric_pull_period: str = None,
        name: str = None,
        rule_computing_definition: str = None,
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

    def validate(self):
        pass

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

        return self

