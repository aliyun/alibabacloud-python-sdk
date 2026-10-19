# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackupResponseBody(DaraModel):
    def __init__(
        self,
        backup_job_id: str = None,
        request_id: str = None,
    ):
        # The backup task ID. For cluster instances created before December 5, 2023, the return value consists of the job IDs of individual child DB nodes. For example, for a cluster instance with two shards, the BackupJobID value is returned in the format of "10000,10001". For cluster instances created on or after December 5, 2023, all DB nodes in a cluster are described by a single job ID. You only need to use this single job ID.
        self.backup_job_id = backup_job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupJobID') is not None:
            self.backup_job_id = m.get('BackupJobID')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

