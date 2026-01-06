# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHanaBackupSettingRequest(DaraModel):
    def __init__(
        self,
        catalog_backup_parameter_file: str = None,
        catalog_backup_using_backint: bool = None,
        cluster_id: str = None,
        data_backup_parameter_file: str = None,
        database_name: str = None,
        enable_auto_log_backup: bool = None,
        log_backup_parameter_file: str = None,
        log_backup_timeout: int = None,
        log_backup_using_backint: bool = None,
        vault_id: str = None,
    ):
        # The configuration file for catalog backup.
        self.catalog_backup_parameter_file = catalog_backup_parameter_file
        # Specifies whether to use Backint to back up catalogs. Valid values:
        # 
        # *   true: Backint is used to back up catalogs.
        # *   false: Backint is not used to back up catalogs.
        # 
        # This parameter is required.
        self.catalog_backup_using_backint = catalog_backup_using_backint
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The configuration file for data backup.
        self.data_backup_parameter_file = data_backup_parameter_file
        # The name of the database.
        # 
        # This parameter is required.
        self.database_name = database_name
        # Specifies whether to enable automatic log backup. Valid values:
        # 
        # *   **true**: enables automatic log backup.
        # *   **false**: disables automatic log backup.
        # 
        # This parameter is required.
        self.enable_auto_log_backup = enable_auto_log_backup
        # The configuration file for log backup.
        self.log_backup_parameter_file = log_backup_parameter_file
        # The interval at which logs are backed up. Unit: seconds.
        self.log_backup_timeout = log_backup_timeout
        # Specifies whether to use Backint to back up logs. Valid values:
        # 
        # *   true: Backint is used to back up logs.
        # *   false: Backint is not used to back up logs.
        # 
        # This parameter is required.
        self.log_backup_using_backint = log_backup_using_backint
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_backup_parameter_file is not None:
            result['CatalogBackupParameterFile'] = self.catalog_backup_parameter_file

        if self.catalog_backup_using_backint is not None:
            result['CatalogBackupUsingBackint'] = self.catalog_backup_using_backint

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_backup_parameter_file is not None:
            result['DataBackupParameterFile'] = self.data_backup_parameter_file

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.enable_auto_log_backup is not None:
            result['EnableAutoLogBackup'] = self.enable_auto_log_backup

        if self.log_backup_parameter_file is not None:
            result['LogBackupParameterFile'] = self.log_backup_parameter_file

        if self.log_backup_timeout is not None:
            result['LogBackupTimeout'] = self.log_backup_timeout

        if self.log_backup_using_backint is not None:
            result['LogBackupUsingBackint'] = self.log_backup_using_backint

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogBackupParameterFile') is not None:
            self.catalog_backup_parameter_file = m.get('CatalogBackupParameterFile')

        if m.get('CatalogBackupUsingBackint') is not None:
            self.catalog_backup_using_backint = m.get('CatalogBackupUsingBackint')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataBackupParameterFile') is not None:
            self.data_backup_parameter_file = m.get('DataBackupParameterFile')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EnableAutoLogBackup') is not None:
            self.enable_auto_log_backup = m.get('EnableAutoLogBackup')

        if m.get('LogBackupParameterFile') is not None:
            self.log_backup_parameter_file = m.get('LogBackupParameterFile')

        if m.get('LogBackupTimeout') is not None:
            self.log_backup_timeout = m.get('LogBackupTimeout')

        if m.get('LogBackupUsingBackint') is not None:
            self.log_backup_using_backint = m.get('LogBackupUsingBackint')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

