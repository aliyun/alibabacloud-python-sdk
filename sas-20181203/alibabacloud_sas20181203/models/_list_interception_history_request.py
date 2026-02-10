# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListInterceptionHistoryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_page: int = None,
        end_time: int = None,
        history_name: str = None,
        interception_types: List[int] = None,
        lang: str = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The number of the page to return.
        self.current_page = current_page
        # The end of the time range to query. The value is a UNIX timestamp.
        self.end_time = end_time
        # The name of the alert.
        self.history_name = history_name
        # The types of exceptions.
        self.interception_types = interception_types
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        self.page_size = page_size
        # The start of the time range to query. The value is a UNIX timestamp.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.history_name is not None:
            result['HistoryName'] = self.history_name

        if self.interception_types is not None:
            result['InterceptionTypes'] = self.interception_types

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HistoryName') is not None:
            self.history_name = m.get('HistoryName')

        if m.get('InterceptionTypes') is not None:
            self.interception_types = m.get('InterceptionTypes')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

