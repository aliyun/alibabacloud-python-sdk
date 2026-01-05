# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetJobStatusResponseBody(DaraModel):
    def __init__(
        self,
        job_status: main_models.GetJobStatusResponseBodyJobStatus = None,
        request_id: str = None,
    ):
        # The real-time status information of the asynchronous task.
        self.job_status = job_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job_status:
            self.job_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_status is not None:
            result['JobStatus'] = self.job_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobStatus') is not None:
            temp_model = main_models.GetJobStatusResponseBodyJobStatus()
            self.job_status = temp_model.from_map(m.get('JobStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetJobStatusResponseBodyJobStatus(DaraModel):
    def __init__(
        self,
        completed: str = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        job_type: str = None,
        status: str = None,
    ):
        # Indicates whether the asynchronous task is complete. Valid values: True False
        self.completed = completed
        # The time when the asynchronous task was created.
        self.create_time = create_time
        # The error message returned if the asynchronous task fails.
        self.error = error
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The type of the asynchronous task. Valid values:
        # 
        # *   **Create**: The asynchronous task is used to create an object.
        # *   **Update**: The asynchronous task is used to update an object.
        # *   **Cancel**: The asynchronous task is used to cancel an operation.
        self.job_type = job_type
        # The status of the asynchronous task. Valid values:
        # 
        # *   **Success**
        # *   **Fail**
        # *   **Cancel**
        # *   **Running**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed is not None:
            result['Completed'] = self.completed

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error is not None:
            result['Error'] = self.error

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

