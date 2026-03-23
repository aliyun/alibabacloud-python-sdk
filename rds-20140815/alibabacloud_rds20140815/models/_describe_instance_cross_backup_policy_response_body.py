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
        self.backup_enabled = backup_enabled
        self.backup_enabled_time = backup_enabled_time
        self.cross_backup_region = cross_backup_region
        self.cross_backup_type = cross_backup_type
        self.dbinstance_description = dbinstance_description
        self.dbinstance_id = dbinstance_id
        self.dbinstance_status = dbinstance_status
        self.engine = engine
        self.engine_version = engine_version
        self.lock_mode = lock_mode
        self.log_backup_enabled = log_backup_enabled
        self.log_backup_enabled_time = log_backup_enabled_time
        self.region_id = region_id
        self.request_id = request_id
        self.retent_type = retent_type
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

