# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CstoreIndexModel(DaraModel):
    def __init__(
        self,
        column_ords: List[str] = None,
        create_time: str = None,
        database_name: str = None,
        index_columns: List[main_models.FieldSchemaModel] = None,
        index_name: str = None,
        index_type: str = None,
        options: Dict[str, str] = None,
        physical_table_name: str = None,
        update_time: str = None,
    ):
        self.column_ords = column_ords
        self.create_time = create_time
        self.database_name = database_name
        self.index_columns = index_columns
        self.index_name = index_name
        self.index_type = index_type
        self.options = options
        self.physical_table_name = physical_table_name
        self.update_time = update_time

    def validate(self):
        if self.index_columns:
            for v1 in self.index_columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_ords is not None:
            result['ColumnOrds'] = self.column_ords

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        result['IndexColumns'] = []
        if self.index_columns is not None:
            for k1 in self.index_columns:
                result['IndexColumns'].append(k1.to_map() if k1 else None)

        if self.index_name is not None:
            result['IndexName'] = self.index_name

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.options is not None:
            result['Options'] = self.options

        if self.physical_table_name is not None:
            result['PhysicalTableName'] = self.physical_table_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnOrds') is not None:
            self.column_ords = m.get('ColumnOrds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        self.index_columns = []
        if m.get('IndexColumns') is not None:
            for k1 in m.get('IndexColumns'):
                temp_model = main_models.FieldSchemaModel()
                self.index_columns.append(temp_model.from_map(k1))

        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('PhysicalTableName') is not None:
            self.physical_table_name = m.get('PhysicalTableName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

