# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetStructSyncExecSqlDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_exec_sql_detail: main_models.GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The details of the SQL statements.
        self.struct_sync_exec_sql_detail = struct_sync_exec_sql_detail
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.struct_sync_exec_sql_detail:
            self.struct_sync_exec_sql_detail.validate()

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

        if self.struct_sync_exec_sql_detail is not None:
            result['StructSyncExecSqlDetail'] = self.struct_sync_exec_sql_detail.to_map()

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

        if m.get('StructSyncExecSqlDetail') is not None:
            temp_model = main_models.GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail()
            self.struct_sync_exec_sql_detail = temp_model.from_map(m.get('StructSyncExecSqlDetail'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail(DaraModel):
    def __init__(
        self,
        exec_sql: str = None,
        total_sql_count: int = None,
    ):
        # The SQL statements that are executed.
        self.exec_sql = exec_sql
        # The total number of SQL statements.
        self.total_sql_count = total_sql_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec_sql is not None:
            result['ExecSql'] = self.exec_sql

        if self.total_sql_count is not None:
            result['TotalSqlCount'] = self.total_sql_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecSql') is not None:
            self.exec_sql = m.get('ExecSql')

        if m.get('TotalSqlCount') is not None:
            self.total_sql_count = m.get('TotalSqlCount')

        return self

