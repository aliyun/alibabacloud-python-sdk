# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHasRuleNameByEventCodeRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_code: str = None,
        exclude_rule_id: str = None,
        reg_id: str = None,
        rule_name: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Event code
        self.event_code = event_code
        # Excluded policy ID
        self.exclude_rule_id = exclude_rule_id
        # Region code
        self.reg_id = reg_id
        # Policy name
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

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.exclude_rule_id is not None:
            result['excludeRuleId'] = self.exclude_rule_id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('excludeRuleId') is not None:
            self.exclude_rule_id = m.get('excludeRuleId')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        return self

