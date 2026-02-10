# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMaliciousFileWhitelistConfigsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        event_name: str = None,
        id_list: int = None,
        lang: str = None,
        page_size: int = None,
        source: str = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The name of the alert.
        # 
        # *   Set the value to ALL, which indicates all alert types.
        self.event_name = event_name
        # Event ID. <notice>Field is deprecated.</notice>
        self.id_list = id_list
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The feature to which this operation belongs. If you leave this parameter empty, the default value agentless is used.
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

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.id_list is not None:
            result['IdList'] = self.id_list

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

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

