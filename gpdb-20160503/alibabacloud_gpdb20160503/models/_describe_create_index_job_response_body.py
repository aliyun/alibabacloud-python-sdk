# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeCreateIndexJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.DescribeCreateIndexJobResponseBodyJob = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The details of the index creation task.
        self.job = job
        # The detailed information returned by the API operation.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The execution status of the API operation. Valid values:
        # - **success**: Successful.
        # - **fail**: Failed.
        self.status = status

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = main_models.DescribeCreateIndexJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeCreateIndexJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        id: str = None,
        progress: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # Indicates whether the operation is completed.
        self.completed = completed
        # The time when the task was created.
        self.create_time = create_time
        # The error message returned when the current operation encounters an exception or fails.
        self.error = error
        # The job ID.
        self.id = id
        # The creation progress. This value is a percentage, and a value of 100 indicates that the task is completed.
        # 
        # >- Only AnalyticDB for PostgreSQL 7.0 instances support progress updates.
        self.progress = progress
        # The task status. Valid values:
        # - **Success**: Successful.
        # - **Failed**: Failed. You can check the Error field for the cause of the failure.
        # - **Cancelled**: Canceled.
        # - **Running**: Running.
        self.status = status
        # The time when the task was updated.
        self.update_time = update_time

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

        if self.id is not None:
            result['Id'] = self.id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

