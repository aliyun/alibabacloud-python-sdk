# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetSqlStatementResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSqlStatementResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetSqlStatementResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetSqlStatementResponseBodyData(DaraModel):
    def __init__(
        self,
        execution_time: List[int] = None,
        sql_error_code: str = None,
        sql_error_message: str = None,
        sql_outputs: List[main_models.GetSqlStatementResponseBodyDataSqlOutputs] = None,
        state: str = None,
        statement_id: str = None,
    ):
        # The list of time that is consumed by SQL queries.
        self.execution_time = execution_time
        # The error code.
        self.sql_error_code = sql_error_code
        # The error message.
        self.sql_error_message = sql_error_message
        # The query results.
        self.sql_outputs = sql_outputs
        # The query status.
        # 
        # Valid values:
        # 
        # *   running
        # *   available
        # *   cancelled
        # *   error
        # *   cancelling
        self.state = state
        # The query ID.
        self.statement_id = statement_id

    def validate(self):
        if self.sql_outputs:
            for v1 in self.sql_outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_time is not None:
            result['executionTime'] = self.execution_time

        if self.sql_error_code is not None:
            result['sqlErrorCode'] = self.sql_error_code

        if self.sql_error_message is not None:
            result['sqlErrorMessage'] = self.sql_error_message

        result['sqlOutputs'] = []
        if self.sql_outputs is not None:
            for k1 in self.sql_outputs:
                result['sqlOutputs'].append(k1.to_map() if k1 else None)

        if self.state is not None:
            result['state'] = self.state

        if self.statement_id is not None:
            result['statementId'] = self.statement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionTime') is not None:
            self.execution_time = m.get('executionTime')

        if m.get('sqlErrorCode') is not None:
            self.sql_error_code = m.get('sqlErrorCode')

        if m.get('sqlErrorMessage') is not None:
            self.sql_error_message = m.get('sqlErrorMessage')

        self.sql_outputs = []
        if m.get('sqlOutputs') is not None:
            for k1 in m.get('sqlOutputs'):
                temp_model = main_models.GetSqlStatementResponseBodyDataSqlOutputs()
                self.sql_outputs.append(temp_model.from_map(k1))

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('statementId') is not None:
            self.statement_id = m.get('statementId')

        return self

class GetSqlStatementResponseBodyDataSqlOutputs(DaraModel):
    def __init__(
        self,
        rows: str = None,
        rows_file_path: str = None,
        schema: str = None,
    ):
        # The queried data, which is a string in the JSON format.
        self.rows = rows
        self.rows_file_path = rows_file_path
        # The information about the schema, which is a string in the JSON format.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rows is not None:
            result['rows'] = self.rows

        if self.rows_file_path is not None:
            result['rowsFilePath'] = self.rows_file_path

        if self.schema is not None:
            result['schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = m.get('rows')

        if m.get('rowsFilePath') is not None:
            self.rows_file_path = m.get('rowsFilePath')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        return self

