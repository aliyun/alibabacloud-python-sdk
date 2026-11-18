# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class CreateWebFilterRulesRequest(DaraModel):
    def __init__(
        self,
        rules: List[main_models.CreateWebFilterRulesRequestRules] = None,
        web_filter_template_id: str = None,
    ):
        # The list of web filtering rules. You can specify a maximum of 100 rules at a time, and the total number of rules in the template after creation must not exceed 100.
        # 
        # This parameter is required.
        self.rules = rules
        # The ID of the web filtering template to which the web filtering rules belong. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.web_filter_template_id = web_filter_template_id

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
        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.web_filter_template_id is not None:
            result['WebFilterTemplateId'] = self.web_filter_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateWebFilterRulesRequestRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('WebFilterTemplateId') is not None:
            self.web_filter_template_id = m.get('WebFilterTemplateId')

        return self

class CreateWebFilterRulesRequestRules(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.CreateWebFilterRulesRequestRulesConditions] = None,
        rule_action: str = None,
    ):
        # The list of matching conditions for the rule. The list must contain exactly one condition.
        self.conditions = conditions
        # The action to perform when a rule is matched. Valid values:
        # - **Allow**: allows the request.
        # - **Alert**: monitors the request.
        # - **Deny**: blocks the request.
        self.rule_action = rule_action

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

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.CreateWebFilterRulesRequestRulesConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        return self

class CreateWebFilterRulesRequestRulesConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: str = None,
    ):
        # The type of the matching condition. Only **URL** is supported, which indicates matching by URL.
        self.key = key
        # The URL to match. It cannot be empty and must not exceed 240 bytes in length (each Chinese character counts as 3 bytes). It must contain at least one forward slash (/), and the first segment must contain letters, digits, or Chinese characters. It cannot contain a protocol header, query parameters, or fragment identifiers. A single asterisk (*) indicates matching all URLs. When a wildcard is used, a maximum of one wildcard is allowed and it must end with /*. URLs within the same template cannot be duplicated.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

