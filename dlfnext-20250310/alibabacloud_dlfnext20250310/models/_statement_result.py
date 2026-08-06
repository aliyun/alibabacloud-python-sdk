# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class StatementResult(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        error: str = None,
        error_code: str = None,
        execution_time: int = None,
        index: int = None,
        row_count: int = None,
        schema: List[main_models.StatementResultSchema] = None,
        sql: str = None,
        status: str = None,
    ):
        # The presigned URL of the Arrow IPC file. This parameter is returned when a result set exists. The URL is valid for 1 hour and contains full data. The value is null for an empty result set (rowCount == 0).
        self.download_url = download_url
        # The error message. This parameter is returned only when the status is FAILED.
        self.error = error
        # The error code. This parameter is returned only when the status is FAILED.
        self.error_code = error_code
        # The execution duration of the statement, in milliseconds.
        self.execution_time = execution_time
        # The statement sequence number (0-based).
        self.index = index
        # The total number of rows in the result. The value is 0 for statements that do not return a result set.
        self.row_count = row_count
        # The result column information. This parameter is returned when a result set exists.
        self.schema = schema
        # The SQL text of the statement.
        self.sql = sql
        # The status of the statement. Valid values: COMPLETED and FAILED.
        self.status = status

    def validate(self):
        if self.schema:
            for v1 in self.schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.error is not None:
            result['error'] = self.error

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.execution_time is not None:
            result['executionTime'] = self.execution_time

        if self.index is not None:
            result['index'] = self.index

        if self.row_count is not None:
            result['rowCount'] = self.row_count

        result['schema'] = []
        if self.schema is not None:
            for k1 in self.schema:
                result['schema'].append(k1.to_map() if k1 else None)

        if self.sql is not None:
            result['sql'] = self.sql

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('executionTime') is not None:
            self.execution_time = m.get('executionTime')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('rowCount') is not None:
            self.row_count = m.get('rowCount')

        self.schema = []
        if m.get('schema') is not None:
            for k1 in m.get('schema'):
                temp_model = main_models.StatementResultSchema()
                self.schema.append(temp_model.from_map(k1))

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class StatementResultSchema(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The column name.
        self.name = name
        # The data type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

