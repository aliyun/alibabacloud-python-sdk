# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDBTaskSQLJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        dbtask_sqljob_detail_list: List[main_models.ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of SQL tasks.
        self.dbtask_sqljob_detail_list = dbtask_sqljob_detail_list
        # The error code that is returned.
        self.error_code = error_code
        # The error message that is returned.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success
        # The total number of SQL tasks.
        self.total_count = total_count

    def validate(self):
        if self.dbtask_sqljob_detail_list:
            for v1 in self.dbtask_sqljob_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBTaskSQLJobDetailList'] = []
        if self.dbtask_sqljob_detail_list is not None:
            for k1 in self.dbtask_sqljob_detail_list:
                result['DBTaskSQLJobDetailList'].append(k1.to_map() if k1 else None)

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
        self.dbtask_sqljob_detail_list = []
        if m.get('DBTaskSQLJobDetailList') is not None:
            for k1 in m.get('DBTaskSQLJobDetailList'):
                temp_model = main_models.ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList()
                self.dbtask_sqljob_detail_list.append(temp_model.from_map(k1))

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

class ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        current_sql: str = None,
        db_id: int = None,
        end_time: str = None,
        execute_count: int = None,
        job_detail_id: int = None,
        job_id: int = None,
        log: str = None,
        logic: bool = None,
        skip: bool = None,
        sql_type: str = None,
        start_time: str = None,
        status: str = None,
        time_delay: int = None,
    ):
        # The number of rows affected by the SQL task.
        self.affect_rows = affect_rows
        # The SQL statement that was executed in the SQL task.
        self.current_sql = current_sql
        # The ID of the physical database.
        self.db_id = db_id
        # The point in time when the SQL task ended.
        self.end_time = end_time
        # The number of times that the SQL statement was executed.
        self.execute_count = execute_count
        # The ID of the details of the SQL task.
        self.job_detail_id = job_detail_id
        # The ID of the SQL task.
        self.job_id = job_id
        # The details of the operational log.
        self.log = log
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is a physical database.
        self.logic = logic
        # Indicates whether the SQL statement was skipped. Valid values:
        # 
        # *   **true**: The SQL statement was skipped.
        # *   **false**: The SQL statement was not skipped.
        self.skip = skip
        # The type of the SQL statement, such as DELETE, UPDATE, or ALTER_TABLE.
        self.sql_type = sql_type
        # The point in time when the SQL task started.
        self.start_time = start_time
        # The status of the SQL task. Valid values:
        # 
        # *   **INIT**: The SQL task was initialized.
        # *   **PENDING**: The SQL task waited to be run.
        # *   **BE_SCHEDULED**: The SQL task waited to be scheduled.
        # *   **FAIL**: The SQL task failed.
        # *   **SUCCESS**: The SQL task was successful.
        # *   **PAUSE**: The SQL task was paused.
        # *   **DELETE**: The SQL task was deleted.
        # *   **RUNNING**: The SQL task was being run.
        self.status = status
        # The duration of the SQL task. Unit: milliseconds.
        self.time_delay = time_delay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.current_sql is not None:
            result['CurrentSql'] = self.current_sql

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.execute_count is not None:
            result['ExecuteCount'] = self.execute_count

        if self.job_detail_id is not None:
            result['JobDetailId'] = self.job_detail_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.log is not None:
            result['Log'] = self.log

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.time_delay is not None:
            result['TimeDelay'] = self.time_delay

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('CurrentSql') is not None:
            self.current_sql = m.get('CurrentSql')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')

        if m.get('JobDetailId') is not None:
            self.job_detail_id = m.get('JobDetailId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeDelay') is not None:
            self.time_delay = m.get('TimeDelay')

        return self

