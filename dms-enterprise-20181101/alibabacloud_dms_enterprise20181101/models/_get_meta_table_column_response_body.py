# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetMetaTableColumnResponseBody(DaraModel):
    def __init__(
        self,
        column_list: List[main_models.GetMetaTableColumnResponseBodyColumnList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about fields in the table.
        self.column_list = column_list
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
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
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.GetMetaTableColumnResponseBodyColumnList()
                self.column_list.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMetaTableColumnResponseBodyColumnList(DaraModel):
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
        position: int = None,
        primary_key: str = None,
        security_level: str = None,
    ):
        # Indicates whether the column is an auto-increment column. Valid values:
        # 
        # *   **true**: The column is an auto-increment column.
        # *   **false**: The column is not an auto-increment column.
        self.auto_increment = auto_increment
        # The ID of the column.
        self.column_id = column_id
        # The name of the column.
        self.column_name = column_name
        # The data type of the column.
        # 
        # > The return value of a column is not unique, such as **bigint** or **int**.
        self.column_type = column_type
        # The length of the field.
        self.data_length = data_length
        # The precision of the field.
        self.data_precision = data_precision
        # The number of decimal places for the field.
        self.data_scale = data_scale
        # The description of the column.
        self.description = description
        # Indicates whether the field can be empty. Valid values:
        # 
        # *   **true**: The field can be empty.
        # *   **false**: The field cannot be empty.
        self.nullable = nullable
        # The position of the field in the table.
        self.position = position
        # Indicates whether the field is the primary key. Valid values:
        # 
        # *   **true**: The field is the primary key.
        # *   **false**: The field is not the primary key.
        self.primary_key = primary_key
        # The sensitivity level of the column. Valid values:
        # 
        # *   **INNER**: The column is not sensitive.
        # *   **SENSITIVE**: The column is sensitive.
        # *   **CONFIDENTIAL**: The column is confidential.
        # 
        # > For more information, see [Sensitivity levels of columns](https://help.aliyun.com/document_detail/66091.html).
        self.security_level = security_level

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

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

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

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        return self

