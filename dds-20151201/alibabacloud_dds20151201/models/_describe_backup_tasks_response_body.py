# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupTasksResponseBody(DaraModel):
    def __init__(
        self,
        backup_jobs: List[main_models.DescribeBackupTasksResponseBodyBackupJobs] = None,
        request_id: str = None,
    ):
        # The details of the backup task.
        self.backup_jobs = backup_jobs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.backup_jobs:
            for v1 in self.backup_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupJobs'] = []
        if self.backup_jobs is not None:
            for k1 in self.backup_jobs:
                result['BackupJobs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_jobs = []
        if m.get('BackupJobs') is not None:
            for k1 in m.get('BackupJobs'):
                temp_model = main_models.DescribeBackupTasksResponseBodyBackupJobs()
                self.backup_jobs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupTasksResponseBodyBackupJobs(DaraModel):
    def __init__(
        self,
        backup_set_status: str = None,
        backup_start_time: str = None,
        backupjob_id: str = None,
        job_mode: str = None,
        progress: str = None,
    ):
        # The backup task status. Valid values:
        # 
        # *   **Scheduled**: The backup task is in planning. Regular backup tasks that have not started are also in this state.
        # *   **Checking**: The instance is being checked before the backup.
        # *   **Backuping**: The backup task is in progress.
        # *   **Finished**: The backup task is completed.
        self.backup_set_status = backup_set_status
        # The start time of the backup task.
        self.backup_start_time = backup_start_time
        # The ID of the backup task.
        self.backupjob_id = backupjob_id
        # The backup mode. Valid values:
        # 
        # *   **Automated**: automatic backup
        # *   **Manual**: manual backup
        self.job_mode = job_mode
        # The progress of the backup task. Unit: %. The progress is returned only for running backup tasks.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_status is not None:
            result['BackupSetStatus'] = self.backup_set_status

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backupjob_id is not None:
            result['BackupjobId'] = self.backupjob_id

        if self.job_mode is not None:
            result['JobMode'] = self.job_mode

        if self.progress is not None:
            result['Progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetStatus') is not None:
            self.backup_set_status = m.get('BackupSetStatus')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupjobId') is not None:
            self.backupjob_id = m.get('BackupjobId')

        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        return self

