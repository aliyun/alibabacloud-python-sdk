# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ListApplicationCustomRulesResponseBody(DaraModel):
    def __init__(
        self,
        application_custom_rules: List[main_models.ListApplicationCustomRulesResponseBodyApplicationCustomRules] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of application custom rules, sorted by priority in ascending order.
        self.application_custom_rules = application_custom_rules
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of application custom rules that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.application_custom_rules:
            for v1 in self.application_custom_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationCustomRules'] = []
        if self.application_custom_rules is not None:
            for k1 in self.application_custom_rules:
                result['ApplicationCustomRules'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_custom_rules = []
        if m.get('ApplicationCustomRules') is not None:
            for k1 in m.get('ApplicationCustomRules'):
                temp_model = main_models.ListApplicationCustomRulesResponseBodyApplicationCustomRules()
                self.application_custom_rules.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationCustomRulesResponseBodyApplicationCustomRules(DaraModel):
    def __init__(
        self,
        application_custom_rule_id: str = None,
        application_custom_rule_name: str = None,
        application_template_id: str = None,
        applications: List[main_models.ListApplicationCustomRulesResponseBodyApplicationCustomRulesApplications] = None,
        priority: int = None,
        rule_action: str = None,
    ):
        # The ID of the application custom rule.
        self.application_custom_rule_id = application_custom_rule_id
        # The name of the custom rule.
        self.application_custom_rule_name = application_custom_rule_name
        # The ID of the application template to which the rule belongs.
        self.application_template_id = application_template_id
        # The list of applications associated with the rule.
        self.applications = applications
        # The priority of the rule. Valid values: integers from 1 to 200. A smaller value indicates a higher priority.
        self.priority = priority
        # The action performed after the rule is matched. Valid values:
        # - **Allow**: allows the traffic.
        # - **Alert**: monitors the traffic.
        # - **Deny**: blocks the traffic.
        self.rule_action = rule_action

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_custom_rule_id is not None:
            result['ApplicationCustomRuleId'] = self.application_custom_rule_id

        if self.application_custom_rule_name is not None:
            result['ApplicationCustomRuleName'] = self.application_custom_rule_name

        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCustomRuleId') is not None:
            self.application_custom_rule_id = m.get('ApplicationCustomRuleId')

        if m.get('ApplicationCustomRuleName') is not None:
            self.application_custom_rule_name = m.get('ApplicationCustomRuleName')

        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationCustomRulesResponseBodyApplicationCustomRulesApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        return self

class ListApplicationCustomRulesResponseBodyApplicationCustomRulesApplications(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        application_name: str = None,
    ):
        # The ID of the application in the built-in application signature library.
        self.application_id = application_id
        # The name of the application. The name is returned in Chinese or English based on the Lang parameter.
        self.application_name = application_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        return self

