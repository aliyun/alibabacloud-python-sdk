# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataTrackJobTableMetaResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        table_meta_list: List[main_models.GetDataTrackJobTableMetaResponseBodyTableMetaList] = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The metadata of tables.
        self.table_meta_list = table_meta_list

    def validate(self):
        if self.table_meta_list:
            for v1 in self.table_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TableMetaList'] = []
        if self.table_meta_list is not None:
            for k1 in self.table_meta_list:
                result['TableMetaList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.table_meta_list = []
        if m.get('TableMetaList') is not None:
            for k1 in m.get('TableMetaList'):
                temp_model = main_models.GetDataTrackJobTableMetaResponseBodyTableMetaList()
                self.table_meta_list.append(temp_model.from_map(k1))

        return self

class GetDataTrackJobTableMetaResponseBodyTableMetaList(DaraModel):
    def __init__(
        self,
        columns: List[main_models.GetDataTrackJobTableMetaResponseBodyTableMetaListColumns] = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The information about columns.
        self.columns = columns
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
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

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.GetDataTrackJobTableMetaResponseBodyTableMetaListColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetDataTrackJobTableMetaResponseBodyTableMetaListColumns(DaraModel):
    def __init__(
        self,
        charset: str = None,
        column_name: str = None,
        column_position: int = None,
        column_type: str = None,
        fictive: bool = None,
    ):
        # The name of the character set.
        self.charset = charset
        # The name of the column.
        self.column_name = column_name
        # The position of the column.
        self.column_position = column_position
        # The data type of the column. Examples: BIGINT, INT, and VARCHAR.
        self.column_type = column_type
        # Indicates whether the column is a virtual column. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fictive = fictive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charset is not None:
            result['Charset'] = self.charset

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_position is not None:
            result['ColumnPosition'] = self.column_position

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.fictive is not None:
            result['Fictive'] = self.fictive

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnPosition') is not None:
            self.column_position = m.get('ColumnPosition')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Fictive') is not None:
            self.fictive = m.get('Fictive')

        return self

