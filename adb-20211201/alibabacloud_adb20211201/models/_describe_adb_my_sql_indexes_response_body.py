# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAdbMySqlIndexesResponseBody(DaraModel):
    def __init__(
        self,
        index_count: int = None,
        indexes: List[main_models.DescribeAdbMySqlIndexesResponseBodyIndexes] = None,
        message: str = None,
        request_id: str = None,
        schema: str = None,
        success: bool = None,
        table_name: str = None,
    ):
        # The filter condition for the number of indexes (the number of indexes currently owned by the table with missing indexes). The input format is `operator + separator "" + number of indexes`, such as `>=100`.
        self.index_count = index_count
        # The list of indexes.
        self.indexes = indexes
        # The message returned for the call. Valid values:
        # - **Success**: The request is successful. 
        # - Specific error message: returned when the request fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The name of the database.  
        # 
        # > <br>If this parameter is specified, subsequent migration or synchronization operations are performed only on this database.
        self.schema = schema
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        if self.indexes:
            for v1 in self.indexes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_count is not None:
            result['IndexCount'] = self.index_count

        result['Indexes'] = []
        if self.indexes is not None:
            for k1 in self.indexes:
                result['Indexes'].append(k1.to_map() if k1 else None)

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
        if m.get('IndexCount') is not None:
            self.index_count = m.get('IndexCount')

        self.indexes = []
        if m.get('Indexes') is not None:
            for k1 in m.get('Indexes'):
                temp_model = main_models.DescribeAdbMySqlIndexesResponseBodyIndexes()
                self.indexes.append(temp_model.from_map(k1))

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

class DescribeAdbMySqlIndexesResponseBodyIndexes(DaraModel):
    def __init__(
        self,
        column: str = None,
        name: str = None,
        type: str = None,
    ):
        # The name of the column.
        self.column = column
        # The name of the index.
        self.name = name
        # The type of the index.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

