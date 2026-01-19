# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQueryVariablePageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: int = None,
        data_source_code: str = None,
        event_code: str = None,
        name: str = None,
        page_size: int = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Current page number.
        self.current_page = current_page
        # Data source code
        self.data_source_code = data_source_code
        # Event code
        self.event_code = event_code
        # Query variable name
        self.name = name
        # Page size, default value is 10
        self.page_size = page_size
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id

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

        if self.data_source_code is not None:
            result['dataSourceCode'] = self.data_source_code

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.name is not None:
            result['name'] = self.name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('dataSourceCode') is not None:
            self.data_source_code = m.get('dataSourceCode')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

