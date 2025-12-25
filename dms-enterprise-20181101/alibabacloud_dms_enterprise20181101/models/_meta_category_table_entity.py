# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetaCategoryTableEntity(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        category_id: int = None,
        database_search_name: str = None,
        db_id: int = None,
        db_type: str = None,
        description: str = None,
        instance_id: int = None,
        schema_name: str = None,
        table_name: str = None,
        table_schema_name: str = None,
    ):
        self.catalog_name = catalog_name
        self.category_id = category_id
        self.database_search_name = database_search_name
        self.db_id = db_id
        self.db_type = db_type
        self.description = description
        self.instance_id = instance_id
        self.schema_name = schema_name
        self.table_name = table_name
        self.table_schema_name = table_schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.database_search_name is not None:
            result['DatabaseSearchName'] = self.database_search_name

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('DatabaseSearchName') is not None:
            self.database_search_name = m.get('DatabaseSearchName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')

        return self

