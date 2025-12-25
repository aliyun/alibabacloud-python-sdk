# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeBaseSystemRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[main_models.DescribeBaseSystemRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.rules = rules
        self.total_count = total_count

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeBaseSystemRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBaseSystemRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        cve_id: str = None,
        description: str = None,
        detect_type: str = None,
        risk_level: str = None,
        rule_action: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_status: int = None,
        update_time: int = None,
    ):
        self.cve_id = cve_id
        self.description = description
        self.detect_type = detect_type
        self.risk_level = risk_level
        self.rule_action = rule_action
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_status = rule_status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.description is not None:
            result['Description'] = self.description

        if self.detect_type is not None:
            result['DetectType'] = self.detect_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetectType') is not None:
            self.detect_type = m.get('DetectType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

