# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        compress_type: str = None,
        dbinstance_id: str = None,
        enable_backup_log: str = None,
        high_space_usage_protection: str = None,
        local_log_retention_hours: int = None,
        local_log_retention_space: str = None,
        log_backup_local_retention_number: int = None,
        request_id: str = None,
    ):
        # The method that is used to compress backups. Valid values:
        # 
        # *   **0:** Backups are not compressed.
        # *   **1**: Backups are compressed by using the zlib tool.
        # *   **2**: Backups are compressed in parallel by using the zlib tool.
        # *   **4**: Backups are compressed by using the QuickLZ tool and can be used to restore individual databases and tables.
        # *   **8**: Backups are compressed by using the QuickLZ tool but cannot be used to restore individual databases or tables. This value is supported only for instances that run MySQL 8.0.
        self.compress_type = compress_type
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # Indicates whether the log backup feature is enabled. Valid values:
        # 
        # *   **1**: The feature is enabled.
        # *   **0**: The feature is disabled.
        self.enable_backup_log = enable_backup_log
        # Specifies whether to forcefully delete log backup files from the instance when the storage usage of the instance exceeds 80% or the amount of remaining storage on the instance is less than 5 GB.
        self.high_space_usage_protection = high_space_usage_protection
        # The number of hours for which log backup files are retained on the instance.
        self.local_log_retention_hours = local_log_retention_hours
        # The maximum storage usage that is allowed for log backup files on the instance.
        self.local_log_retention_space = local_log_retention_space
        # The number of binary log files on the instance.
        self.log_backup_local_retention_number = log_backup_local_retention_number
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compress_type is not None:
            result['CompressType'] = self.compress_type

        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.high_space_usage_protection is not None:
            result['HighSpaceUsageProtection'] = self.high_space_usage_protection

        if self.local_log_retention_hours is not None:
            result['LocalLogRetentionHours'] = self.local_log_retention_hours

        if self.local_log_retention_space is not None:
            result['LocalLogRetentionSpace'] = self.local_log_retention_space

        if self.log_backup_local_retention_number is not None:
            result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressType') is not None:
            self.compress_type = m.get('CompressType')

        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('HighSpaceUsageProtection') is not None:
            self.high_space_usage_protection = m.get('HighSpaceUsageProtection')

        if m.get('LocalLogRetentionHours') is not None:
            self.local_log_retention_hours = m.get('LocalLogRetentionHours')

        if m.get('LocalLogRetentionSpace') is not None:
            self.local_log_retention_space = m.get('LocalLogRetentionSpace')

        if m.get('LogBackupLocalRetentionNumber') is not None:
            self.log_backup_local_retention_number = m.get('LogBackupLocalRetentionNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

