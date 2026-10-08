# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskListRequest(DaraModel):
    def __init__(
        self,
        begin_create_time: int = None,
        end_create_time: int = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        user_client_ip: str = None,
    ):
        # Start time of the creation date range for the query, expressed as the number of milliseconds since 00:00 on January 1, 1970, UTC. Currently, queries are supported only by day.
        self.begin_create_time = begin_create_time
        # End time of the creation date range for the query, expressed as the number of milliseconds since 00:00 on January 1, 1970, UTC. Currently, queries are supported only by day.
        self.end_create_time = end_create_time
        # Language for API error messages. Valid values:  
        # - **zh**: Chinese.  
        # - **en**: English.  
        # 
        # Default value: **en**.
        self.lang = lang
        # Page number for paging.
        # 
        # This parameter is required.
        self.page_num = page_num
        # Page size for paging.
        # 
        # This parameter is required.
        self.page_size = page_size
        # User IP address.
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

        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')

        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

