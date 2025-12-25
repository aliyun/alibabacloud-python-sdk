# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSensitiveColumnsDetailRequest(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        logic: bool = None,
        schema_name: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        # The name of the field. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to obtain the name of the field.
        # 
        # >  You can also call the [ListColumns](https://help.aliyun.com/document_detail/141870.html) operation to obtain the name of the field.
        # 
        # This parameter is required.
        self.column_name = column_name
        # The ID of the database. The database can be a physical database or a logical database.
        # 
        # *   To obtain the ID of a physical database, call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        # *   To obtain the ID of a logical database, call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        self.db_id = db_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is a physical database.
        self.logic = logic
        # The name of the database. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to obtain the name of the database.
        # 
        # > * You can also call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the name of a physical database.
        # > * You can also call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the name of a logical database.
        # 
        # This parameter is required.
        self.schema_name = schema_name
        # The name of the table. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to obtain the name of the table.
        # 
        # >  You can also call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to obtain the name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

