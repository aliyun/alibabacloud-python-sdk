# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAdbMySqlColumnsResponseBody(DaraModel):
    def __init__(
        self,
        column_count: int = None,
        columns: List[main_models.DescribeAdbMySqlColumnsResponseBodyColumns] = None,
        message: str = None,
        request_id: str = None,
        schema: str = None,
        success: bool = None,
        table_name: str = None,
    ):
        # The total number of columns.
        self.column_count = column_count
        # Details of the columns.
        self.columns = columns
        # The message returned for the operation. Valid values:
        # 
        # *   **Success** is returned if the operation is successful.
        # *   An error message is returned if the operation fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The name of the database.
        self.schema = schema
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   **true**: The operation is successful.
        # *   **false**: The operation fails.
        self.success = success
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
        if self.column_count is not None:
            result['ColumnCount'] = self.column_count

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.success is not None:
            result['Success'] = self.success

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.DescribeAdbMySqlColumnsResponseBodyColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeAdbMySqlColumnsResponseBodyColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # The comments of the column.
        self.comment = comment
        # The name of the column.
        self.name = name
        # The data type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

