# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupTasksResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeBackupTasksResponseBodyItems = None,
        request_id: str = None,
    ):
        # The details of the backup task.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeBackupTasksResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_job: List[main_models.DescribeBackupTasksResponseBodyItemsBackupJob] = None,
    ):
        self.backup_job = backup_job

    def validate(self):
        if self.backup_job:
            for v1 in self.backup_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupJob'] = []
        if self.backup_job is not None:
            for k1 in self.backup_job:
                result['BackupJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_job = []
        if m.get('BackupJob') is not None:
            for k1 in m.get('BackupJob'):
                temp_model = main_models.DescribeBackupTasksResponseBodyItemsBackupJob()
                self.backup_job.append(temp_model.from_map(k1))

        return self

class DescribeBackupTasksResponseBodyItemsBackupJob(DaraModel):
    def __init__(
        self,
        backup_job_id: str = None,
        backup_progress_status: str = None,
        job_mode: str = None,
        process: str = None,
        start_time: str = None,
        task_action: str = None,
    ):
        # The ID of the backup task.
        self.backup_job_id = backup_job_id
        # The state of the backup task. Valid values:
        # 
        # *   **NoStart**
        # *   **Preparing**
        # *   **Waiting**
        # *   **Uploading**
        # *   **Checking**
        # *   **Finished**
        self.backup_progress_status = backup_progress_status
        # The backup mode. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.job_mode = job_mode
        # The progress of the backup task in percentage.
        self.process = process
        # The time when the backup task started. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        self.start_time = start_time
        # The type of the backup task. Valid values:
        # 
        # *   **TempBackupTask**: The backup task is an adhoc backup task.
        # *   **NormalBackupTask**: The backup task is a common backup task.
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.backup_progress_status is not None:
            result['BackupProgressStatus'] = self.backup_progress_status

        if self.job_mode is not None:
            result['JobMode'] = self.job_mode

        if self.process is not None:
            result['Process'] = self.process

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('BackupProgressStatus') is not None:
            self.backup_progress_status = m.get('BackupProgressStatus')

        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        return self

