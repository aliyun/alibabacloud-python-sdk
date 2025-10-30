# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetUpsertCollectionDataJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetUpsertCollectionDataJobResponseBodyJob = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The information about the vector data upload job.
        self.job = job
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
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
            temp_model = main_models.GetUpsertCollectionDataJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetUpsertCollectionDataJobResponseBodyJob(DaraModel):
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
        # Indicates whether the operation is complete.
        self.completed = completed
        # The time when the job was created.
        self.create_time = create_time
        # The error message.
        self.error = error
        # The job ID.
        self.id = id
        # The progress of the vector data upload job. The value of this parameter indicates the number of data entries that have been uploaded.
        self.progress = progress
        # The status of the job.
        # 
        # >  Valid values:
        # 
        # *   Success
        # 
        # *   Failed (See the Error parameter for failure reasons.)
        # 
        # *   Cancelling
        # 
        # *   Cancelled
        # 
        # *   Start
        # 
        # *   Running
        self.status = status
        # The time when the job was updated.
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

