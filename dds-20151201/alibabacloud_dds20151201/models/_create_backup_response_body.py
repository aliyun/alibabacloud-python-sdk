# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackupResponseBody(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the backup set.
        self.backup_id = backup_id
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
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

