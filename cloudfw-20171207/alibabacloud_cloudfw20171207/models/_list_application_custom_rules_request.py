# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationCustomRulesRequest(DaraModel):
    def __init__(
        self,
        application_custom_rule_id: str = None,
        application_custom_rule_name: str = None,
        application_id: int = None,
        application_template_id: str = None,
        lang: str = None,
        page_no: int = None,
        page_size: int = None,
        priority: int = None,
        rule_action: str = None,
    ):
        # The ID of the application custom rule. Exact match is supported.
        self.application_custom_rule_id = application_custom_rule_id
        # The name of the custom rule. Fuzzy match is supported.
        self.application_custom_rule_name = application_custom_rule_name
        # The ID of the application. This parameter is used to filter custom rules associated with the application. The application must exist in the built-in application signature library.
        self.application_id = application_id
        # The ID of the application template to query. This parameter is required. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.application_template_id = application_template_id
        # The language of the returned information. Valid values:
        # - **zh**: Chinese. This is the default value.
        # - **en**: English.
        # This parameter determines whether the returned application names are in Chinese or English.
        self.lang = lang
        # The page number. Valid values: integers greater than or equal to 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: integers greater than or equal to 1. Default value: 10.
        self.page_size = page_size
        # The priority of the rule. Exact match is supported. Valid values: integers from 1 to 200.
        self.priority = priority
        # The action of the rule. Exact match is supported. Valid values:
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
        if self.application_custom_rule_id is not None:
            result['ApplicationCustomRuleId'] = self.application_custom_rule_id

        if self.application_custom_rule_name is not None:
            result['ApplicationCustomRuleName'] = self.application_custom_rule_name

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        return self

