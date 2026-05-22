# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeHttpDDoSIntelligentAclRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rule_infos: List[main_models.DescribeHttpDDoSIntelligentAclRulesResponseBodyRuleInfos] = None,
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
                temp_model = main_models.DescribeHttpDDoSIntelligentAclRulesResponseBodyRuleInfos()
                self.rule_infos.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHttpDDoSIntelligentAclRulesResponseBodyRuleInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        condition: str = None,
        log_rule_id: int = None,
        punish_time: int = None,
        record_name: str = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.action = action
        self.condition = condition
        self.log_rule_id = log_rule_id
        self.punish_time = punish_time
        self.record_name = record_name
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.condition is not None:
            result['Condition'] = self.condition

        if self.log_rule_id is not None:
            result['LogRuleId'] = self.log_rule_id

        if self.punish_time is not None:
            result['PunishTime'] = self.punish_time

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('LogRuleId') is not None:
            self.log_rule_id = m.get('LogRuleId')

        if m.get('PunishTime') is not None:
            self.punish_time = m.get('PunishTime')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

