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
        # The page number of the current page to return. Minimum value: 1. Default value: 1.
        self.current_page = current_page
        # The alerting name. Valid values:
        # - ALL: all Alarm Metric values.
        self.event_name = event_name
        # The event ID.
        # 
        # >Notice: This field is deprecated..
        self.id_list = id_list
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return per page in a paging query. Default value: 20.
        self.page_size = page_size
        # The business source. This parameter can be left empty. Default value: agentless.
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

