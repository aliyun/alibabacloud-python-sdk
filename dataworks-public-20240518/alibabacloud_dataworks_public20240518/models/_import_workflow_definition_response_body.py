# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ImportWorkflowDefinitionResponseBody(DaraModel):
    def __init__(
        self,
        async_job: main_models.ImportWorkflowDefinitionResponseBodyAsyncJob = None,
        request_id: str = None,
    ):
        # The asynchronous task status information.
        self.async_job = async_job
        # The request ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.async_job:
            self.async_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_job is not None:
            result['AsyncJob'] = self.async_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncJob') is not None:
            temp_model = main_models.ImportWorkflowDefinitionResponseBodyAsyncJob()
            self.async_job = temp_model.from_map(m.get('AsyncJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ImportWorkflowDefinitionResponseBodyAsyncJob(DaraModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: int = None,
        error: str = None,
        id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the asynchronous task is complete.
        self.completed = completed
        # The timestamp when the asynchronous task was created.
        self.create_time = create_time
        # The error message when the asynchronous task fails.
        self.error = error
        # The ID of the asynchronous task.
        self.id = id
        # The progress of the asynchronous task. Valid values: 0 to 100.
        self.progress = progress
        # The content that the asynchronous task is expected to return.
        # 
        # > This field currently stores the ID of the workflow created in the asynchronous task.
        self.response = response
        # The status of the asynchronous task.
        # 
        # Valid values:
        # 
        # - Running: The task is running.
        # - Success: The task succeeded.
        # - Fail: The task failed.
        # - Cancel: The task was canceled.
        self.status = status
        # The operation type of the asynchronous task.
        # 
        # Valid values:
        # 
        # - Create: creates a resource. 
        # - Cancel: cancels a creation task.
        self.type = type

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

        if self.response is not None:
            result['Response'] = self.response

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('Response') is not None:
            self.response = m.get('Response')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

