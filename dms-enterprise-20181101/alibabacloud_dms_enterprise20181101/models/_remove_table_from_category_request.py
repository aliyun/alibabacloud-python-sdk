# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveTableFromCategoryRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        db_id: int = None,
        table_name: str = None,
        table_schema_name: str = None,
        tid: int = None,
    ):
        # The category ID.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The database ID. You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the ID of a physical database and the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the ID of a logical database.
        # 
        # >  The value of DatabaseId is that of DbId.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The table name.
        # 
        # > You can also call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the table name.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The schema name of the table, which is required only for SQL Server instances.
        self.table_schema_name = table_schema_name
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

