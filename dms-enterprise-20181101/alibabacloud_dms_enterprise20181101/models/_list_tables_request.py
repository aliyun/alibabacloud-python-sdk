# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTablesRequest(DaraModel):
    def __init__(
        self,
        database_id: str = None,
        page_number: int = None,
        page_size: int = None,
        real_login_user_uid: str = None,
        return_guid: bool = None,
        search_name: str = None,
        tid: int = None,
    ):
        # The ID of the physical database. You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the ID of the physical database.
        # 
        # This parameter is required.
        self.database_id = database_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        self.real_login_user_uid = real_login_user_uid
        # Specifies whether to return the GUID of a table. Valid values:
        # 
        # *   **true**: returns the GUID of a table.
        # *   **false**: does not return the GUID of a table.
        self.return_guid = return_guid
        # The name used to search for tables. Fuzzy search is supported.
        self.search_name = search_name
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

