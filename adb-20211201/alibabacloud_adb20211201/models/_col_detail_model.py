# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ColDetailModel(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        create_time: str = None,
        description: str = None,
        distribute_key: bool = None,
        nullable: bool = None,
        partition_key: bool = None,
        primary_key: bool = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.column_name = column_name
        self.create_time = create_time
        self.description = description
        self.distribute_key = distribute_key
        self.nullable = nullable
        self.partition_key = partition_key
        self.primary_key = primary_key
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.distribute_key is not None:
            result['DistributeKey'] = self.distribute_key

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DistributeKey') is not None:
            self.distribute_key = m.get('DistributeKey')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('PartitionKey') is not None:
            self.partition_key = m.get('PartitionKey')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

