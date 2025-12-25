# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTableToCategoryRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        db_id: int = None,
        table_name: str = None,
        table_schema_name: str = None,
        tid: int = None,
    ):
        # The ID of the associated category.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The ID of a physical database: You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the physical database ID.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The name of the table. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the table name.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The schema name of the table, which is required only for SQL Server instances.
        self.table_schema_name = table_schema_name
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
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

