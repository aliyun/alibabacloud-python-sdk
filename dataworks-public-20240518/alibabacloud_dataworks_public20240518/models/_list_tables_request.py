# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTablesRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        include_extended_properties: bool = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_meta_entity_id: str = None,
        sort_by: str = None,
        table_types: List[str] = None,
    ):
        # The comment. Fuzzy match is supported.
        self.comment = comment
        # Specifies whether to return extended properties. If this parameter is set to `true`, extended properties are returned. If this parameter is set to `false`, extended properties are not returned.
        self.include_extended_properties = include_extended_properties
        # The name. Fuzzy match is supported.
        self.name = name
        # The sort order. Default value: Asc. Valid values:
        # - Asc: ascending order
        # - Desc: descending order
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the parent metadata entity. You can refer to the response of the ListDatabases or ListSchemas operation, or see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # - The parent entity can be the database to which the table belongs. The `ParentMetaEntityId` format is `${EntityType}:${Instance ID or URL-encoded JDBC URL}:${Data catalog identifier}:${Database name}`. Use an empty string as a placeholder for non-existent levels.
        # 
        # - The parent entity can also be the database schema to which the table belongs. The `ParentMetaEntityId` format is `${EntityType}:${Instance ID or URL-encoded JDBC URL}:${Data catalog identifier}:${Database name}:${Schema name}`. Use an empty string as a placeholder for non-existent levels.
        # 
        # > - The database schema can be used for `ParentMetaEntityId` only when the database type supports schemas (`maxcompute`, `holo`, `postgresql`, `sqlserver`, `hybriddb_for_postgresql`, or `oracle`). For MaxCompute, the three-level model must be enabled. Otherwise, only the database can be used.
        # > - For MaxCompute and DLF types, use an empty string as a placeholder for the instance ID. For MaxCompute, the database name is the MaxCompute project name.
        # > - For StarRocks, the data catalog identifier is the catalog name. For DLF, the data catalog identifier is the catalog ID. Other types do not support the catalog level, so use an empty string as a placeholder.
        # 
        # Examples of `ParentMetaEntityId` formats for common types:
        # 
        # - `maxcompute-project:::project_name`
        # 
        # - `maxcompute-schema:::project_name:schema_name` (only when the three-level model is enabled for the project)
        # 
        # - `dlf-database::catalog_id:database_name`
        # 
        # - `hms-database:instance_id::database_name`
        # 
        # - `holo-schema:instance_id::database_name:schema_name`
        # 
        # - `mysql-database:(instance_id|encoded_jdbc_url)::database_name`
        # 
        # > Where:  
        # > - `instance_id`: the instance ID, which is required when the data source is registered in instance mode.
        # > - `encoded_jdbc_url`: the URL-encoded JDBC connection string, which is required when the data source is registered by using a connection string.
        # > - `catalog_id`: the DLF catalog ID.
        # > - `project_name`: the MaxCompute project name.
        # > - `database_name`: the database name.
        # > - `schema_name`: the schema name.
        # 
        # This parameter is required.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The field used for sorting. Default value: CreateTime. Valid values:
        # - CreateTime: creation time
        # - ModifyTime: modification time
        # - Name: name
        # - TableType: table type
        self.sort_by = sort_by
        # The list of table types to query. If this parameter is left empty, all table types are queried.
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

        if self.include_extended_properties is not None:
            result['IncludeExtendedProperties'] = self.include_extended_properties

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

        if m.get('IncludeExtendedProperties') is not None:
            self.include_extended_properties = m.get('IncludeExtendedProperties')

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

