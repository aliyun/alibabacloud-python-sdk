# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class AddTableRequest(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        table_columns: List[main_models.AddTableRequestTableColumns] = None,
        table_name: str = None,
    ):
        # This parameter is required.
        self.connector_id = connector_id
        # This parameter is required.
        self.table_columns = table_columns
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        if self.table_columns:
            for v1 in self.table_columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        result['TableColumns'] = []
        if self.table_columns is not None:
            for k1 in self.table_columns:
                result['TableColumns'].append(k1.to_map() if k1 else None)

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        self.table_columns = []
        if m.get('TableColumns') is not None:
            for k1 in m.get('TableColumns'):
                temp_model = main_models.AddTableRequestTableColumns()
                self.table_columns.append(temp_model.from_map(k1))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class AddTableRequestTableColumns(DaraModel):
    def __init__(
        self,
        column_desc: str = None,
        column_name: str = None,
        data_type: str = None,
    ):
        self.column_desc = column_desc
        # This parameter is required.
        self.column_name = column_name
        # This parameter is required.
        self.data_type = data_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_desc is not None:
            result['ColumnDesc'] = self.column_desc

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.data_type is not None:
            result['DataType'] = self.data_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnDesc') is not None:
            self.column_desc = m.get('ColumnDesc')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        return self

