# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateAntiBruteForceRuleResponseBody(DaraModel):
    def __init__(
        self,
        create_anti_brute_force_rule: main_models.CreateAntiBruteForceRuleResponseBodyCreateAntiBruteForceRule = None,
        request_id: str = None,
    ):
        # The information about the defense rule.
        self.create_anti_brute_force_rule = create_anti_brute_force_rule
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.create_anti_brute_force_rule:
            self.create_anti_brute_force_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_anti_brute_force_rule is not None:
            result['CreateAntiBruteForceRule'] = self.create_anti_brute_force_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateAntiBruteForceRule') is not None:
            temp_model = main_models.CreateAntiBruteForceRuleResponseBodyCreateAntiBruteForceRule()
            self.create_anti_brute_force_rule = temp_model.from_map(m.get('CreateAntiBruteForceRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAntiBruteForceRuleResponseBodyCreateAntiBruteForceRule(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # The ID of the defense rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

