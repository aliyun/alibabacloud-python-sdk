# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuthRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        console_rule_id: int = None,
        event_code: str = None,
        reg_id: str = None,
        rule_actions: str = None,
        rule_expressions: str = None,
        rule_id: str = None,
        rule_version_id: int = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Policy primary key ID
        self.console_rule_id = console_rule_id
        # Event code
        self.event_code = event_code
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Policy output action
        self.rule_actions = rule_actions
        # Expression
        # 
        # This parameter is required.
        self.rule_expressions = rule_expressions
        # Policy ID
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # Policy version primary key ID
        self.rule_version_id = rule_version_id

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

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_actions is not None:
            result['ruleActions'] = self.rule_actions

        if self.rule_expressions is not None:
            result['ruleExpressions'] = self.rule_expressions

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_version_id is not None:
            result['ruleVersionId'] = self.rule_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleActions') is not None:
            self.rule_actions = m.get('ruleActions')

        if m.get('ruleExpressions') is not None:
            self.rule_expressions = m.get('ruleExpressions')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleVersionId') is not None:
            self.rule_version_id = m.get('ruleVersionId')

        return self

