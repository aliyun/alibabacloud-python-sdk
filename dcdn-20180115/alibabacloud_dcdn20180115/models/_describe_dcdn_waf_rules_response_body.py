# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[main_models.DescribeDcdnWafRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The page number of the returned page. The value of this parameter is the same as that of the PageNumber parameter in the request.
        self.page_number = page_number
        # The number of protection rules returned per page. The value of this parameter is the same as that of the PageSize parameter in the request.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The information about the protection rule.
        self.rules = rules
        # The total number of protection rules.
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeDcdnWafRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDcdnWafRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        gmt_modified: str = None,
        policy_id: int = None,
        rule_config: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_status: str = None,
    ):
        # The type of the protection policy. The value of this parameter is the same as that of the DefenseScene field in QueryArgst.
        self.defense_scene = defense_scene
        # The time when the protection policy was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the protection policy.
        self.policy_id = policy_id
        # The configuration information about the protection rule.
        self.rule_config = rule_config
        # The ID of the protection rule.
        self.rule_id = rule_id
        # The name of the protection rule.
        self.rule_name = rule_name
        # The status of the protection rule. The value of this parameter is the same as that of the RuleStatus field in QueryArgst.
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        return self

