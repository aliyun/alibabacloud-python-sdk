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
        # The startup parameters of the process.
        self.cmdline = cmdline
        # The page number of the page to return. Default value: **1**, which indicates that the first page is returned.
        self.current_page = current_page
        # Specifies whether fuzzy match is supported for the process name. Set this parameter to 1 to enable fuzzy match. Other values or an empty value indicate that fuzzy match is not supported.
        self.extend = extend
        # The process name.
        self.name = name
        # The token that marks the current position from which to start reading. Leave this parameter empty to start reading from the beginning.
        # 
        # > You do not need to specify this parameter for the first call. The NextToken value for the second call is included in the response of the first call. Each subsequent response contains the NextToken value for the next call.
        self.next_token = next_token
        # The number of entries per page in a paged query. Default value: **10**, which indicates that 10 entries of process Asset Fingerprints information are displayed per page.
        self.page_size = page_size
        # The end timestamp of the process startup time range. Unit: milliseconds.
        self.proc_time_end = proc_time_end
        # The start timestamp of the process startup time range. Unit: milliseconds.
        self.proc_time_start = proc_time_start
        # The name or IP address of the server that you want to query.
        self.remark = remark
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # >You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to use the NextToken method to retrieve the vulnerability list data. If this parameter is used, TotalCount is no longer returned. Valid values:
        # 
        # - **true**: Use the NextToken method.
        # - **false**: Do not use the NextToken method.
        self.use_next_token = use_next_token
        # The information about the user that runs the process.
        self.user = user
        # The UUID of the server that you want to query.
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

