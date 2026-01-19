# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        console_rule_id: int = None,
        create_type: str = None,
        event_code: str = None,
        event_name: str = None,
        logic_expression: str = None,
        memo: str = None,
        reg_id: str = None,
        rule_actions: str = None,
        rule_body: str = None,
        rule_expressions: str = None,
        rule_name: str = None,
        rule_status: str = None,
        rule_type: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Rule ID.
        self.console_rule_id = console_rule_id
        # Creation type
        self.create_type = create_type
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Policy expression execution logic
        self.logic_expression = logic_expression
        # Memo
        self.memo = memo
        # Region code
        self.reg_id = reg_id
        # Policy execution output action
        self.rule_actions = rule_actions
        # DSL policy execution logic
        self.rule_body = rule_body
        # Policy expression
        self.rule_expressions = rule_expressions
        # Policy name
        self.rule_name = rule_name
        # Policy status
        self.rule_status = rule_status
        # Policy type
        self.rule_type = rule_type

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

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.logic_expression is not None:
            result['logicExpression'] = self.logic_expression

        if self.memo is not None:
            result['memo'] = self.memo

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_actions is not None:
            result['ruleActions'] = self.rule_actions

        if self.rule_body is not None:
            result['ruleBody'] = self.rule_body

        if self.rule_expressions is not None:
            result['ruleExpressions'] = self.rule_expressions

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        if self.rule_type is not None:
            result['ruleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('logicExpression') is not None:
            self.logic_expression = m.get('logicExpression')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleActions') is not None:
            self.rule_actions = m.get('ruleActions')

        if m.get('ruleBody') is not None:
            self.rule_body = m.get('ruleBody')

        if m.get('ruleExpressions') is not None:
            self.rule_expressions = m.get('ruleExpressions')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')

        return self

