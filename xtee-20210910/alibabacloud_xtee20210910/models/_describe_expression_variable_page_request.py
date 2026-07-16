# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExpressionVariablePageRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: str = None,
        event_code: str = None,
        outputs: str = None,
        page_size: str = None,
        reg_id: str = None,
        status: str = None,
        value: str = None,
    ):
        # The language type for the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The event code.
        self.event_code = event_code
        # The variable return type.
        self.outputs = outputs
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region code.
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # The status.
        self.status = status
        # The variable name or description.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.status is not None:
            result['status'] = self.status

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

