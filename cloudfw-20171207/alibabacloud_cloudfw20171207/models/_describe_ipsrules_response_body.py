# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeIPSRulesResponseBody(DaraModel):
    def __init__(
        self,
        drop_count: int = None,
        high_risk_count: int = None,
        open_count: int = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[main_models.DescribeIPSRulesResponseBodyRules] = None,
        total_count: int = None,
        user_define_count: int = None,
    ):
        # The number of rules that have the `drop` action.
        self.drop_count = drop_count
        # The number of high-risk rules.
        self.high_risk_count = high_risk_count
        # The total number of enabled rules.
        self.open_count = open_count
        # The page number.
        self.page_no = page_no
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of rules.
        self.rules = rules
        # The total number of entries.
        self.total_count = total_count
        # The total number of user-defined rules.
        self.user_define_count = user_define_count

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
        if self.drop_count is not None:
            result['DropCount'] = self.drop_count

        if self.high_risk_count is not None:
            result['HighRiskCount'] = self.high_risk_count

        if self.open_count is not None:
            result['OpenCount'] = self.open_count

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_define_count is not None:
            result['UserDefineCount'] = self.user_define_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DropCount') is not None:
            self.drop_count = m.get('DropCount')

        if m.get('HighRiskCount') is not None:
            self.high_risk_count = m.get('HighRiskCount')

        if m.get('OpenCount') is not None:
            self.open_count = m.get('OpenCount')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeIPSRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserDefineCount') is not None:
            self.user_define_count = m.get('UserDefineCount')

        return self

class DescribeIPSRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        attack_app: str = None,
        attack_type: str = None,
        current_mode: str = None,
        cve: str = None,
        default_mode: str = None,
        description: str = None,
        rule_class: int = None,
        rule_id: str = None,
        rule_level: int = None,
        rule_name: str = None,
        rule_uuid: str = None,
        update_time: int = None,
        user_defined: str = None,
        user_status: int = None,
    ):
        # The target application.
        self.attack_app = attack_app
        # The attack type.
        self.attack_type = attack_type
        # The current action.
        self.current_mode = current_mode
        # The CVE ID.
        self.cve = cve
        # The default action.
        self.default_mode = default_mode
        # A description of the rule.
        self.description = description
        # The engine mode.
        # 
        # This parameter takes effect only when `DefaultMode` is set to `drop`.
        self.rule_class = rule_class
        # The rule ID.
        self.rule_id = rule_id
        # The rule level.
        self.rule_level = rule_level
        # The rule name.
        self.rule_name = rule_name
        # The rule UUID.
        self.rule_uuid = rule_uuid
        # The UNIX timestamp for when the rule was last updated.
        self.update_time = update_time
        # Specifies whether the rule is user-defined.
        self.user_defined = user_defined
        # The user-defined status of the rule.
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.current_mode is not None:
            result['CurrentMode'] = self.current_mode

        if self.cve is not None:
            result['Cve'] = self.cve

        if self.default_mode is not None:
            result['DefaultMode'] = self.default_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_level is not None:
            result['RuleLevel'] = self.rule_level

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_uuid is not None:
            result['RuleUuid'] = self.rule_uuid

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_defined is not None:
            result['UserDefined'] = self.user_defined

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('CurrentMode') is not None:
            self.current_mode = m.get('CurrentMode')

        if m.get('Cve') is not None:
            self.cve = m.get('Cve')

        if m.get('DefaultMode') is not None:
            self.default_mode = m.get('DefaultMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleLevel') is not None:
            self.rule_level = m.get('RuleLevel')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleUuid') is not None:
            self.rule_uuid = m.get('RuleUuid')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserDefined') is not None:
            self.user_defined = m.get('UserDefined')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

