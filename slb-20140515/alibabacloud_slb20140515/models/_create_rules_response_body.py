# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class CreateRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rules: main_models.CreateRulesResponseBodyRules = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The forwarding rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rules') is not None:
            temp_model = main_models.CreateRulesResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class CreateRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.CreateRulesResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.CreateRulesResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class CreateRulesResponseBodyRulesRule(DaraModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The forwarding rule ID.
        self.rule_id = rule_id
        # The name of the forwarding rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

