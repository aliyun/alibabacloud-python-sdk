# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeColumnsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeColumnsResponseBodyItems = None,
        request_id: str = None,
    ):
        # The queried columns.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeColumnsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeColumnsResponseBodyItems(DaraModel):
    def __init__(
        self,
        column: List[main_models.DescribeColumnsResponseBodyItemsColumn] = None,
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
                temp_model = main_models.DescribeColumnsResponseBodyItemsColumn()
                self.column.append(temp_model.from_map(k1))

        return self

class DescribeColumnsResponseBodyItemsColumn(DaraModel):
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
        # The name of the column.
        self.column_name = column_name
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        self.dbcluster_id = dbcluster_id
        # Indicates whether the column is the primary key of the table. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.primary_key = primary_key
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The data type of the column.
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

