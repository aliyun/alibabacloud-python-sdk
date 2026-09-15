# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyCronDetailRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        extend: str = None,
        next_token: str = None,
        page_size: int = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        source: str = None,
        use_next_token: bool = None,
        user: str = None,
        uuid: str = None,
    ):
        # The page number of the page to return. Default value: **1**, which indicates that the first page is returned.
        self.current_page = current_page
        # Specifies whether fuzzy match is supported for the scheduled task path. Set this parameter to **1** to enable fuzzy match. Other values or an empty value indicate that fuzzy match is not supported.
        self.extend = extend
        # The pagination token that marks the position from which you want to start reading. Leave this parameter empty to read from the beginning.
        # 
        # > You do not need to specify this parameter for the first call. The response includes the NextToken value for the second call. Each subsequent response includes the NextToken value for the next call.
        self.next_token = next_token
        # Settings the number of scheduled task asset fingerprint information entries displayed per page in a paging query. Default value: **10**, which indicates that 10 entries of scheduled task asset fingerprint information are displayed per page.
        self.page_size = page_size
        # The name or IP address of the server that you want to query.
        self.remark = remark
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # >Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The task path that you want to query.
        self.source = source
        # Specifies whether to use the NextToken method to retrieve the vulnerability list data. If you use this parameter, TotalCount is no longer returned. Valid values:
        # 
        # - **true**: Use the NextToken method.
        # - **false**: Do not use the NextToken method.
        self.use_next_token = use_next_token
        # The account name of the scheduled task that you want to query.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source is not None:
            result['Source'] = self.source

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        if self.user is not None:
            result['User'] = self.user

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

