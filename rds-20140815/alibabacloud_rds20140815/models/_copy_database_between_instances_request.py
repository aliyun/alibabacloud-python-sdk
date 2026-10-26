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
        # The ID of the backup set of the source instance. When you copy a database based on a backup set, you can call the DescribeBackups operation to query the backup set ID.
        # >When you call this operation, you must specify either **BackupId** or **RestoreTime**.
        self.backup_id = backup_id
        # The ID of the source instance. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The names of the databases to be copied. Specify the names in the following format: `{"Source database name":"Target database name"}`. Separate multiple databases with commas (,). Examples:
        # 
        # - Copy a single database: `{"zhttest":"zhttest"}`
        # - Copy multiple databases: `{"zhttest01":"zhttest01","zhttest02":"zhttest02"}`
        # 
        # > The name of the database in the target instance can be different from that in the source instance. However, before copying, make sure that the target instance does not contain a database with the same name.
        # 
        # This parameter is required.
        self.db_names = db_names
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore the database. You can select any point in time within the backup retention period. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time must be in UTC.
        # >When you call this operation, you must specify either **BackupId** or **RestoreTime**.
        self.restore_time = restore_time
        # Specifies whether to enable the replication of users and permissions. Valid values:
        # * **YES**: Enables the replication of users and permissions. If the target instance contains a user with the same name as a user in the source instance, the permissions of the source user are added to the target user.
        # * **NO**: Disables the replication of users and permissions. This is the default value.
        self.sync_user_privilege = sync_user_privilege
        # The ID of the target instance. You can call the DescribeDBInstances operation to query the instance ID.
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

