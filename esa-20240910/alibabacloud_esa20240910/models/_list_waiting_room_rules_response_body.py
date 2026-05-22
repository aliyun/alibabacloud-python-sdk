# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWaitingRoomRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_room_rules: List[main_models.ListWaitingRoomRulesResponseBodyWaitingRoomRules] = None,
    ):
        # Request ID, used for tracking the call status.
        self.request_id = request_id
        # List of waiting room bypass rules.
        self.waiting_room_rules = waiting_room_rules

    def validate(self):
        if self.waiting_room_rules:
            for v1 in self.waiting_room_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['WaitingRoomRules'] = []
        if self.waiting_room_rules is not None:
            for k1 in self.waiting_room_rules:
                result['WaitingRoomRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.waiting_room_rules = []
        if m.get('WaitingRoomRules') is not None:
            for k1 in m.get('WaitingRoomRules'):
                temp_model = main_models.ListWaitingRoomRulesResponseBodyWaitingRoomRules()
                self.waiting_room_rules.append(temp_model.from_map(k1))

        return self

class ListWaitingRoomRulesResponseBodyWaitingRoomRules(DaraModel):
    def __init__(
        self,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        waiting_room_rule_id: int = None,
    ):
        # Rule content, using conditional expressions to match user requests. This parameter does not need to be set when adding global configuration. There are two usage scenarios:
        # - Match all incoming requests: set the value to true
        # - Match specific requests: set the value to a custom expression, e.g., (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter does not need to be set when adding global configuration. Value range:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # Rule name. This parameter does not need to be set when adding global configuration.
        self.rule_name = rule_name
        # Rule ID.
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')

        return self

