# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStorageStrategyRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_retention_period: int = None,
        backup_storage_encrypt_method: str = None,
        client_token: str = None,
        duplication_archive_period: int = None,
        duplication_infrequent_access_period: int = None,
        increment_backup_retention_period: str = None,
        increment_duplication_archive_period: str = None,
        increment_duplication_infrequent_access_period: str = None,
        log_backup_retention_period: str = None,
        log_duplication_archive_period: str = None,
        log_duplication_infrequent_access_period: str = None,
        owner_id: str = None,
    ):
        # Backup plan ID. Obtain this parameter\\"s value by calling the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # Backup data retention period, in days. Valid values: 0 to 1825.
        # 
        # > Default value: 730 days.
        # 
        # This parameter is required.
        self.backup_retention_period = backup_retention_period
        self.backup_storage_encrypt_method = backup_storage_encrypt_method
        # An arbitrary string used to ensure the idempotence of the request and prevent duplicate submissions.
        self.client_token = client_token
        # Time to convert to Archive Storage. This value must be less than the backup data retention period (BackupRetentionPeriod parameter). For more information about Archive Storage, see [Storage Type Overview](https://help.aliyun.com/document_detail/51374.html).
        # 
        # > Default value: 365 days.
        # 
        # This parameter is required.
        self.duplication_archive_period = duplication_archive_period
        # Time to convert to Infrequent Access storage. This value must be less than the Archive Storage period (DuplicationArchivePeriod parameter). For more information about Infrequent Access storage, see [Storage Type Overview](https://help.aliyun.com/document_detail/51374.html).
        # 
        # > Default value: 180 days.
        # 
        # This parameter is required.
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        self.increment_backup_retention_period = increment_backup_retention_period
        self.increment_duplication_archive_period = increment_duplication_archive_period
        self.increment_duplication_infrequent_access_period = increment_duplication_infrequent_access_period
        self.log_backup_retention_period = log_backup_retention_period
        self.log_duplication_archive_period = log_duplication_archive_period
        self.log_duplication_infrequent_access_period = log_duplication_infrequent_access_period
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.backup_storage_encrypt_method is not None:
            result['BackupStorageEncryptMethod'] = self.backup_storage_encrypt_method

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period

        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period

        if self.increment_backup_retention_period is not None:
            result['IncrementBackupRetentionPeriod'] = self.increment_backup_retention_period

        if self.increment_duplication_archive_period is not None:
            result['IncrementDuplicationArchivePeriod'] = self.increment_duplication_archive_period

        if self.increment_duplication_infrequent_access_period is not None:
            result['IncrementDuplicationInfrequentAccessPeriod'] = self.increment_duplication_infrequent_access_period

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.log_duplication_archive_period is not None:
            result['LogDuplicationArchivePeriod'] = self.log_duplication_archive_period

        if self.log_duplication_infrequent_access_period is not None:
            result['LogDuplicationInfrequentAccessPeriod'] = self.log_duplication_infrequent_access_period

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('BackupStorageEncryptMethod') is not None:
            self.backup_storage_encrypt_method = m.get('BackupStorageEncryptMethod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')

        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')

        if m.get('IncrementBackupRetentionPeriod') is not None:
            self.increment_backup_retention_period = m.get('IncrementBackupRetentionPeriod')

        if m.get('IncrementDuplicationArchivePeriod') is not None:
            self.increment_duplication_archive_period = m.get('IncrementDuplicationArchivePeriod')

        if m.get('IncrementDuplicationInfrequentAccessPeriod') is not None:
            self.increment_duplication_infrequent_access_period = m.get('IncrementDuplicationInfrequentAccessPeriod')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('LogDuplicationArchivePeriod') is not None:
            self.log_duplication_archive_period = m.get('LogDuplicationArchivePeriod')

        if m.get('LogDuplicationInfrequentAccessPeriod') is not None:
            self.log_duplication_infrequent_access_period = m.get('LogDuplicationInfrequentAccessPeriod')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

