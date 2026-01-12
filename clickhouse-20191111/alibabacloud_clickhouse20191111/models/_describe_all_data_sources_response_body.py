# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeAllDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        columns: main_models.DescribeAllDataSourcesResponseBodyColumns = None,
        request_id: str = None,
        schemas: main_models.DescribeAllDataSourcesResponseBodySchemas = None,
        tables: main_models.DescribeAllDataSourcesResponseBodyTables = None,
    ):
        # Details of the columns.
        self.columns = columns
        # The request ID.
        self.request_id = request_id
        # The information about the databases.
        self.schemas = schemas
        # The information about the tables.
        self.tables = tables

    def validate(self):
        if self.columns:
            self.columns.validate()
        if self.schemas:
            self.schemas.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['Columns'] = self.columns.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schemas is not None:
            result['Schemas'] = self.schemas.to_map()

        if self.tables is not None:
            result['Tables'] = self.tables.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            temp_model = main_models.DescribeAllDataSourcesResponseBodyColumns()
            self.columns = temp_model.from_map(m.get('Columns'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schemas') is not None:
            temp_model = main_models.DescribeAllDataSourcesResponseBodySchemas()
            self.schemas = temp_model.from_map(m.get('Schemas'))

        if m.get('Tables') is not None:
            temp_model = main_models.DescribeAllDataSourcesResponseBodyTables()
            self.tables = temp_model.from_map(m.get('Tables'))

        return self

class DescribeAllDataSourcesResponseBodyTables(DaraModel):
    def __init__(
        self,
        table: List[main_models.DescribeAllDataSourcesResponseBodyTablesTable] = None,
    ):
        self.table = table

    def validate(self):
        if self.table:
            for v1 in self.table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Table'] = []
        if self.table is not None:
            for k1 in self.table:
                result['Table'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k1 in m.get('Table'):
                temp_model = main_models.DescribeAllDataSourcesResponseBodyTablesTable()
                self.table.append(temp_model.from_map(k1))

        return self

class DescribeAllDataSourcesResponseBodyTablesTable(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The database name.
        self.schema_name = schema_name
        # The table name.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeAllDataSourcesResponseBodySchemas(DaraModel):
    def __init__(
        self,
        schema: List[main_models.DescribeAllDataSourcesResponseBodySchemasSchema] = None,
    ):
        self.schema = schema

    def validate(self):
        if self.schema:
            for v1 in self.schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Schema'] = []
        if self.schema is not None:
            for k1 in self.schema:
                result['Schema'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k1 in m.get('Schema'):
                temp_model = main_models.DescribeAllDataSourcesResponseBodySchemasSchema()
                self.schema.append(temp_model.from_map(k1))

        return self

class DescribeAllDataSourcesResponseBodySchemasSchema(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The database name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        return self

class DescribeAllDataSourcesResponseBodyColumns(DaraModel):
    def __init__(
        self,
        column: List[main_models.DescribeAllDataSourcesResponseBodyColumnsColumn] = None,
    ):
        self.column = column

    def validate(self):
        if self.column:
            for v1 in self.column:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Column'] = []
        if self.column is not None:
            for k1 in self.column:
                result['Column'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k1 in m.get('Column'):
                temp_model = main_models.DescribeAllDataSourcesResponseBodyColumnsColumn()
                self.column.append(temp_model.from_map(k1))

        return self

class DescribeAllDataSourcesResponseBodyColumnsColumn(DaraModel):
    def __init__(
        self,
        auto_increment_column: bool = None,
        column_name: str = None,
        dbcluster_id: str = None,
        primary_key: bool = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        # Indicates whether the column is an auto-increment column. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_increment_column = auto_increment_column
        # The column name.
        self.column_name = column_name
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # Indicates whether the column is the primary key of the table. Valid values:
        # 
        # *   **true**: The column is the primary key of the table.
        # *   **false**: The column is not the primary key of the table.
        self.primary_key = primary_key
        # The database name.
        self.schema_name = schema_name
        # The table name.
        self.table_name = table_name
        # The column type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

