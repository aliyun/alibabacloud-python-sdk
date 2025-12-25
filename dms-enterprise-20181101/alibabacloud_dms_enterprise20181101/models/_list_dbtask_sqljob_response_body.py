# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDBTaskSQLJobResponseBody(DaraModel):
    def __init__(
        self,
        dbtask_sqljob_list: List[main_models.ListDBTaskSQLJobResponseBodyDBTaskSQLJobList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of the SQL tasks.
        self.dbtask_sqljob_list = dbtask_sqljob_list
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of the SQL tasks.
        self.total_count = total_count

    def validate(self):
        if self.dbtask_sqljob_list:
            for v1 in self.dbtask_sqljob_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBTaskSQLJobList'] = []
        if self.dbtask_sqljob_list is not None:
            for k1 in self.dbtask_sqljob_list:
                result['DBTaskSQLJobList'].append(k1.to_map() if k1 else None)

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
        self.dbtask_sqljob_list = []
        if m.get('DBTaskSQLJobList') is not None:
            for k1 in m.get('DBTaskSQLJobList'):
                temp_model = main_models.ListDBTaskSQLJobResponseBodyDBTaskSQLJobList()
                self.dbtask_sqljob_list.append(temp_model.from_map(k1))

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

class ListDBTaskSQLJobResponseBodyDBTaskSQLJobList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: str = None,
        db_id: int = None,
        db_search_name: str = None,
        db_task_group_id: int = None,
        job_id: int = None,
        job_type: str = None,
        last_exec_time: str = None,
        logic: bool = None,
        status: str = None,
        transactional: bool = None,
    ):
        # The description of the SQL task.
        self.comment = comment
        # The time when the SQL task was created.
        self.create_time = create_time
        # The ID of the database.
        self.db_id = db_id
        # The name that is used to search for the database.
        self.db_search_name = db_search_name
        # The ID of the SQL task group.
        self.db_task_group_id = db_task_group_id
        # The ID of the SQL task.
        self.job_id = job_id
        # The type of the SQL task.
        self.job_type = job_type
        # The time when the SQL task was last executed.
        self.last_exec_time = last_exec_time
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is a logical database.
        self.logic = logic
        # The state of the SQL task. Valid values:
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
        # Indicates whether the SQL task is executed as a transaction. Valid values:
        # 
        # *   **true**: The SQL task is executed as a transaction.
        # *   **false**: The SQL task is not executed as a transaction.
        self.transactional = transactional

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name

        if self.db_task_group_id is not None:
            result['DbTaskGroupId'] = self.db_task_group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.last_exec_time is not None:
            result['LastExecTime'] = self.last_exec_time

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.status is not None:
            result['Status'] = self.status

        if self.transactional is not None:
            result['Transactional'] = self.transactional

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')

        if m.get('DbTaskGroupId') is not None:
            self.db_task_group_id = m.get('DbTaskGroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('LastExecTime') is not None:
            self.last_exec_time = m.get('LastExecTime')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Transactional') is not None:
            self.transactional = m.get('Transactional')

        return self

