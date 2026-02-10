# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccesskeyLeakListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        query: str = None,
        resource_directory_account_id: int = None,
        start_ts: int = None,
        status: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries to return on each page.\\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The AccessKey ID that you want to query. Only exact match is supported.
        self.query = query
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to query the ID.
        self.resource_directory_account_id = resource_directory_account_id
        # The beginning of the time range to query. You can query all AccessKey pair leaks that are detected later than this time point. The value of this parameter is a UNIX timestamp. Unit: milliseconds.
        self.start_ts = start_ts
        # Specifies whether an AccessKey pair leak is handled. Valid values:
        # 
        # *   **pending**: unhandled
        # *   **dealed**: handled
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

        if self.query is not None:
            result['Query'] = self.query

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

