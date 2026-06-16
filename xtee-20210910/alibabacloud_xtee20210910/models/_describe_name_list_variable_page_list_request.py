# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNameListVariablePageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: int = None,
        name: str = None,
        name_list_type: str = None,
        page_size: int = None,
        reg_id: str = None,
        value: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The current page number.
        self.current_page = current_page
        # The variable name.
        self.name = name
        # The variable type.
        self.name_list_type = name_list_type
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region code.
        self.reg_id = reg_id
        # The named list value.
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

        if self.name is not None:
            result['name'] = self.name

        if self.name_list_type is not None:
            result['nameListType'] = self.name_list_type

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameListType') is not None:
            self.name_list_type = m.get('nameListType')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

