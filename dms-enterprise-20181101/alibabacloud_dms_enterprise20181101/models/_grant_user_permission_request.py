# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantUserPermissionRequest(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        ds_type: str = None,
        expire_date: str = None,
        instance_id: int = None,
        logic: bool = None,
        perm_types: str = None,
        table_id: str = None,
        table_name: str = None,
        tid: int = None,
        user_id: str = None,
    ):
        # The ID of the database. You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the ID of a physical database and the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the ID of a logical database.
        # 
        # >  The value of the DatabaseId parameter is that of the DbId parameter.
        self.db_id = db_id
        # The permissions on a specific type of object that you want to grant to the user. Valid values:
        # 
        # *   INSTANCE: permissions on instances
        # *   DATABASE: permissions on physical databases
        # *   LOGIC_DATABASE: permissions on logical databases
        # *   TABLE: permissions on physical tables
        # *   LOGIC_TABLE: permissions on logical tables
        # 
        # This parameter is required.
        self.ds_type = ds_type
        # The time when the permissions expire.
        # 
        # This parameter is required.
        self.expire_date = expire_date
        # The ID of the instance. You must specify this parameter if you grant permissions on an instance to the user. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the ID of the instance.
        self.instance_id = instance_id
        # Specifies whether the database is a logical database. You must specify this parameter if you grant permissions on a database to the user. Valid values:
        # 
        # *   true: The database is a logical database.
        # *   false: The database is a physical database.
        self.logic = logic
        # The permission type. Separate multiple permission types with commas (,). Valid values:
        # 
        # *   **QUERY**: the query permissions
        # *   **EXPORT**: the export permissions
        # *   **CORRECT**: the change permissions
        # *   **LOGIN**: the logon permissions
        # *   **PERF**: the query permissions on the performance details of the instance
        # 
        # This parameter is required.
        self.perm_types = perm_types
        # The ID of the table. You must specify this parameter if you grant permissions on a table to the user. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the table ID.
        self.table_id = table_id
        # The name of the table. You must specify this parameter if you grant permissions on a table to the user.
        self.table_name = table_name
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
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.perm_types is not None:
            result['PermTypes'] = self.perm_types

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('PermTypes') is not None:
            self.perm_types = m.get('PermTypes')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

