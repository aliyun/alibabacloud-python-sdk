# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBackupJobsRequest(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        dbinstance_id: str = None,
    ):
        # The backup mode. Valid values:
        # 
        # *   Automated
        # *   Manual
        # 
        # If you do not specify this parameter, all backup sets are returned.
        self.backup_mode = backup_mode
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

