# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckBatchTableAccessPermissionShrinkRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        permission_type: str = None,
        table_name_list_shrink: str = None,
        tid: int = None,
    ):
        # The database ID. You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the ID of a physical database and the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the ID of a logical database.
        # 
        # >  The value of DatabaseId is that of DbId.
        # 
        # This parameter is required.
        self.db_id = db_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   true: Logical database.
        # *   false: Physical database.
        self.logic = logic
        # The type of the permission to be verified.
        # 
        # Valid values:
        # 
        # *   QUERY
        # *   EXPORT
        # *   CORRECT
        # *   LOGIN
        # *   PERF
        # 
        # This parameter is required.
        self.permission_type = permission_type
        # The name of the table.
        # 
        # This parameter is required.
        self.table_name_list_shrink = table_name_list_shrink
        # The ID of the tenant.
        # 
        # >  View Tenant ID by hovering over your profile icon in the DMS console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

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

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        if self.table_name_list_shrink is not None:
            result['TableNameList'] = self.table_name_list_shrink

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        if m.get('TableNameList') is not None:
            self.table_name_list_shrink = m.get('TableNameList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

