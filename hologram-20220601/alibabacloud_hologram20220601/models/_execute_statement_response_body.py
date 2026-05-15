# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ExecuteStatementResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExecuteStatementResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

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

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ExecuteStatementResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ExecuteStatementResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        results: List[main_models.ExecuteStatementResponseBodyDataResults] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.results = results
        self.success = success

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.ExecuteStatementResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ExecuteStatementResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        column_metadata: List[main_models.ExecuteStatementResponseBodyDataResultsColumnMetadata] = None,
        count: int = None,
        error_code: str = None,
        error_message: str = None,
        query_id: str = None,
        records: List[List[str]] = None,
        sql: str = None,
        success: bool = None,
        truncated: bool = None,
        update_count: int = None,
    ):
        self.column_metadata = column_metadata
        self.count = count
        self.error_code = error_code
        self.error_message = error_message
        # **Query ID**
        self.query_id = query_id
        self.records = records
        self.sql = sql
        self.success = success
        self.truncated = truncated
        self.update_count = update_count

    def validate(self):
        if self.column_metadata:
            for v1 in self.column_metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['columnMetadata'] = []
        if self.column_metadata is not None:
            for k1 in self.column_metadata:
                result['columnMetadata'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['count'] = self.count

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.query_id is not None:
            result['queryId'] = self.query_id

        if self.records is not None:
            result['records'] = self.records

        if self.sql is not None:
            result['sql'] = self.sql

        if self.success is not None:
            result['success'] = self.success

        if self.truncated is not None:
            result['truncated'] = self.truncated

        if self.update_count is not None:
            result['updateCount'] = self.update_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_metadata = []
        if m.get('columnMetadata') is not None:
            for k1 in m.get('columnMetadata'):
                temp_model = main_models.ExecuteStatementResponseBodyDataResultsColumnMetadata()
                self.column_metadata.append(temp_model.from_map(k1))

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('queryId') is not None:
            self.query_id = m.get('queryId')

        if m.get('records') is not None:
            self.records = m.get('records')

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('truncated') is not None:
            self.truncated = m.get('truncated')

        if m.get('updateCount') is not None:
            self.update_count = m.get('updateCount')

        return self

class ExecuteStatementResponseBodyDataResultsColumnMetadata(DaraModel):
    def __init__(
        self,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.name = name
        self.nullable = nullable
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

        if self.nullable is not None:
            result['nullable'] = self.nullable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

