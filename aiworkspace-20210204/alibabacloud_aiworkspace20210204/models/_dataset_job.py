# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DatasetJob(DaraModel):
    def __init__(
        self,
        completed_file_count: int = None,
        create_time: str = None,
        dataset_job_id: str = None,
        dataset_version: str = None,
        description: str = None,
        failed_file_count: int = None,
        finish_time: str = None,
        job_action: str = None,
        job_mode: str = None,
        job_spec: str = None,
        logs: List[str] = None,
        status: str = None,
        total_file_count: int = None,
        workspace_id: str = None,
    ):
        self.completed_file_count = completed_file_count
        self.create_time = create_time
        self.dataset_job_id = dataset_job_id
        self.dataset_version = dataset_version
        self.description = description
        self.failed_file_count = failed_file_count
        self.finish_time = finish_time
        self.job_action = job_action
        self.job_mode = job_mode
        self.job_spec = job_spec
        self.logs = logs
        self.status = status
        self.total_file_count = total_file_count
        self.workspace_id = workspace_id

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

        if self.dataset_job_id is not None:
            result['DatasetJobId'] = self.dataset_job_id

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

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

        if self.status is not None:
            result['Status'] = self.status

        if self.total_file_count is not None:
            result['TotalFileCount'] = self.total_file_count

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedFileCount') is not None:
            self.completed_file_count = m.get('CompletedFileCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetJobId') is not None:
            self.dataset_job_id = m.get('DatasetJobId')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalFileCount') is not None:
            self.total_file_count = m.get('TotalFileCount')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

