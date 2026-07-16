# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNameListPageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: int = None,
        page_size: int = None,
        reg_id: str = None,
        update_begin_time: int = None,
        update_end_time: int = None,
        value: str = None,
        variable_id: int = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The current page number.
        self.current_page = current_page
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region code.
        self.reg_id = reg_id
        # The start time of the update period.
        self.update_begin_time = update_begin_time
        # The end time of the update period.
        self.update_end_time = update_end_time
        # The variable name or description.
        self.value = value
        # The variable ID.
        # 
        # This parameter is required.
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

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.update_begin_time is not None:
            result['updateBeginTime'] = self.update_begin_time

        if self.update_end_time is not None:
            result['updateEndTime'] = self.update_end_time

        if self.value is not None:
            result['value'] = self.value

        if self.variable_id is not None:
            result['variableId'] = self.variable_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('updateBeginTime') is not None:
            self.update_begin_time = m.get('updateBeginTime')

        if m.get('updateEndTime') is not None:
            self.update_end_time = m.get('updateEndTime')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('variableId') is not None:
            self.variable_id = m.get('variableId')

        return self

