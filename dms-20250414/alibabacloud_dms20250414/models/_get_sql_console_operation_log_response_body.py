# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetSqlConsoleOperationLogResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetSqlConsoleOperationLogResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response struct.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned if the call failed.
        self.error_message = error_message
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of logs.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSqlConsoleOperationLogResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetSqlConsoleOperationLogResponseBodyData(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        cost: int = None,
        database_search_name: str = None,
        error: str = None,
        schema: str = None,
        sql: str = None,
        sql_type: str = None,
        start_time: str = None,
        success: bool = None,
        username: str = None,
    ):
        # The number of affected rows.
        self.affect_rows = affect_rows
        # The execution duration. Unit: milliseconds.
        self.cost = cost
        # The database search name.
        self.database_search_name = database_search_name
        # The error message.
        self.error = error
        # The database schema.
        self.schema = schema
        # The SQL statement.
        self.sql = sql
        # The SQL type.
        self.sql_type = sql_type
        # The start time of the logs.
        self.start_time = start_time
        # Indicates whether the statement is executed.
        self.success = success
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.cost is not None:
            result['Cost'] = self.cost

        if self.database_search_name is not None:
            result['DatabaseSearchName'] = self.database_search_name

        if self.error is not None:
            result['Error'] = self.error

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.success is not None:
            result['Success'] = self.success

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('DatabaseSearchName') is not None:
            self.database_search_name = m.get('DatabaseSearchName')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

