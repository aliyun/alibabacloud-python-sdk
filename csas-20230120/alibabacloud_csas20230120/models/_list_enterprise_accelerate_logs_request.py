# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnterpriseAccelerateLogsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        department: str = None,
        dst_addr: str = None,
        end_time: int = None,
        page_size: int = None,
        search_mode: str = None,
        start_time: int = None,
        username: str = None,
    ):
        # The current page number displayed during paged queries. Value range: 1 to 10000.
        self.current_page = current_page
        # Department.
        self.department = department
        # Endpoint.
        self.dst_addr = dst_addr
        # End time, UNIX timestamp, in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of items per page for paged queries. Value range: 1 to 1000.
        self.page_size = page_size
        # Query mode. Only the DstAddr field supports the following modes:
        # 
        # - **Exact**: Term query
        # 
        # - **Fuzzy**: Fuzzy query
        self.search_mode = search_mode
        # Start time, UNIX timestamp, in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department is not None:
            result['Department'] = self.department

        if self.dst_addr is not None:
            result['DstAddr'] = self.dst_addr

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DstAddr') is not None:
            self.dst_addr = m.get('DstAddr')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

