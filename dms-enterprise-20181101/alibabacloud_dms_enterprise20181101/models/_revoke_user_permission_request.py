# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeUserPermissionRequest(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        ds_type: str = None,
        instance_id: int = None,
        logic: bool = None,
        perm_types: str = None,
        table_id: str = None,
        table_name: str = None,
        tid: int = None,
        user_access_id: str = None,
        user_id: str = None,
    ):
        # The database ID. The database can be a physical database or a logical database.
        # 
        # *   To query the ID of a physical database, call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        # *   To query the ID of a logical database, call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        self.db_id = db_id
        # The type of the object on which you want to revoke permissions from a user. Valid values:
        # 
        # *   **INSTANCE**: instances.
        # *   **DATABASE**: physical databases.
        # *   **LOGIC_DATABASE**: logical databases.
        # *   **TABLE**: physical tables.
        # *   **LOGIC_TABLE**: logical tables.
        # 
        # This parameter is required.
        self.ds_type = ds_type
        # The database instance ID. You must specify this parameter if you revoke a permission from the database instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the ID of the database instance.
        self.instance_id = instance_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is a physical database.
        # 
        # > 
        # 
        # *   If the database is a logical database, set this parameter to **true**.
        # 
        # *   If the database is a physical database, set this parameter to **false**.
        self.logic = logic
        # The type of the permissions. Valid values:
        # 
        # *   **QUERY**: query permissions.
        # *   **EXPORT**: export permissions.
        # *   **CORRECT**: change permissions.
        # *   **LOGIN**: logon permissions.
        # *   **PERF**: query permissions on the performance details of an instance.
        # 
        # This parameter is required.
        self.perm_types = perm_types
        # The table ID. You must specify this parameter if you revoke a permission from the table. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the table ID.
        self.table_id = table_id
        # The name of the table. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the table name.
        self.table_name = table_name
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid
        # The permission ID. You can call the [ListUserPermission](https://help.aliyun.com/document_detail/146957.html) operation to query the permission ID.
        # 
        # This parameter is required.
        self.user_access_id = user_access_id
        # The user ID. You can call the [ListUsers](https://help.aliyun.com/document_detail/141938.html) or [GetUser](https://help.aliyun.com/document_detail/147098.html) operation to query the ID of the user.
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

        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

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

        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

