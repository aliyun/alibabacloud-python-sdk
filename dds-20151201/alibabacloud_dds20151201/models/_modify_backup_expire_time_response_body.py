# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupExpireTimeResponseBody(DaraModel):
    def __init__(
        self,
        backup_expire_time: str = None,
        backup_id: str = None,
        request_id: str = None,
    ):
        self.backup_expire_time = backup_expire_time
        self.backup_id = backup_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_expire_time is not None:
            result['BackupExpireTime'] = self.backup_expire_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupExpireTime') is not None:
            self.backup_expire_time = m.get('BackupExpireTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

