# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSensitiveColumnsDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sensitive_columns_detail_list: main_models.ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The details of the sensitive field.
        self.sensitive_columns_detail_list = sensitive_columns_detail_list
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.sensitive_columns_detail_list:
            self.sensitive_columns_detail_list.validate()

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

        if self.sensitive_columns_detail_list is not None:
            result['SensitiveColumnsDetailList'] = self.sensitive_columns_detail_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SensitiveColumnsDetailList') is not None:
            temp_model = main_models.ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList()
            self.sensitive_columns_detail_list = temp_model.from_map(m.get('SensitiveColumnsDetailList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList(DaraModel):
    def __init__(
        self,
        sensitive_columns_detail: List[main_models.ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailListSensitiveColumnsDetail] = None,
    ):
        self.sensitive_columns_detail = sensitive_columns_detail

    def validate(self):
        if self.sensitive_columns_detail:
            for v1 in self.sensitive_columns_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SensitiveColumnsDetail'] = []
        if self.sensitive_columns_detail is not None:
            for k1 in self.sensitive_columns_detail:
                result['SensitiveColumnsDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_columns_detail = []
        if m.get('SensitiveColumnsDetail') is not None:
            for k1 in m.get('SensitiveColumnsDetail'):
                temp_model = main_models.ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailListSensitiveColumnsDetail()
                self.sensitive_columns_detail.append(temp_model.from_map(k1))

        return self

class ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailListSensitiveColumnsDetail(DaraModel):
    def __init__(
        self,
        column_description: str = None,
        column_name: str = None,
        column_type: str = None,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        schema_name: str = None,
        search_name: str = None,
        table_name: str = None,
    ):
        # The description of the field.
        self.column_description = column_description
        # The name of the field.
        self.column_name = column_name
        # The data type of the field.
        self.column_type = column_type
        # The ID of the database.
        self.db_id = db_id
        # The type of the database.
        self.db_type = db_type
        # The type of the environment to which the database belongs.
        self.env_type = env_type
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is not a logical database.
        self.logic = logic
        # The name of the database.
        self.schema_name = schema_name
        # The name that is used to search for the database.
        self.search_name = search_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_description is not None:
            result['ColumnDescription'] = self.column_description

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnDescription') is not None:
            self.column_description = m.get('ColumnDescription')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

