# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class UpdateTableAddColumnRequest(DaraModel):
    def __init__(
        self,
        column: List[main_models.UpdateTableAddColumnRequestColumn] = None,
        table_guid: str = None,
    ):
        # The fields.
        # 
        # This parameter is required.
        self.column = column
        # The globally unique identifier (GUID) of the MaxCompute table. Specify the GUID in the odps.projectName.tableName format.
        # 
        # This parameter is required.
        self.table_guid = table_guid

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

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k1 in m.get('Column'):
                temp_model = main_models.UpdateTableAddColumnRequestColumn()
                self.column.append(temp_model.from_map(k1))

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

class UpdateTableAddColumnRequestColumn(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_name_cn: str = None,
        column_type: str = None,
        comment: str = None,
    ):
        # The name of the field.
        # 
        # This parameter is required.
        self.column_name = column_name
        # The display name of the field.
        self.column_name_cn = column_name_cn
        # The type of the field. For more information, see MaxCompute field types.
        # 
        # This parameter is required.
        self.column_type = column_type
        # The comment of the field.
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_name_cn is not None:
            result['ColumnNameCn'] = self.column_name_cn

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.comment is not None:
            result['Comment'] = self.comment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnNameCn') is not None:
            self.column_name_cn = m.get('ColumnNameCn')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        return self

