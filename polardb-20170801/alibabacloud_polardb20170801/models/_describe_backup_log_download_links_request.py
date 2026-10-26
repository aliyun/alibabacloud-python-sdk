# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupLogDownloadLinksRequest(DaraModel):
    def __init__(
        self,
        backup_log_ids: str = None,
        dbcluster_id: str = None,
        expire_hours: int = None,
    ):
        # The IDs of the redo log backups.
        self.backup_log_ids = backup_log_ids
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The validity period of the download links in hours. Valid values: 1 to 596523.
        self.expire_hours = expire_hours

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_log_ids is not None:
            result['BackupLogIds'] = self.backup_log_ids

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.expire_hours is not None:
            result['ExpireHours'] = self.expire_hours

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLogIds') is not None:
            self.backup_log_ids = m.get('BackupLogIds')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExpireHours') is not None:
            self.expire_hours = m.get('ExpireHours')

        return self

