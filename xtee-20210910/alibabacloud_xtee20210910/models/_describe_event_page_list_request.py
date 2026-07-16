# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventPageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        current_page: int = None,
        event_code: str = None,
        event_name: str = None,
        event_status: str = None,
        page_size: int = None,
        reg_id: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The creation type.
        self.create_type = create_type
        # The current page number.
        self.current_page = current_page
        # The event code.
        self.event_code = event_code
        # The event name.
        self.event_name = event_name
        # The event status.
        self.event_status = event_status
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region code.
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

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_status is not None:
            result['eventStatus'] = self.event_status

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventStatus') is not None:
            self.event_status = m.get('eventStatus')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

