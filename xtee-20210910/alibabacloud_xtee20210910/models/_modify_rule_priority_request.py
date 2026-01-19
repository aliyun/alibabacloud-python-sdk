# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRulePriorityRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        console_rule_id: int = None,
        priority: int = None,
        reg_id: str = None,
        rule_id: int = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Primary key ID of the policy
        self.console_rule_id = console_rule_id
        # Policy priority, the higher the number, the higher the priority.
        self.priority = priority
        # Region code
        self.reg_id = reg_id
        # Policy ID
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.console_rule_id is not None:
            result['consoleRuleId'] = self.console_rule_id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        return self

