# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNameListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        current_page: str = None,
        page_size: str = None,
        reg_id: str = None,
        value: str = None,
        variable_id: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Creation type.
        self.create_type = create_type
        # Current page number.
        self.current_page = current_page
        # Page size, with a default value of 10.
        self.page_size = page_size
        # Region code.
        self.reg_id = reg_id
        # Search value.
        self.value = value
        # Variable ID.
        self.variable_id = variable_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.value is not None:
            result['value'] = self.value

        if self.variable_id is not None:
            result['variableId'] = self.variable_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('variableId') is not None:
            self.variable_id = m.get('variableId')

        return self

