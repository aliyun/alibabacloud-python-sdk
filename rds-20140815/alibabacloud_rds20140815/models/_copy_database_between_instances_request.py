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
        # The ID of the backup set based on which you want to restore databases of the source instance. When you replicate databases by backup set, you can call the DescribeBackups operation to obtain the ID of the backup set.
        # 
        # >  You must specify one of the **BackupId** and **RestoreTime** parameters.
        self.backup_id = backup_id
        # The source instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The names of the databases that you want to copy. Format: `Source database name 1,Source database name 2`.
        # 
        # This parameter is required.
        self.db_names = db_names
        self.resource_owner_id = resource_owner_id
        # The point in time when the system replicates databases. You can select a point in time within the backup retention period. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > You must specify one of the **BackupId** and **RestoreTime** parameters.
        self.restore_time = restore_time
        # Specifies whether to copy users and permissions.
        # 
        # *   **YES**: copies users and permissions. If the destination instance has a user whose name is the same as a user in the source instance, the permissions of the user in the source instance will also be granted to the user in the destination instance after you copy user permissions.
        # *   **NO**: does not copy users and permissions.
        # 
        # Default value: **NO**.
        self.sync_user_privilege = sync_user_privilege
        # The destination instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
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

