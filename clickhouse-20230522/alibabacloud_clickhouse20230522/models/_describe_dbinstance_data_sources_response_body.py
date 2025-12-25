# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceDataSourcesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBInstanceDataSourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceDataSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        columns: List[main_models.DescribeDBInstanceDataSourcesResponseBodyDataColumns] = None,
        dbinstance_id: str = None,
        schemas: str = None,
        tables: List[str] = None,
    ):
        # The columns.
        self.columns = columns
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The account.
        self.schemas = schemas
        # The tables.
        self.tables = tables

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.schemas is not None:
            result['Schemas'] = self.schemas

        if self.tables is not None:
            result['Tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.DescribeDBInstanceDataSourcesResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Schemas') is not None:
            self.schemas = m.get('Schemas')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        return self

class DescribeDBInstanceDataSourcesResponseBodyDataColumns(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        comment: str = None,
        dbname: str = None,
        primary_key: str = None,
        table_name: str = None,
        type: str = None,
    ):
        # The column name.
        self.column_name = column_name
        # The description of the database account.
        self.comment = comment
        # The database name.
        self.dbname = dbname
        # Indicates whether the column is the primary key of the table. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.primary_key = primary_key
        # The table name.
        self.table_name = table_name
        # The type of the stored data.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

