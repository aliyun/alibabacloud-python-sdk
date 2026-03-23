# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMigrateTaskRequest(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        check_dbmode: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        is_online_db: str = None,
        migrate_task_id: str = None,
        ossurls: str = None,
        oss_object_positions: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.backup_mode = backup_mode
        self.check_dbmode = check_dbmode
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.dbname = dbname
        # This parameter is required.
        self.is_online_db = is_online_db
        self.migrate_task_id = migrate_task_id
        self.ossurls = ossurls
        self.oss_object_positions = oss_object_positions
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.check_dbmode is not None:
            result['CheckDBMode'] = self.check_dbmode

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.is_online_db is not None:
            result['IsOnlineDB'] = self.is_online_db

        if self.migrate_task_id is not None:
            result['MigrateTaskId'] = self.migrate_task_id

        if self.ossurls is not None:
            result['OSSUrls'] = self.ossurls

        if self.oss_object_positions is not None:
            result['OssObjectPositions'] = self.oss_object_positions

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('CheckDBMode') is not None:
            self.check_dbmode = m.get('CheckDBMode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('IsOnlineDB') is not None:
            self.is_online_db = m.get('IsOnlineDB')

        if m.get('MigrateTaskId') is not None:
            self.migrate_task_id = m.get('MigrateTaskId')

        if m.get('OSSUrls') is not None:
            self.ossurls = m.get('OSSUrls')

        if m.get('OssObjectPositions') is not None:
            self.oss_object_positions = m.get('OssObjectPositions')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

