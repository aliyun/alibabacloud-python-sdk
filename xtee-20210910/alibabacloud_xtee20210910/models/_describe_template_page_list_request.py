# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTemplatePageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: str = None,
        event_codes: str = None,
        page_size: str = None,
        reg_id: str = None,
        template_name: str = None,
        template_search_item: str = None,
        template_status: str = None,
        template_type: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The current page number.
        self.current_page = current_page
        # The event code.
        self.event_codes = event_codes
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region code.
        self.reg_id = reg_id
        # The event name.
        self.template_name = template_name
        # The search field for event templates.
        self.template_search_item = template_search_item
        # The event status.
        self.template_status = template_status
        # The templatetype.
        self.template_type = template_type

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

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.template_search_item is not None:
            result['templateSearchItem'] = self.template_search_item

        if self.template_status is not None:
            result['templateStatus'] = self.template_status

        if self.template_type is not None:
            result['templateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('templateSearchItem') is not None:
            self.template_search_item = m.get('templateSearchItem')

        if m.get('templateStatus') is not None:
            self.template_status = m.get('templateStatus')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        return self

