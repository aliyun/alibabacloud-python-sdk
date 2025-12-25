# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSensitiveColumnsRequest(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        logic: bool = None,
        page_number: int = None,
        page_size: int = None,
        schema_name: str = None,
        security_level: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        # The name of the field. You can call the [ListColumns](https://help.aliyun.com/document_detail/141870.html) operation to query the name of the field.
        self.column_name = column_name
        # The ID of the database. You can call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to query the ID of the database.
        # 
        # >  You can also call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the ID of the physical database and the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the ID of a logical database.
        self.db_id = db_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   true: The database is a logical database.
        # *   false: The database is a physical database.
        self.logic = logic
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the database. You can call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to query the name of the database.
        # 
        # >  You can also call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the name of a physical database and the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the name of a logical database.
        self.schema_name = schema_name
        # The sensitivity level of the field. Valid values:
        # 
        # *   SENSITIVE: medium sensitivity level
        # *   CONFIDENTIAL: high sensitivity level
        self.security_level = security_level
        # The name of the table. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the ID of the table.
        self.table_name = table_name
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

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

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

