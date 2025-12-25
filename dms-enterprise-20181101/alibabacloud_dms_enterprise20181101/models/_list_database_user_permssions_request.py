# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatabaseUserPermssionsRequest(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        logic: bool = None,
        page_number: int = None,
        page_size: int = None,
        perm_type: str = None,
        tid: int = None,
        user_name: str = None,
    ):
        # The ID of the database.
        # 
        # This parameter is required.
        self.db_id = db_id
        # Specifies whether the database is a logical database.
        self.logic = logic
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The type of the permission. Valid values:
        # 
        # *   DATABASE: permissions on databases
        # *   TABLE: permissions on tables
        # *   COLUMN: permissions on fields
        # 
        # This parameter is required.
        self.perm_type = perm_type
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, log on to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid
        # The nickname of the user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.perm_type is not None:
            result['PermType'] = self.perm_type

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

