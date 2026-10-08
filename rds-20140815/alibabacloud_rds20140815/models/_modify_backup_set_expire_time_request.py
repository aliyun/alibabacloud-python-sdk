# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupSetExpireTimeRequest(DaraModel):
    def __init__(
        self,
        backup_id: int = None,
        dbinstance_id: str = None,
        expect_expire_time: str = None,
        resource_owner_id: int = None,
    ):
        # The backup set ID. You can invoke DescribeBackups to query the backup set ID. The backup set must meet the following conditions:
        # 
        # - Engine (database type): SQLServer
        # - BackupMode (backup pattern): Manual (manual backup)
        # - BackupMethod: Physical (physical backup)
        # - BackupType: FullBackup (full backup)
        # - BackupStatus: Success (backup completed)
        # 
        # This parameter is required.
        self.backup_id = backup_id
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The time to which you want to extend the expiration time of the backup set. Specify the time in the yyyy-MM-ddTHH:mmZ format (UTC).
        # 
        # The specified time cannot be earlier than the current expiration time. You can call DescribeBackups to query the current expiration time (ExpectExpireTime).
        # 
        # This parameter is required.
        self.expect_expire_time = expect_expire_time
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

