# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRuleBaseRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        console_rule_id: int = None,
        event_code: str = None,
        memo: str = None,
        reg_id: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The primary key ID of the policy.
        self.console_rule_id = console_rule_id
        # The event code.
        self.event_code = event_code
        # The description.
        self.memo = memo
        # The region code.
        self.reg_id = reg_id
        # The policy ID.
        self.rule_id = rule_id
        # The policy name.
        self.rule_name = rule_name

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

        if self.memo is not None:
            result['memo'] = self.memo

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        return self

