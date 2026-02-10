# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyProcDetailRequest(DaraModel):
    def __init__(
        self,
        cmdline: str = None,
        current_page: int = None,
        extend: str = None,
        name: str = None,
        next_token: str = None,
        page_size: int = None,
        proc_time_end: int = None,
        proc_time_start: int = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        use_next_token: bool = None,
        user: str = None,
        uuid: str = None,
    ):
        # The startup parameter of the process.
        self.cmdline = cmdline
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether fuzzy search by process name is supported. If you want to use fuzzy search, set the parameter to 1. If you set the parameter to a different value or leave the parameter empty, fuzzy search is not supported.
        self.extend = extend
        # The name of the process.
        self.name = name
        # The value of NextToken that is returned when the NextToken method is used. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The timestamp when the process ends. Unit: milliseconds.
        self.proc_time_end = proc_time_end
        # The timestamp when the process starts. Unit: milliseconds.
        self.proc_time_start = proc_time_start
        # The name or IP address of the server.
        self.remark = remark
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to query the account ID.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to use the NextToken method to retrieve a new page of results. If you set UseNextToken to true, the value of TotalCount is not returned. Valid values:
        # 
        # - **true**: The NextToken method is used.
        # - **false**: The NextToken method is not used.
        self.use_next_token = use_next_token
        # The user who runs the process.
        self.user = user
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proc_time_end is not None:
            result['ProcTimeEnd'] = self.proc_time_end

        if self.proc_time_start is not None:
            result['ProcTimeStart'] = self.proc_time_start

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        if self.user is not None:
            result['User'] = self.user

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcTimeEnd') is not None:
            self.proc_time_end = m.get('ProcTimeEnd')

        if m.get('ProcTimeStart') is not None:
            self.proc_time_start = m.get('ProcTimeStart')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

