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
        enable_increment_data_backup: bool = None,
        enable_pitr_protection: bool = None,
        high_space_usage_protection: str = None,
        inc_backup_interval: int = None,
        local_log_retention_hours: int = None,
        local_log_retention_space: str = None,
        log_backup_local_retention_number: int = None,
        request_id: str = None,
    ):
        # The backup compression method. Valid values:
        # * **0**: no compression.
        # * **1**: zlib compression.
        # * **2**: parallel zlib compression.
        # * **4**: quicklz compression. Database and table restoration is enabled.
        # * **8**: quicklz compression for MySQL 8.0. Database and table restoration is not supported.
        self.compress_type = compress_type
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # Indicates whether instance log backup is enabled. Valid values:
        # * **1**: enabled.
        # * **0**: shutdown.
        # 
        # 
        # > Instance log backup is enabled by default and cannot be shut down for ApsaraDB RDS for SQL Server instances.
        self.enable_backup_log = enable_backup_log
        # Indicates whether incremental backup is enabled.
        self.enable_increment_data_backup = enable_increment_data_backup
        # Indicates whether point-in-time recovery (PITR) is enabled for the ApsaraDB RDS for MySQL instance.
        self.enable_pitr_protection = enable_pitr_protection
        # Indicates whether binary log files are unconditionally deleted when the storage usage of the **ApsaraDB RDS for MySQL** instance exceeds 80% or the remaining storage space is less than 5 GB.
        self.high_space_usage_protection = high_space_usage_protection
        # The high-frequency incremental backup interval. Unit: minutes. Valid values: 60, 120, 240, 360, and 720.
        self.inc_backup_interval = inc_backup_interval
        # The number of hours for which instance log backups are retained locally on the **MySQL** instance.
        self.local_log_retention_hours = local_log_retention_hours
        # The maximum loop space usage of the local binary log on the **MySQL** instance.
        self.local_log_retention_space = local_log_retention_space
        # The number of binary log files retained locally on the **ApsaraDB RDS for MySQL** instance.
        self.log_backup_local_retention_number = log_backup_local_retention_number
        # The request ID.
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

        if self.enable_increment_data_backup is not None:
            result['EnableIncrementDataBackup'] = self.enable_increment_data_backup

        if self.enable_pitr_protection is not None:
            result['EnablePitrProtection'] = self.enable_pitr_protection

        if self.high_space_usage_protection is not None:
            result['HighSpaceUsageProtection'] = self.high_space_usage_protection

        if self.inc_backup_interval is not None:
            result['IncBackupInterval'] = self.inc_backup_interval

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

        if m.get('EnableIncrementDataBackup') is not None:
            self.enable_increment_data_backup = m.get('EnableIncrementDataBackup')

        if m.get('EnablePitrProtection') is not None:
            self.enable_pitr_protection = m.get('EnablePitrProtection')

        if m.get('HighSpaceUsageProtection') is not None:
            self.high_space_usage_protection = m.get('HighSpaceUsageProtection')

        if m.get('IncBackupInterval') is not None:
            self.inc_backup_interval = m.get('IncBackupInterval')

        if m.get('LocalLogRetentionHours') is not None:
            self.local_log_retention_hours = m.get('LocalLogRetentionHours')

        if m.get('LocalLogRetentionSpace') is not None:
            self.local_log_retention_space = m.get('LocalLogRetentionSpace')

        if m.get('LogBackupLocalRetentionNumber') is not None:
            self.log_backup_local_retention_number = m.get('LogBackupLocalRetentionNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

