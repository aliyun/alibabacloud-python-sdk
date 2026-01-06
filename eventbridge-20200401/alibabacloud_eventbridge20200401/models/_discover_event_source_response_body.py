# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class DiscoverEventSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DiscoverEventSourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DiscoverEventSourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DiscoverEventSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        source_my_sqldiscovery: main_models.DiscoverEventSourceResponseBodyDataSourceMySQLDiscovery = None,
    ):
        self.source_my_sqldiscovery = source_my_sqldiscovery

    def validate(self):
        if self.source_my_sqldiscovery:
            self.source_my_sqldiscovery.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_my_sqldiscovery is not None:
            result['SourceMySQLDiscovery'] = self.source_my_sqldiscovery.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceMySQLDiscovery') is not None:
            temp_model = main_models.DiscoverEventSourceResponseBodyDataSourceMySQLDiscovery()
            self.source_my_sqldiscovery = temp_model.from_map(m.get('SourceMySQLDiscovery'))

        return self

class DiscoverEventSourceResponseBodyDataSourceMySQLDiscovery(DaraModel):
    def __init__(
        self,
        database_names: List[str] = None,
        estimated_rows: int = None,
        expire_logs_days: int = None,
        simple_data: str = None,
        table_names: List[str] = None,
        table_schema: main_models.DiscoverEventSourceResponseBodyDataSourceMySQLDiscoveryTableSchema = None,
        wait_timeout: int = None,
    ):
        self.database_names = database_names
        self.estimated_rows = estimated_rows
        self.expire_logs_days = expire_logs_days
        self.simple_data = simple_data
        self.table_names = table_names
        self.table_schema = table_schema
        self.wait_timeout = wait_timeout

    def validate(self):
        if self.table_schema:
            self.table_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names

        if self.estimated_rows is not None:
            result['EstimatedRows'] = self.estimated_rows

        if self.expire_logs_days is not None:
            result['ExpireLogsDays'] = self.expire_logs_days

        if self.simple_data is not None:
            result['SimpleData'] = self.simple_data

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema.to_map()

        if self.wait_timeout is not None:
            result['WaitTimeout'] = self.wait_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')

        if m.get('EstimatedRows') is not None:
            self.estimated_rows = m.get('EstimatedRows')

        if m.get('ExpireLogsDays') is not None:
            self.expire_logs_days = m.get('ExpireLogsDays')

        if m.get('SimpleData') is not None:
            self.simple_data = m.get('SimpleData')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        if m.get('TableSchema') is not None:
            temp_model = main_models.DiscoverEventSourceResponseBodyDataSourceMySQLDiscoveryTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        if m.get('WaitTimeout') is not None:
            self.wait_timeout = m.get('WaitTimeout')

        return self

class DiscoverEventSourceResponseBodyDataSourceMySQLDiscoveryTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.DiscoverEventSourceResponseBodyDataSourceMySQLDiscoveryTableSchemaColumns] = None,
        table_name: str = None,
    ):
        self.columns = columns
        self.table_name = table_name

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

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.DiscoverEventSourceResponseBodyDataSourceMySQLDiscoveryTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DiscoverEventSourceResponseBodyDataSourceMySQLDiscoveryTableSchemaColumns(DaraModel):
    def __init__(
        self,
        extra: str = None,
        field: str = None,
        is_null: str = None,
        key: str = None,
        type: str = None,
    ):
        self.extra = extra
        self.field = field
        self.is_null = is_null
        self.key = key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        if self.field is not None:
            result['Field'] = self.field

        if self.is_null is not None:
            result['IsNull'] = self.is_null

        if self.key is not None:
            result['Key'] = self.key

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('IsNull') is not None:
            self.is_null = m.get('IsNull')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

