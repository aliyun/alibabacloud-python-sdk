# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyUserDetailRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        extend: str = None,
        is_root: str = None,
        last_login_time_end: int = None,
        last_login_time_start: int = None,
        next_token: str = None,
        page_size: int = None,
        remark: str = None,
        use_next_token: bool = None,
        user: str = None,
        uuid: str = None,
    ):
        # Set which page of the returned results to start displaying the query results. The default value is **1**, indicating that the display starts from the first page.
        self.current_page = current_page
        # Whether the account name supports fuzzy search. To enable fuzzy search, set this parameter\\"s value to **1**; other values or an empty value indicate that fuzzy search is not supported.
        self.extend = extend
        # Whether the queried account has ROOT privileges. Possible values include:
        # 
        # - **0**: No
        # - **1**: Yes
        self.is_root = is_root
        # The end timestamp for the last login retrieval. The unit is milliseconds.
        self.last_login_time_end = last_login_time_end
        # The start timestamp for the last login retrieval. The unit is milliseconds.
        self.last_login_time_start = last_login_time_start
        # Used to mark the starting position for reading. Leave it empty to start from the beginning.
        # 
        # > For the first call, you do not need to fill in this field. The response will include the NextToken for the second call, and each subsequent call will include the NextToken for the next call.
        self.next_token = next_token
        # Set the number of account asset fingerprint information items to display per page during pagination. The default value is **10**, indicating that 10 items of account asset fingerprint information are displayed per page.
        self.page_size = page_size
        # The name or IP address of the server to be queried.
        self.remark = remark
        # Whether to use the NextToken method to fetch vulnerability list data. If this parameter is used, TotalCount will no longer be returned. Possible values:
        # 
        # - **true**: Use the NextToken method.
        # - **false**: Do not use the NextToken method.
        self.use_next_token = use_next_token
        # The account name of the server to be queried.
        self.user = user
        # The UUID of the server to be queried.
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

        if self.is_root is not None:
            result['IsRoot'] = self.is_root

        if self.last_login_time_end is not None:
            result['LastLoginTimeEnd'] = self.last_login_time_end

        if self.last_login_time_start is not None:
            result['LastLoginTimeStart'] = self.last_login_time_start

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

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

        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')

        if m.get('LastLoginTimeEnd') is not None:
            self.last_login_time_end = m.get('LastLoginTimeEnd')

        if m.get('LastLoginTimeStart') is not None:
            self.last_login_time_start = m.get('LastLoginTimeStart')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

