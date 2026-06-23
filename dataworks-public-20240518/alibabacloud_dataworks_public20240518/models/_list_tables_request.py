# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTablesRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_meta_entity_id: str = None,
        sort_by: str = None,
        table_types: List[str] = None,
    ):
        # The comment on the table. Fuzzy matching is supported.
        self.comment = comment
        # The name of the table. Fuzzy matching is supported.
        self.name = name
        # The sort order. Default value: `Asc`. Valid values:
        # 
        # - `Asc`: ascending
        # 
        # - `Desc`: descending
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The page size. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the parent metadata entity. You can obtain this ID from the response of the ListDatabases or ListSchemas operation. For details, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # - The value can be the database to which the table belongs. The format is `${EntityType}:${instance ID or URL-encoded connection string}:${data catalog identifier}:${database name}`. Use an empty string as a placeholder for a hierarchy level that does not exist.
        # 
        # - The value can also be the schema to which the table belongs. The format is `${EntityType}:${instance ID or URL-encoded connection string}:${data catalog identifier}:${database name}:${schema name}`. Use an empty string as a placeholder for a hierarchy level that does not exist.
        # 
        # > * You can specify a schema in `ParentMetaEntityId` only if the database type supports schemas, such as `maxcompute/holo/postgresql/sqlserver/hybriddb_for_postgresql/oracle`. For the maxcompute type, the three-layer model must be enabled. Otherwise, you can only specify a database.
        # >
        # > * For `maxcompute` and `dlf` data types, use an empty string as a placeholder for the instance ID. For the maxcompute data type, the database name is the MaxCompute project name.
        # >
        # > * For the `starrocks` type, the data catalog identifier is the catalog name. For the `dlf` type, the data catalog identifier is the catalog ID. Other types do not support the catalog level, so you can use an empty string as a placeholder.
        # 
        # The following list shows the `ParentMetaEntityId` format for several common data source types:
        # 
        # - `maxcompute-project:::project_name`
        # 
        # - `maxcompute-schema:::project_name:schema_name` (Only when the three-layer model is enabled for the project)
        # 
        # - `dlf-database::catalog_id:database_name`
        # 
        # - `hms-database:instance_id::database_name`
        # 
        # - `holo-schema:instance_id::database_name:schema_name`
        # 
        # - `mysql-database:(instance_id|encoded_jdbc_url)::database_name`
        # 
        # > In these formats:
        # >
        # > - `instance_id`: The instance ID. This parameter is required if the data source is registered in instance mode.
        # >
        # > - `encoded_jdbc_url`: The URL-encoded JDBC connection string. This parameter is required if the data source is registered by using a connection string.
        # >
        # > - `catalog_id`: The ID of the DLF data catalog.
        # >
        # > - `project_name`: The name of the MaxCompute project.
        # >
        # > - `database_name`: The name of the database.
        # >
        # > - `schema_name`: The name of the schema.
        # 
        # This parameter is required.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The sort field. Default value: `CreateTime`. Valid values:
        # 
        # - `CreateTime`: creation time
        # 
        # - `ModifyTime`: modification time
        # 
        # - `Name`: name
        # 
        # - `TableType`: table type
        self.sort_by = sort_by
        # A list of table types to query. If you omit this parameter, tables of all types are returned.
        self.table_types = table_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_meta_entity_id is not None:
            result['ParentMetaEntityId'] = self.parent_meta_entity_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.table_types is not None:
            result['TableTypes'] = self.table_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentMetaEntityId') is not None:
            self.parent_meta_entity_id = m.get('ParentMetaEntityId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TableTypes') is not None:
            self.table_types = m.get('TableTypes')

        return self

