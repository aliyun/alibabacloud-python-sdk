# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupJobResponseBody(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_job_id: str = None,
        backup_mode: str = None,
        backup_status: str = None,
        process: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The backup set ID.
        # 
        # >  You can call the [DescribeDataBackups](https://help.aliyun.com/document_detail/210093.html) operation to query the IDs of all backup sets in the instance.
        self.backup_id = backup_id
        # The backup job ID.
        self.backup_job_id = backup_job_id
        # The backup mode. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The backup status. Valid values:
        # 
        # *   **schedule**
        # *   **check**
        # *   **backup**
        # *   **finish**
        self.backup_status = backup_status
        # The progress of the backup job.
        self.process = process
        # The request ID.
        self.request_id = request_id
        # The time when the backup job started. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.process is not None:
            result['Process'] = self.process

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

