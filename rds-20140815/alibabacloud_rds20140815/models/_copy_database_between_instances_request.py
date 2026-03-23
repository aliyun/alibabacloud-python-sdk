# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyDatabaseBetweenInstancesRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        dbinstance_id: str = None,
        db_names: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        sync_user_privilege: str = None,
        target_dbinstance_id: str = None,
    ):
        self.backup_id = backup_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.db_names = db_names
        self.resource_owner_id = resource_owner_id
        self.restore_time = restore_time
        self.sync_user_privilege = sync_user_privilege
        # This parameter is required.
        self.target_dbinstance_id = target_dbinstance_id

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

        if self.db_names is not None:
            result['DbNames'] = self.db_names

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.sync_user_privilege is not None:
            result['SyncUserPrivilege'] = self.sync_user_privilege

        if self.target_dbinstance_id is not None:
            result['TargetDBInstanceId'] = self.target_dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SyncUserPrivilege') is not None:
            self.sync_user_privilege = m.get('SyncUserPrivilege')

        if m.get('TargetDBInstanceId') is not None:
            self.target_dbinstance_id = m.get('TargetDBInstanceId')

        return self

