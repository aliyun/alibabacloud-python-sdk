# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAdvanceSearchPageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        condition: str = None,
        current_page: int = None,
        event_begin_time: int = None,
        event_codes: str = None,
        event_end_time: int = None,
        field_name: str = None,
        field_value: str = None,
        page_size: int = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Condition value.
        self.condition = condition
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Query start time, accurate to milliseconds (ms).
        # 
        # This parameter is required.
        self.event_begin_time = event_begin_time
        # Event code.
        # 
        # This parameter is required.
        self.event_codes = event_codes
        # End time, accurate to milliseconds (ms).
        # 
        # This parameter is required.
        self.event_end_time = event_end_time
        # Field name
        self.field_name = field_name
        # Field value
        self.field_value = field_value
        # Page size, default value is 10
        # 
        # This parameter is required.
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

        if self.condition is not None:
            result['condition'] = self.condition

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.event_begin_time is not None:
            result['eventBeginTime'] = self.event_begin_time

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.event_end_time is not None:
            result['eventEndTime'] = self.event_end_time

        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.field_value is not None:
            result['fieldValue'] = self.field_value

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('eventBeginTime') is not None:
            self.event_begin_time = m.get('eventBeginTime')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('eventEndTime') is not None:
            self.event_end_time = m.get('eventEndTime')

        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

