# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class Rule(DaraModel):
    def __init__(
        self,
        combinator: str = None,
        id: str = None,
        name: str = None,
        operator: str = None,
        rule_sub_type: str = None,
        rule_type: str = None,
        rules: List[main_models.Rule] = None,
        values: List[str] = None,
    ):
        self.combinator = combinator
        self.id = id
        self.name = name
        self.operator = operator
        self.rule_sub_type = rule_sub_type
        self.rule_type = rule_type
        self.rules = rules
        self.values = values

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
        if self.combinator is not None:
            result['Combinator'] = self.combinator

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.rule_sub_type is not None:
            result['RuleSubType'] = self.rule_sub_type

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Combinator') is not None:
            self.combinator = m.get('Combinator')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('RuleSubType') is not None:
            self.rule_sub_type = m.get('RuleSubType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.Rule()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

