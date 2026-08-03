# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ListRecycleBinJobsResponseBody(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListRecycleBinJobsResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of task information in the recycle bin.
        self.jobs = jobs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of tasks per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of tasks in the recycle bin.
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListRecycleBinJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecycleBinJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        file_id: str = None,
        file_name: str = None,
        id: str = None,
        progress: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the task was created. The time follows the ISO 8601 standard in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The error code.
        # 
        # This value is valid only when Status is Fail or PartialSuccess.
        self.error_code = error_code
        # The error message.
        # 
        # This value is valid only when JobStatus is Fail or PartialSuccess.
        self.error_message = error_message
        # The FileId of the file or directory associated with the task.
        self.file_id = file_id
        # The name of the file or directory associated with the task.
        self.file_name = file_name
        # The task ID.
        self.id = id
        # The execution progress of the task.
        # 
        # Valid values: 1 to 100.
        self.progress = progress
        # The task status. Valid values:
        # 
        # - Running: The task is running.
        # - Defragmenting: Data is being defragmented.
        # - PartialSuccess: The task partially succeeded.
        # - Success: The task succeeded.
        # - Fail: The task failed.
        # - Cancelled: The task is canceled.
        self.status = status
        # The task type. Valid values:
        # 
        # - Restore: A file restoration task.
        # - Delete: A file deletion task.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

