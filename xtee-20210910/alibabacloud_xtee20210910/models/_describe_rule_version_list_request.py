# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRuleVersionListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        console_rule_id: int = None,
        current_page: int = None,
        page_size: int = None,
        reg_id: str = None,
        rule_id: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The primary key ID of the policy.
        self.console_rule_id = console_rule_id
        # The current page number.
        self.current_page = current_page
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region code.
        self.reg_id = reg_id
        # The policy ID.
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

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

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

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        return self

