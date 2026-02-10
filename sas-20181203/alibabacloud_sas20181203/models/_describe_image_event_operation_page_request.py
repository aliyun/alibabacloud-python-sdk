# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageEventOperationPageRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        event_key: str = None,
        event_name: str = None,
        event_type: str = None,
        id: int = None,
        lang: str = None,
        page_size: int = None,
        source: str = None,
    ):
        # The page number.
        self.current_page = current_page
        # The keyword of the alert item.
        self.event_key = event_key
        # The name of the alert item.
        self.event_name = event_name
        # The alert type.
        # 
        # *   Set the value to **sensitiveFile**.
        self.event_type = event_type
        # The ID of the alert handling rule.
        self.id = id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The number of entries per page.
        self.page_size = page_size
        # The source of the alert handling rule. Valid values:
        # 
        # *   **default**: image.
        # *   **agentless**: agentless detection.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.event_key is not None:
            result['EventKey'] = self.event_key

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

