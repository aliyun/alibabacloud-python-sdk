# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[main_models.ListRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The authorization rules that are returned.
        self.rules = rules
        # The total number of authorization rules that are returned.
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
                temp_model = main_models.ListRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        comment: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_state: str = None,
    ):
        # The remarks of the authorization rule.
        self.comment = comment
        # The end time of the validity period of the authorization rule. The value is a timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The start time of the validity period of the authorization rule. The value is a timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The authorization rule ID.
        self.rule_id = rule_id
        # The name of the authorization rule.
        self.rule_name = rule_name
        # The state of the authorization rule.
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.rule_state = rule_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_state is not None:
            result['RuleState'] = self.rule_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleState') is not None:
            self.rule_state = m.get('RuleState')

        return self

