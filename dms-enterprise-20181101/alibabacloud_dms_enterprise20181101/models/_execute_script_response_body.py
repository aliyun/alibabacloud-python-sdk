# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ExecuteScriptResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        results: List[main_models.ExecuteScriptResponseBodyResults] = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message about the gateway.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The results of the SQL statements that are executed, in the format of an array. Each entry in the array indicates the result of an SQL statement.
        self.results = results
        # Indicates whether the request is successful.
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
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

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

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.ExecuteScriptResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ExecuteScriptResponseBodyResults(DaraModel):
    def __init__(
        self,
        column_names: List[str] = None,
        message: str = None,
        row_count: int = None,
        rows: List[Dict[str, Any]] = None,
        success: bool = None,
    ):
        # The fields that are queried after the SQL statement is executed.
        self.column_names = column_names
        # The error message that is returned if the SQL statement fails to be executed. For example, an error message is returned because the SQL statement is invalid.
        self.message = message
        # The total number of entries that are returned.
        self.row_count = row_count
        # The rows that are queried after the SQL statement is executed.
        self.rows = rows
        # Indicates whether the SQL statement is executed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names

        if self.message is not None:
            result['Message'] = self.message

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

