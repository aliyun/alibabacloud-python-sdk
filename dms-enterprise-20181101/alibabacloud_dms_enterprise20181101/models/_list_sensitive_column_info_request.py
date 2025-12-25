# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSensitiveColumnInfoRequest(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        instance_id: int = None,
        page_number: int = None,
        page_size: int = None,
        schema_name: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        # The name of the sensitive field. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to query the name of the sensitive field.
        # 
        # > You can also call the [ListColumns](https://help.aliyun.com/document_detail/141870.html) operation to query the name of the sensitive field.
        self.column_name = column_name
        # The ID of the instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The database name. You can also call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to query the name of the database.
        # 
        # > You can also call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the value of the SchemaName parameter of a physical database, or the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the value of the SchemaName parameter of a logical database.
        self.schema_name = schema_name
        # The name of the table. You can call the [ListSensitiveColumns](https://help.aliyun.com/document_detail/188103.html) operation to query the table name.
        # 
        # > You can also call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the table name.
        self.table_name = table_name
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the DMS console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

