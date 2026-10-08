# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskInfoHistoryRequest(DaraModel):
    def __init__(
        self,
        begin_create_time: int = None,
        create_time_cursor: int = None,
        end_create_time: int = None,
        lang: str = None,
        page_size: int = None,
        task_no_cursor: str = None,
        user_client_ip: str = None,
    ):
        # Start time of the creation date range for the query, expressed as the number of milliseconds since 00:00 UTC on January 1, 1970. Currently supports queries by day only.
        self.begin_create_time = begin_create_time
        # Cursor for creation date (technical parameter).
        self.create_time_cursor = create_time_cursor
        # End time of the creation date range for the query, expressed as the number of milliseconds since 00:00 UTC on January 1, 1970. Currently supports queries by day only.
        self.end_create_time = end_create_time
        # Language for API error messages. Valid values:  
        # - **zh**: Chinese  
        # - **en**: English  
        # 
        # Default value is **en**.
        self.lang = lang
        # Page size.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Job cursor; pass in the job number from the corresponding page cursor during pagination (technical parameter).
        self.task_no_cursor = task_no_cursor
        # User IP address, which can be set to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time

        if self.create_time_cursor is not None:
            result['CreateTimeCursor'] = self.create_time_cursor

        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_no_cursor is not None:
            result['TaskNoCursor'] = self.task_no_cursor

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')

        if m.get('CreateTimeCursor') is not None:
            self.create_time_cursor = m.get('CreateTimeCursor')

        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskNoCursor') is not None:
            self.task_no_cursor = m.get('TaskNoCursor')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

