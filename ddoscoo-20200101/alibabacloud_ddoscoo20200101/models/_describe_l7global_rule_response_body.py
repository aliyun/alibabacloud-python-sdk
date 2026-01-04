# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeL7GlobalRuleResponseBody(DaraModel):
    def __init__(
        self,
        global_rules: List[main_models.DescribeL7GlobalRuleResponseBodyGlobalRules] = None,
        request_id: str = None,
    ):
        self.global_rules = global_rules
        self.request_id = request_id

    def validate(self):
        if self.global_rules:
            for v1 in self.global_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GlobalRules'] = []
        if self.global_rules is not None:
            for k1 in self.global_rules:
                result['GlobalRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_rules = []
        if m.get('GlobalRules') is not None:
            for k1 in m.get('GlobalRules'):
                temp_model = main_models.DescribeL7GlobalRuleResponseBodyGlobalRules()
                self.global_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeL7GlobalRuleResponseBodyGlobalRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_default: str = None,
        description: str = None,
        enabled: int = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.action = action
        self.action_default = action_default
        self.description = description
        self.enabled = enabled
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_default is not None:
            result['ActionDefault'] = self.action_default

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionDefault') is not None:
            self.action_default = m.get('ActionDefault')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

