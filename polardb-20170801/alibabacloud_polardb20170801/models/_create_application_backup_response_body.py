# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationBackupResponseBody(DaraModel):
    def __init__(
        self,
        backup_job_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The ID of the created backup job.
        self.backup_job_id = backup_job_id
        # The request ID.
        self.request_id = request_id
        # The ID of the workflow task corresponding to the backup creation.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

