# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataCorrectTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_correct_task_detail: main_models.GetDataCorrectTaskDetailResponseBodyDataCorrectTaskDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data change task.
        self.data_correct_task_detail = data_correct_task_detail
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data_correct_task_detail:
            self.data_correct_task_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_correct_task_detail is not None:
            result['DataCorrectTaskDetail'] = self.data_correct_task_detail.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCorrectTaskDetail') is not None:
            temp_model = main_models.GetDataCorrectTaskDetailResponseBodyDataCorrectTaskDetail()
            self.data_correct_task_detail = temp_model.from_map(m.get('DataCorrectTaskDetail'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataCorrectTaskDetailResponseBodyDataCorrectTaskDetail(DaraModel):
    def __init__(
        self,
        actual_affect_rows: int = None,
        create_time: str = None,
        dbtask_group_id: int = None,
        job_status: str = None,
    ):
        # The number of rows affected by the SQL statement.
        self.actual_affect_rows = actual_affect_rows
        # The time when the task was created.
        self.create_time = create_time
        # The ID of the SQL task group.
        self.dbtask_group_id = dbtask_group_id
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
        self.job_status = job_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id

        if self.job_status is not None:
            result['jobStatus'] = self.job_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')

        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')

        return self

