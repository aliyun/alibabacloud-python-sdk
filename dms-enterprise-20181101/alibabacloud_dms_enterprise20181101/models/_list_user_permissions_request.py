# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserPermissionsRequest(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        page_number: int = None,
        page_size: int = None,
        perm_type: str = None,
        search_key: str = None,
        tid: int = None,
        user_id: str = None,
    ):
        # The name of the database.
        self.database_name = database_name
        # The type of the database. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The type of the environment to which the database belongs. Valid values:
        # 
        # *   product: production environment
        # *   dev: development environment
        # *   pre: staging environment
        # *   test: test environment
        # *   sit: SIT environment
        # *   uat: user acceptance testing (UAT) environment
        # *   pet: stress testing environment
        # *   stag: STAG environment
        self.env_type = env_type
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   true: The database is a logical database.
        # *   false: The database is a physical database.
        self.logic = logic
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The permissions on a specific type of resources that you want to query. Valid values:
        # 
        # *   DATABASE: permissions on databases
        # *   TABLE: permissions on tables
        # *   COLUMN: permissions on fields
        # *   INSTANCE: permissions on instances
        # 
        # This parameter is required.
        self.perm_type = perm_type
        # The keyword used in the query. For example, if you want to query permissions on an instance, you can specify the endpoint of the instance, such as rm-bp144d5ky4l4r****.
        self.search_key = search_key
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid
        # The ID of the user. You can call the [GetUser](https://help.aliyun.com/document_detail/147098.html) or [ListUsers](https://help.aliyun.com/document_detail/141938.html) operation to query the ID of the user.
        # 
        # >  The user ID is different from the ID of your Alibaba Cloud account.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.perm_type is not None:
            result['PermType'] = self.perm_type

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

