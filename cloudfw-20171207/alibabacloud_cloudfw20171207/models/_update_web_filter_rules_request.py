# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class UpdateWebFilterRulesRequest(DaraModel):
    def __init__(
        self,
        rules: List[main_models.UpdateWebFilterRulesRequestRules] = None,
    ):
        # The list of web filtering rules to be updated. You can specify up to 20 rules at a time. The rule IDs in the list must be unique.
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
        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateWebFilterRulesRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdateWebFilterRulesRequestRules(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.UpdateWebFilterRulesRequestRulesConditions] = None,
        rule_action: str = None,
        web_filter_rule_id: str = None,
    ):
        # The list of match conditions for the rule. The list must contain exactly one condition. After the update, URLs within the same template must be unique.
        self.conditions = conditions
        # The action to perform when the rule is matched. Valid values:
        # - **Allow**: allows the request.
        # - **Alert**: monitors the request.
        # - **Deny**: blocks the request.
        self.rule_action = rule_action
        # The ID of the web filtering rule to be updated. The rule must exist within the current Alibaba Cloud account.
        self.web_filter_rule_id = web_filter_rule_id

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

        if self.web_filter_rule_id is not None:
            result['WebFilterRuleId'] = self.web_filter_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.UpdateWebFilterRulesRequestRulesConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('WebFilterRuleId') is not None:
            self.web_filter_rule_id = m.get('WebFilterRuleId')

        return self

class UpdateWebFilterRulesRequestRulesConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: str = None,
    ):
        # The type of the match condition. Only **URL** is supported, which indicates matching by URL.
        self.key = key
        # The URL to match. The value cannot be empty and must not exceed 240 bytes in length. Each Chinese character is counted as 3 bytes. The URL must contain at least one forward slash (/), and the first segment must contain letters, digits, or Chinese characters. The URL cannot contain a protocol header, query parameters, or fragment identifiers. A single asterisk (*) matches all URLs. If a wildcard is used, only one wildcard is allowed and it must end with /*. URLs within the same template must be unique.
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

