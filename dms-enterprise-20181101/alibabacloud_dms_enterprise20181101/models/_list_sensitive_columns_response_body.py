# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSensitiveColumnsResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sensitive_column_list: main_models.ListSensitiveColumnsResponseBodySensitiveColumnList = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The sensitive fields.
        self.sensitive_column_list = sensitive_column_list
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.sensitive_column_list:
            self.sensitive_column_list.validate()

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

        if self.sensitive_column_list is not None:
            result['SensitiveColumnList'] = self.sensitive_column_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SensitiveColumnList') is not None:
            temp_model = main_models.ListSensitiveColumnsResponseBodySensitiveColumnList()
            self.sensitive_column_list = temp_model.from_map(m.get('SensitiveColumnList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSensitiveColumnsResponseBodySensitiveColumnList(DaraModel):
    def __init__(
        self,
        sensitive_column: List[main_models.ListSensitiveColumnsResponseBodySensitiveColumnListSensitiveColumn] = None,
    ):
        self.sensitive_column = sensitive_column

    def validate(self):
        if self.sensitive_column:
            for v1 in self.sensitive_column:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SensitiveColumn'] = []
        if self.sensitive_column is not None:
            for k1 in self.sensitive_column:
                result['SensitiveColumn'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_column = []
        if m.get('SensitiveColumn') is not None:
            for k1 in m.get('SensitiveColumn'):
                temp_model = main_models.ListSensitiveColumnsResponseBodySensitiveColumnListSensitiveColumn()
                self.sensitive_column.append(temp_model.from_map(k1))

        return self

class ListSensitiveColumnsResponseBodySensitiveColumnListSensitiveColumn(DaraModel):
    def __init__(
        self,
        column_count: int = None,
        column_name: str = None,
        function_type: str = None,
        schema_name: str = None,
        security_level: str = None,
        table_name: str = None,
    ):
        # The number of sensitive fields.
        self.column_count = column_count
        # The name of the field.
        self.column_name = column_name
        # The type of the de-identification algorithm. Valid values:
        # 
        # *   DEFAULT: All characters are masked. This is the default value.
        # *   FIX_POS: The characters at specific positions are masked.
        # *   FIX_CHAR: Specific characters are masked.
        self.function_type = function_type
        # The name of the database.
        self.schema_name = schema_name
        # The sensitivity level of the field. Valid values:
        # 
        # *   SENSITIVE
        # *   CONFIDENTIAL
        self.security_level = security_level
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_count is not None:
            result['ColumnCount'] = self.column_count

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

