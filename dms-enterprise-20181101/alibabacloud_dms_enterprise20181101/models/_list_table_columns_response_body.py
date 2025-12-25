# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTableColumnsResponseBody(DaraModel):
    def __init__(
        self,
        column_list: main_models.ListTableColumnsResponseBodyColumnList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about fields in the table.
        self.column_list = column_list
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.column_list:
            self.column_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_list is not None:
            result['ColumnList'] = self.column_list.to_map()

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
        if m.get('ColumnList') is not None:
            temp_model = main_models.ListTableColumnsResponseBodyColumnList()
            self.column_list = temp_model.from_map(m.get('ColumnList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTableColumnsResponseBodyColumnList(DaraModel):
    def __init__(
        self,
        column: List[main_models.ListTableColumnsResponseBodyColumnListColumn] = None,
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
                temp_model = main_models.ListTableColumnsResponseBodyColumnListColumn()
                self.column.append(temp_model.from_map(k1))

        return self

class ListTableColumnsResponseBodyColumnListColumn(DaraModel):
    def __init__(
        self,
        auto_increment: bool = None,
        column_id: str = None,
        column_name: str = None,
        column_type: str = None,
        data_length: int = None,
        data_precision: int = None,
        data_scale: int = None,
        default_value: str = None,
        description: str = None,
        function_type: str = None,
        nullable: bool = None,
        security_level: str = None,
        sensitive: bool = None,
    ):
        # Indicates whether the field is an auto-increment field. Valid values:
        # 
        # *   true: The field is an auto-increment field.
        # *   false: The field is not an auto-increment field.
        self.auto_increment = auto_increment
        # The ID of the field.
        self.column_id = column_id
        # The field name.
        self.column_name = column_name
        # The data type of the field.
        self.column_type = column_type
        # The length of the field.
        self.data_length = data_length
        # The number of valid digits for the column.
        self.data_precision = data_precision
        # The number of decimal places of the field data.
        self.data_scale = data_scale
        # The default value of the column.
        self.default_value = default_value
        # The description of the field.
        self.description = description
        # The type of the masking algorithm that is used for the field. Valid values:
        # 
        # *   null: No masking algorithm is used.
        # *   DEFAULT: A full masking algorithm is used.
        # *   FIX_POS: The fixed position is masked.
        # *   FIX_CHAR: The fixed characters are replaced.
        self.function_type = function_type
        # Indicates whether the field can be empty. Valid values:
        # 
        # *   true: The field can be empty.
        # *   false: The field cannot be empty.
        self.nullable = nullable
        # The security level of the field. Valid values:
        # 
        # *   INNER: The field is an internal field but not sensitive.
        # *   SENSITIVE: The field is sensitive.
        # *   CONFIDENTIAL: The field is a confidential column.
        self.security_level = security_level
        # Indicates whether the field is a sensitive column. Valid values:
        # 
        # *   true: The field is a sensitive field.
        # *   false: The field is not a sensitive field.
        self.sensitive = sensitive

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

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive

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

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')

        return self

