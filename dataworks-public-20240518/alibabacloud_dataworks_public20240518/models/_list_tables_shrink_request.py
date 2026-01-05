# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTablesShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_meta_entity_id: str = None,
        sort_by: str = None,
        table_types_shrink: str = None,
    ):
        # The comment. Supports fuzzy matching.
        self.comment = comment
        # The name. Supports fuzzy matching.
        self.name = name
        # The order in which the tables are sorted. Default value: Asc. Valid values:
        # 
        # *   Asc
        # *   Desc
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The parent metadata entity ID. You can refer to the responses of the ListDatabases or ListSchemas operation and [Description of concepts related to metadata entities.](https://help.aliyun.com/document_detail/2880092.html)
        # 
        # *   The parent metadata entity is a database: The format of `ParentMetaEntityId` is `${EntityType}:${Instance ID or encoded URL}:${Catalog Identifier}:${Database Name}`. Use an empty string (\\`""\\`) as a placeholder for any non-existent level.
        # *   The parent metadata entity is a database schema: The format of `ParentMetaEntityId` is `${EntityType}:${Instance ID or encoded URL}:${Catalog Identifier}:${Database Name}:${Schema Name}`. Use an empty string (\\`""\\`) as a placeholder for any non-existent level.
        # 
        # > 
        # 
        # *   The schema level in `ParentMetaEntityId` is supported only for database services, such as `MaxCompute (with schema enabled), Hologres, PostgreSQL, SQL Server, HybridDB for PostgreSQL, and Oracle`.
        # 
        # *   For the MaxCompute and DLF types, use an empty string as the placeholder for the instance ID. For MaxCompute, the database name is the same as the project name.
        # 
        # *   For StarRocks, the catalog identifier is the catalog name. For DLF, it is the catalog ID. Other types do not support the catalog level and you can use an empty string as a placeholder.
        # 
        # Examples of common ParentMetaEntityId formats
        # 
        # *   `maxcompute-project:::project_name`
        # *   `maxcompute-schema:::project_name:schema_name` (for MaxCompute projects with schema enabled)
        # *   `dlf-database::catalog_id:database_name`
        # *   `hms-database:instance_id::database_name`
        # *   `holo-schema:instance_id::database_name:schema_name`
        # *   `mysql-database:(instance_id|encoded_jdbc_url)::database_name`
        # 
        # > 
        # 
        # *   `instance_id`: The instance ID, which is required when the data source is registered in instance mode.
        # 
        # *   `encoded_jdbc_url`: The URLEncoded JDBC connection string, which is requiredwhen the data source is registered using a connection string.
        # 
        # *   `catalog_id`: The DLF catalog ID.
        # 
        # *   `project_name`: The MaxCompute project name.
        # 
        # *   `database_name`: The database name.
        # 
        # *   `schema_name`: The schema name.
        # 
        # This parameter is required.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The sort field. Default value: CreateTime. Valid values:
        # 
        # *   CreateTime
        # *   ModifyTime
        # *   Name
        # *   TableType
        self.sort_by = sort_by
        # The list of table types to query. If it\\"s left empty, all types will be queried.
        self.table_types_shrink = table_types_shrink

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

        if self.table_types_shrink is not None:
            result['TableTypes'] = self.table_types_shrink

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
            self.table_types_shrink = m.get('TableTypes')

        return self

