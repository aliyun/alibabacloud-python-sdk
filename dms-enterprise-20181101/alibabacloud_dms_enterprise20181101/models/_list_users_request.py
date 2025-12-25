# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        role: str = None,
        search_key: str = None,
        tid: int = None,
        user_state: str = None,
    ):
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # **
        # 
        # Valid values: 10, 20, 50, and 100.**** Default value: 10.
        self.page_size = page_size
        # The role that is assigned to the user. Valid values:
        # 
        # *   **USER**: a regular user.
        # *   **DBA** : a database administrator (DBA).
        # *   **ADMIN**: a Data Management (DMS) administrator.
        # *   **SECURITY_ADMIN**: a security administrator.
        # *   **STRUCT_READ_ONLY**: a schema read-only user.
        # 
        # >  To check your role, move the pointer over the profile picture in the upper-right corner of the DMS console.
        self.role = role
        # The search keyword. Fuzzy match is supported.
        self.search_key = search_key
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
        self.tid = tid
        # The status of the user. Valid values:
        # 
        # *   **NORMAL**: The user is normal.
        # *   **DISABLE**: The user is disabled.
        # *   **DELETE**: The user is deleted.
        self.user_state = user_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role is not None:
            result['Role'] = self.role

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_state is not None:
            result['UserState'] = self.user_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')

        return self

