# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeColumnSecurityLevelRequest(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        is_logic: bool = None,
        new_sensitivity_level: str = None,
        schema_name: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        # The name of the field. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) or [ListColumns](https://help.aliyun.com/document_detail/141870.html) operation to query the column name.
        # 
        # This parameter is required.
        self.column_name = column_name
        # The database ID. The database can be a physical database or a logical database.
        # 
        # *   The ID of a physical database: You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the physical database ID.
        # *   To obtain the ID of a logical database, call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        # 
        # This parameter is required.
        self.db_id = db_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database
        # *   **false**: The database is a physical database.
        # 
        # This parameter is required.
        self.is_logic = is_logic
        # The new security level of the column. The valid values are the same as the sensitivity levels of the classification template that is associated with the instance. You can call the [ListSensitivityLevel](https://help.aliyun.com/document_detail/2539519.html) operation to obtain the sensitivity levels of the classification template.
        # 
        # This parameter is required.
        self.new_sensitivity_level = new_sensitivity_level
        # The database name. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to query the database name.
        # 
        # > You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the name of a physical database and call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the name of a logical database.
        # 
        # This parameter is required.
        self.schema_name = schema_name
        # The name of the table. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) or [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the table name.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the tenant.
        # 
        # > To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
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

        if self.new_sensitivity_level is not None:
            result['NewSensitivityLevel'] = self.new_sensitivity_level

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

        if m.get('NewSensitivityLevel') is not None:
            self.new_sensitivity_level = m.get('NewSensitivityLevel')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

