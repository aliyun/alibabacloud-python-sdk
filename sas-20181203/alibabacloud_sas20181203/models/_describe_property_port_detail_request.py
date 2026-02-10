# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyPortDetailRequest(DaraModel):
    def __init__(
        self,
        bind_ip: str = None,
        current_page: int = None,
        extend: str = None,
        next_token: str = None,
        page_size: int = None,
        port: str = None,
        proc_name: str = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        use_next_token: bool = None,
        uuid: str = None,
    ):
        # The IP address bound to the port.
        self.bind_ip = bind_ip
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether fuzzy search by port number is supported. If you want to use fuzzy search, set the parameter to **1**. If you set the parameter to a different value or leave the parameter empty, fuzzy search is not supported.
        self.extend = extend
        # The value of NextToken that is returned when the NextToken method is used. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The listening port of the server.
        self.port = port
        # The name of the server process.
        self.proc_name = proc_name
        # The name or IP address of the server.
        self.remark = remark
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # Specifies whether to use the NextToken method to retrieve a new page of results. If you set UseNextToken to true, the value of TotalCount is not returned. Valid values:
        # 
        # - **true**: The NextToken method is used.
        # - **false**: The NextToken method is not used.
        self.use_next_token = use_next_token
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_ip is not None:
            result['BindIp'] = self.bind_ip

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.proc_name is not None:
            result['ProcName'] = self.proc_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindIp') is not None:
            self.bind_ip = m.get('BindIp')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProcName') is not None:
            self.proc_name = m.get('ProcName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

