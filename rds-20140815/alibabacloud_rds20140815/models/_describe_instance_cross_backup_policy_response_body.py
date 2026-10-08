# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceCrossBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        backup_enabled: str = None,
        backup_enabled_time: str = None,
        cross_backup_region: str = None,
        cross_backup_type: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        engine: str = None,
        engine_version: str = None,
        lock_mode: str = None,
        log_backup_enabled: str = None,
        log_backup_enabled_time: str = None,
        region_id: str = None,
        request_id: str = None,
        retent_type: int = None,
        retention: int = None,
    ):
        # The status of the cross-region backup feature. Valid values:
        # * **Disable**: disabled.
        # * **Enable**: enabled.
        self.backup_enabled = backup_enabled
        # The time when cross-region backup was enabled. The time follows the ISO 8601 standard in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.backup_enabled_time = backup_enabled_time
        # The ID of the destination region for cross-region backup.
        self.cross_backup_region = cross_backup_region
        # The storage type for cross-region backup. Default value: **1**, which indicates that each backup is retained.
        self.cross_backup_type = cross_backup_type
        # The instance name. The name is 2 to 256 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter or a Chinese character.
        # >The name cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The instance status. For more information, see [Instance states](https://help.aliyun.com/document_detail/26315.html).
        self.dbinstance_status = dbinstance_status
        # The database engine.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The lock status of the instance. Valid values:
        # * **Unlock**: The instance is not locked.
        # * **ManualLock**: The instance is manually locked.
        # * **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # * **LockByRestoration**: The instance is automatically locked before a rollback.
        # * **LockByDiskQuota**: The instance is automatically locked because the storage space is exhausted. The instance is inaccessible.
        self.lock_mode = lock_mode
        # The status of the cross-region log backup feature. Valid values:
        # * **Disable**: disabled.
        # * **Enable**: enabled.
        self.log_backup_enabled = log_backup_enabled
        # The time when cross-region log backup was enabled. The time follows the ISO 8601 standard in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.log_backup_enabled_time = log_backup_enabled_time
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The retention method for cross-region backup. Default value: **1**, which indicates that backups are retained based on the specified retention period.
        self.retent_type = retent_type
        # The number of days for which cross-region backups are retained. Valid values: **7 to 1825**.
        self.retention = retention

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_enabled is not None:
            result['BackupEnabled'] = self.backup_enabled

        if self.backup_enabled_time is not None:
            result['BackupEnabledTime'] = self.backup_enabled_time

        if self.cross_backup_region is not None:
            result['CrossBackupRegion'] = self.cross_backup_region

        if self.cross_backup_type is not None:
            result['CrossBackupType'] = self.cross_backup_type

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.log_backup_enabled is not None:
            result['LogBackupEnabled'] = self.log_backup_enabled

        if self.log_backup_enabled_time is not None:
            result['LogBackupEnabledTime'] = self.log_backup_enabled_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retent_type is not None:
            result['RetentType'] = self.retent_type

        if self.retention is not None:
            result['Retention'] = self.retention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEnabled') is not None:
            self.backup_enabled = m.get('BackupEnabled')

        if m.get('BackupEnabledTime') is not None:
            self.backup_enabled_time = m.get('BackupEnabledTime')

        if m.get('CrossBackupRegion') is not None:
            self.cross_backup_region = m.get('CrossBackupRegion')

        if m.get('CrossBackupType') is not None:
            self.cross_backup_type = m.get('CrossBackupType')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LogBackupEnabled') is not None:
            self.log_backup_enabled = m.get('LogBackupEnabled')

        if m.get('LogBackupEnabledTime') is not None:
            self.log_backup_enabled_time = m.get('LogBackupEnabledTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetentType') is not None:
            self.retent_type = m.get('RetentType')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        return self

