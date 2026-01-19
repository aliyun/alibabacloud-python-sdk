# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHitRuleFluctuationRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_codes: str = None,
        reg_id: str = None,
        rule_status: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Event codes, separated by commas (,).
        self.event_codes = event_codes
        # Region code
        self.reg_id = reg_id
        # Policy status
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        return self

