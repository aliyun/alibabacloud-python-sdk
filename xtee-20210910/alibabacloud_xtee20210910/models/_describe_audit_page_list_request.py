# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditPageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        audit_status: str = None,
        current_page: str = None,
        event_code: str = None,
        page_size: str = None,
        reg_id: str = None,
        rule_name: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Audit status
        self.audit_status = audit_status
        # Current page number.
        self.current_page = current_page
        # Event code
        self.event_code = event_code
        # Page size, default value is 10
        self.page_size = page_size
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

        if self.audit_status is not None:
            result['auditStatus'] = self.audit_status

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('auditStatus') is not None:
            self.audit_status = m.get('auditStatus')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        return self

