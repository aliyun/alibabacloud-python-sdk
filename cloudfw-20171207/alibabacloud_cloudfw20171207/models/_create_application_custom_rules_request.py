# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationCustomRulesRequest(DaraModel):
    def __init__(
        self,
        application_template_id: str = None,
        rules: List[main_models.CreateApplicationCustomRulesRequestRules] = None,
    ):
        # The ID of the application template to which the custom rules belong. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.application_template_id = application_template_id
        # The list of custom rules for the application. You can specify up to 100 rules at a time, and the total number of rules in the template after creation must not exceed 100.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateApplicationCustomRulesRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreateApplicationCustomRulesRequestRules(DaraModel):
    def __init__(
        self,
        application_custom_rule_name: str = None,
        application_ids: List[int] = None,
        priority: int = None,
        rule_action: str = None,
    ):
        # The name of the custom rule. The name cannot be empty and can be up to 64 characters in length. It can contain Chinese characters, English letters, digits, hyphens (-), underscores (_), and periods (.).
        self.application_custom_rule_name = application_custom_rule_name
        # The list of application IDs associated with the rule. A single rule can be associated with 1 to 200 applications. The IDs cannot be 0, must be unique, and must exist in the built-in application signature library. You can call the ListApplications operation to query the IDs.
        self.application_ids = application_ids
        # The priority of the rule. Valid values: integers from 1 to 200. A smaller value indicates a higher priority. Priorities must be unique within the same batch and the same template.
        self.priority = priority
        # The action to perform when the rule is matched. Valid values:
        # - **Allow**: allows the traffic.
        # - **Alert**: monitors the traffic.
        # - **Deny**: blocks the traffic.
        self.rule_action = rule_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_custom_rule_name is not None:
            result['ApplicationCustomRuleName'] = self.application_custom_rule_name

        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCustomRuleName') is not None:
            self.application_custom_rule_name = m.get('ApplicationCustomRuleName')

        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        return self

