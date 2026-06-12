# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackupResponseBody(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        description: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The description.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The status of the backup.
        # 
        # - Creating: The backup is being created.
        # 
        # - Created: The backup is created.
        # 
        # - CreateFailed: The backup failed to be created.
        # 
        # - Deleting: The backup is being deleted.
        # 
        # - Deleted: The backup is deleted.
        # 
        # - DeleteFailed: The backup failed to be deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

