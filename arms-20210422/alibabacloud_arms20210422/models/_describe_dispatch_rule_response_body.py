# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class DescribeDispatchRuleResponseBody(DaraModel):
    def __init__(
        self,
        dispatch_rule: main_models.DescribeDispatchRuleResponseBodyDispatchRule = None,
        request_id: str = None,
    ):
        self.dispatch_rule = dispatch_rule
        self.request_id = request_id

    def validate(self):
        if self.dispatch_rule:
            self.dispatch_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            temp_model = main_models.DescribeDispatchRuleResponseBodyDispatchRule()
            self.dispatch_rule = temp_model.from_map(m.get('DispatchRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDispatchRuleResponseBodyDispatchRule(DaraModel):
    def __init__(
        self,
        group_rules: List[main_models.DescribeDispatchRuleResponseBodyDispatchRuleGroupRules] = None,
        label_match_expression_grid: main_models.DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid = None,
        name: str = None,
        notify_rules: List[main_models.DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules] = None,
        rule_id: int = None,
        state: str = None,
    ):
        self.group_rules = group_rules
        self.label_match_expression_grid = label_match_expression_grid
        self.name = name
        self.notify_rules = notify_rules
        self.rule_id = rule_id
        self.state = state

    def validate(self):
        if self.group_rules:
            for v1 in self.group_rules:
                 if v1:
                    v1.validate()
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()
        if self.notify_rules:
            for v1 in self.notify_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupRules'] = []
        if self.group_rules is not None:
            for k1 in self.group_rules:
                result['GroupRules'].append(k1.to_map() if k1 else None)

        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()

        if self.name is not None:
            result['Name'] = self.name

        result['NotifyRules'] = []
        if self.notify_rules is not None:
            for k1 in self.notify_rules:
                result['NotifyRules'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_rules = []
        if m.get('GroupRules') is not None:
            for k1 in m.get('GroupRules'):
                temp_model = main_models.DescribeDispatchRuleResponseBodyDispatchRuleGroupRules()
                self.group_rules.append(temp_model.from_map(k1))

        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = main_models.DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m.get('LabelMatchExpressionGrid'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.notify_rules = []
        if m.get('NotifyRules') is not None:
            for k1 in m.get('NotifyRules'):
                temp_model = main_models.DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules()
                self.notify_rules.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules(DaraModel):
    def __init__(
        self,
        notify_channels: List[str] = None,
        notify_objects: List[main_models.DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects] = None,
    ):
        self.notify_channels = notify_channels
        self.notify_objects = notify_objects

    def validate(self):
        if self.notify_objects:
            for v1 in self.notify_objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels

        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k1 in self.notify_objects:
                result['NotifyObjects'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')

        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k1 in m.get('NotifyObjects'):
                temp_model = main_models.DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k1))

        return self

class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects(DaraModel):
    def __init__(
        self,
        name: str = None,
        notify_object_id: str = None,
        notify_type: str = None,
    ):
        self.name = name
        self.notify_object_id = notify_object_id
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        return self

class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid(DaraModel):
    def __init__(
        self,
        label_match_expression_groups: List[main_models.DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups] = None,
    ):
        self.label_match_expression_groups = label_match_expression_groups

    def validate(self):
        if self.label_match_expression_groups:
            for v1 in self.label_match_expression_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k1 in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k1 in m.get('LabelMatchExpressionGroups'):
                temp_model = main_models.DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k1))

        return self

class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups(DaraModel):
    def __init__(
        self,
        label_match_expressions: List[main_models.DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions] = None,
    ):
        self.label_match_expressions = label_match_expressions

    def validate(self):
        if self.label_match_expressions:
            for v1 in self.label_match_expressions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k1 in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k1 in m.get('LabelMatchExpressions'):
                temp_model = main_models.DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k1))

        return self

class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeDispatchRuleResponseBodyDispatchRuleGroupRules(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        group_interval: int = None,
        group_wait_time: int = None,
        grouping_fields: List[str] = None,
    ):
        self.group_id = group_id
        self.group_interval = group_interval
        self.group_wait_time = group_wait_time
        self.grouping_fields = grouping_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval

        if self.group_wait_time is not None:
            result['GroupWaitTime'] = self.group_wait_time

        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')

        if m.get('GroupWaitTime') is not None:
            self.group_wait_time = m.get('GroupWaitTime')

        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')

        return self

