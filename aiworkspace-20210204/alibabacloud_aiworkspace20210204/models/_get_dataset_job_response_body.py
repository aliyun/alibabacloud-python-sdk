# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetDatasetJobResponseBody(DaraModel):
    def __init__(
        self,
        completed_file_count: int = None,
        create_time: str = None,
        description: str = None,
        failed_file_count: int = None,
        finish_time: str = None,
        job_action: str = None,
        job_mode: str = None,
        job_spec: str = None,
        logs: List[str] = None,
        request_id: str = None,
        status: str = None,
        total_file_count: int = None,
    ):
        # The total number of completed files.
        self.completed_file_count = completed_file_count
        # The time when the job is started.
        self.create_time = create_time
        # The job description.
        self.description = description
        # The total number of failed files.
        self.failed_file_count = failed_file_count
        # The time when the job ends.
        self.finish_time = finish_time
        # The action that is performed on the job.
        # 
        # Valid values:
        # 
        # *   SemanticIndex: semantic indexing
        # *   IntelligentTag: smart labeling
        # *   FileMetaExport: metadata export
        self.job_action = job_action
        # The job mode.
        # 
        # Valid value:
        # 
        # *   Full: full data mode.
        self.job_mode = job_mode
        # The job details.
        self.job_spec = job_spec
        # The job logs.
        self.logs = logs
        # The request ID.
        self.request_id = request_id
        # The job state.
        # 
        # Valid values:
        # 
        # *   Succeeded
        # *   Failed
        # *   Running
        # *   Pending
        # *   PartialFailed
        # *   Deleting
        # *   ManuallyStop
        self.status = status
        # The total number of job files.
        self.total_file_count = total_file_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_file_count is not None:
            result['CompletedFileCount'] = self.completed_file_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.failed_file_count is not None:
            result['FailedFileCount'] = self.failed_file_count

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.job_action is not None:
            result['JobAction'] = self.job_action

        if self.job_mode is not None:
            result['JobMode'] = self.job_mode

        if self.job_spec is not None:
            result['JobSpec'] = self.job_spec

        if self.logs is not None:
            result['Logs'] = self.logs

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_file_count is not None:
            result['TotalFileCount'] = self.total_file_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedFileCount') is not None:
            self.completed_file_count = m.get('CompletedFileCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FailedFileCount') is not None:
            self.failed_file_count = m.get('FailedFileCount')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')

        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')

        if m.get('JobSpec') is not None:
            self.job_spec = m.get('JobSpec')

        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalFileCount') is not None:
            self.total_file_count = m.get('TotalFileCount')

        return self

