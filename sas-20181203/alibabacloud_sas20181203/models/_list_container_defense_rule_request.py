# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListContainerDefenseRuleRequest(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.ListContainerDefenseRuleRequestConditions] = None,
        current_page: int = None,
        is_default_rule: int = None,
        lang: str = None,
        page_size: int = None,
        rule_type: int = None,
    ):
        # The details of the condition.
        self.conditions = conditions
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether to query system rules.
        # 
        # >  This parameter is deprecated.
        self.is_default_rule = is_default_rule
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The rule type. Valid values:
        # 
        # *   1: system rule
        # *   2: user-defined rule
        self.rule_type = rule_type

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.is_default_rule is not None:
            result['IsDefaultRule'] = self.is_default_rule

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ListContainerDefenseRuleRequestConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IsDefaultRule') is not None:
            self.is_default_rule = m.get('IsDefaultRule')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

class ListContainerDefenseRuleRequestConditions(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The condition type. Valid values:
        # 
        # *   **ruleName**: the rule name
        self.type = type
        # The rule content.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

