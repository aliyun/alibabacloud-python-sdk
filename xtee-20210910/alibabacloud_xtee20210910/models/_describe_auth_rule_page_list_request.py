# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuthRulePageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_code: str = None,
        reg_id: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Event code
        self.event_code = event_code
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Policy name
        self.rule_name = rule_name
        # Status.
        self.status = status

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

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

