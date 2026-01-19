# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeHttpDDoSAttackRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rule_infos: List[main_models.DescribeHttpDDoSAttackRulesResponseBodyRuleInfos] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.rule_infos = rule_infos
        self.total_count = total_count

    def validate(self):
        if self.rule_infos:
            for v1 in self.rule_infos:
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

        result['RuleInfos'] = []
        if self.rule_infos is not None:
            for k1 in self.rule_infos:
                result['RuleInfos'].append(k1.to_map() if k1 else None)

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

        self.rule_infos = []
        if m.get('RuleInfos') is not None:
            for k1 in m.get('RuleInfos'):
                temp_model = main_models.DescribeHttpDDoSAttackRulesResponseBodyRuleInfos()
                self.rule_infos.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHttpDDoSAttackRulesResponseBodyRuleInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        default_action: str = None,
        log_rule_id: int = None,
        rule_desc: str = None,
        rule_id: int = None,
        rule_id_info: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        self.action = action
        self.default_action = default_action
        self.log_rule_id = log_rule_id
        self.rule_desc = rule_desc
        self.rule_id = rule_id
        self.rule_id_info = rule_id_info
        self.rule_name = rule_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.default_action is not None:
            result['DefaultAction'] = self.default_action

        if self.log_rule_id is not None:
            result['LogRuleId'] = self.log_rule_id

        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_id_info is not None:
            result['RuleIdInfo'] = self.rule_id_info

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('DefaultAction') is not None:
            self.default_action = m.get('DefaultAction')

        if m.get('LogRuleId') is not None:
            self.log_rule_id = m.get('LogRuleId')

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleIdInfo') is not None:
            self.rule_id_info = m.get('RuleIdInfo')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

