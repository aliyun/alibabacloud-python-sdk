# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebLockProcessListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        process_name: str = None,
        status: int = None,
    ):
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The name of the process.
        self.process_name = process_name
        # Specifies whether the process is added to the process whitelist. Valid values:
        # 
        # *   **1**: The process is added to the process whitelist.
        # *   **0**: The process is not added to the process whitelist.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

