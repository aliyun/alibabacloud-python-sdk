# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class RewriteConfig(DaraModel):
    def __init__(
        self,
        equal_rules: List[main_models.EqualRule] = None,
        regex_rules: List[main_models.RegexRule] = None,
        wildcard_rules: List[main_models.WildcardRule] = None,
    ):
        self.equal_rules = equal_rules
        self.regex_rules = regex_rules
        self.wildcard_rules = wildcard_rules

    def validate(self):
        if self.equal_rules:
            for v1 in self.equal_rules:
                 if v1:
                    v1.validate()
        if self.regex_rules:
            for v1 in self.regex_rules:
                 if v1:
                    v1.validate()
        if self.wildcard_rules:
            for v1 in self.wildcard_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['equalRules'] = []
        if self.equal_rules is not None:
            for k1 in self.equal_rules:
                result['equalRules'].append(k1.to_map() if k1 else None)

        result['regexRules'] = []
        if self.regex_rules is not None:
            for k1 in self.regex_rules:
                result['regexRules'].append(k1.to_map() if k1 else None)

        result['wildcardRules'] = []
        if self.wildcard_rules is not None:
            for k1 in self.wildcard_rules:
                result['wildcardRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.equal_rules = []
        if m.get('equalRules') is not None:
            for k1 in m.get('equalRules'):
                temp_model = main_models.EqualRule()
                self.equal_rules.append(temp_model.from_map(k1))

        self.regex_rules = []
        if m.get('regexRules') is not None:
            for k1 in m.get('regexRules'):
                temp_model = main_models.RegexRule()
                self.regex_rules.append(temp_model.from_map(k1))

        self.wildcard_rules = []
        if m.get('wildcardRules') is not None:
            for k1 in m.get('wildcardRules'):
                temp_model = main_models.WildcardRule()
                self.wildcard_rules.append(temp_model.from_map(k1))

        return self

