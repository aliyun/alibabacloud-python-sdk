# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetMetaTableDetailInfoResponseBody(DaraModel):
    def __init__(
        self,
        detail_info: main_models.GetMetaTableDetailInfoResponseBodyDetailInfo = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the table.
        self.detail_info = detail_info
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            temp_model = main_models.GetMetaTableDetailInfoResponseBodyDetailInfo()
            self.detail_info = temp_model.from_map(m.get('DetailInfo'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMetaTableDetailInfoResponseBodyDetailInfo(DaraModel):
    def __init__(
        self,
        column_list: List[main_models.GetMetaTableDetailInfoResponseBodyDetailInfoColumnList] = None,
        index_list: List[main_models.GetMetaTableDetailInfoResponseBodyDetailInfoIndexList] = None,
    ):
        # The columns in the table.
        self.column_list = column_list
        # The list of indexes.
        self.index_list = index_list

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
                 if v1:
                    v1.validate()
        if self.index_list:
            for v1 in self.index_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        result['IndexList'] = []
        if self.index_list is not None:
            for k1 in self.index_list:
                result['IndexList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.GetMetaTableDetailInfoResponseBodyDetailInfoColumnList()
                self.column_list.append(temp_model.from_map(k1))

        self.index_list = []
        if m.get('IndexList') is not None:
            for k1 in m.get('IndexList'):
                temp_model = main_models.GetMetaTableDetailInfoResponseBodyDetailInfoIndexList()
                self.index_list.append(temp_model.from_map(k1))

        return self

class GetMetaTableDetailInfoResponseBodyDetailInfoIndexList(DaraModel):
    def __init__(
        self,
        index_columns: List[str] = None,
        index_id: str = None,
        index_name: str = None,
        index_type: str = None,
        unique: bool = None,
    ):
        # The index column.
        self.index_columns = index_columns
        # The ID of the index.
        self.index_id = index_id
        # The name of the index.
        self.index_name = index_name
        # The type of the index. Examples: Primary, Unique, and Normal.
        self.index_type = index_type
        # Indicates whether the index is unique. Valid values:
        # 
        # *   true: The index is unique.
        # *   false: The index is not unique.
        self.unique = unique

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_columns is not None:
            result['IndexColumns'] = self.index_columns

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.index_name is not None:
            result['IndexName'] = self.index_name

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.unique is not None:
            result['Unique'] = self.unique

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexColumns') is not None:
            self.index_columns = m.get('IndexColumns')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('Unique') is not None:
            self.unique = m.get('Unique')

        return self

class GetMetaTableDetailInfoResponseBodyDetailInfoColumnList(DaraModel):
    def __init__(
        self,
        auto_increment: bool = None,
        column_id: str = None,
        column_name: str = None,
        column_type: str = None,
        data_length: int = None,
        data_precision: int = None,
        data_scale: int = None,
        description: str = None,
        nullable: bool = None,
        position: str = None,
    ):
        # Indicates whether the column is an auto-increment column. Valid values:
        # 
        # *   true: The column is an auto-increment column.
        # *   false: The column is not an auto-increment column.
        self.auto_increment = auto_increment
        # The ID of the column.
        self.column_id = column_id
        # The name of the column.
        self.column_name = column_name
        # The data type of the column. Examples: Bigint, Int, and Varchar.
        self.column_type = column_type
        # The length of the field.
        self.data_length = data_length
        # The precision of the field.
        self.data_precision = data_precision
        # The scale of the column.
        self.data_scale = data_scale
        # The description of the column.
        self.description = description
        # Indicates whether the column is nullable. Valid values:
        # 
        # *   true: The column is nullable.
        # *   false: The column is not nullable.
        self.nullable = nullable
        # The position of the field in the table.
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment

        if self.column_id is not None:
            result['ColumnId'] = self.column_id

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.data_length is not None:
            result['DataLength'] = self.data_length

        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision

        if self.data_scale is not None:
            result['DataScale'] = self.data_scale

        if self.description is not None:
            result['Description'] = self.description

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')

        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')

        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')

        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

