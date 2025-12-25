# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeColumnSecLevelRequest(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        is_logic: bool = None,
        new_level: str = None,
        schema_name: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        # The name of the field. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to obtain the name of the field.
        # 
        # > You can also call the [ListColumns](https://help.aliyun.com/document_detail/141870.html) operation to obtain the name of the field.
        # 
        # This parameter is required.
        self.column_name = column_name
        # The ID of the database. You can call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the ID of the database.
        # 
        # > You can also call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to obtain the ID of a physical database and the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to obtain the ID of a logical database.
        # 
        # This parameter is required.
        self.db_id = db_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   true: The database is a physical database.
        # *   false: The database is a logical database.
        # 
        # This parameter is required.
        self.is_logic = is_logic
        # The new sensitivity level of the field that you want to specify. Valid values:
        # 
        # *   INNER: low sensitivity level
        # *   SENSITIVE: medium sensitivity level
        # *   CONFIDENTIAL: high sensitivity level
        # 
        # This parameter is required.
        self.new_level = new_level
        # The name of the database. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to obtain the name of the database.
        # 
        # *   You can also call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the name of the database.
        # *   You can also call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to obtain the name of a physical database and the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to obtain the name of a logical database.
        # 
        # This parameter is required.
        self.schema_name = schema_name
        # The name of the table. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to obtain the name of the table.
        # 
        # > You can also call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to obtain the name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
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

        if self.is_logic is not None:
            result['IsLogic'] = self.is_logic

        if self.new_level is not None:
            result['NewLevel'] = self.new_level

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

        if m.get('IsLogic') is not None:
            self.is_logic = m.get('IsLogic')

        if m.get('NewLevel') is not None:
            self.new_level = m.get('NewLevel')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

