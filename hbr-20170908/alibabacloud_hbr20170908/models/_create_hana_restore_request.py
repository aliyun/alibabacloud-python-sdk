# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHanaRestoreRequest(DaraModel):
    def __init__(
        self,
        backup_id: int = None,
        backup_prefix: str = None,
        check_access: bool = None,
        clear_log: bool = None,
        cluster_id: str = None,
        database_name: str = None,
        log_position: int = None,
        master_client_id: str = None,
        mode: str = None,
        recovery_point_in_time: int = None,
        sid_admin: str = None,
        source: str = None,
        source_cluster_id: str = None,
        system_copy: bool = None,
        use_catalog: bool = None,
        use_delta: bool = None,
        vault_id: str = None,
        volume_id: int = None,
    ):
        # The ID of the backup.
        self.backup_id = backup_id
        # The backup prefix.
        # 
        # This parameter is required.
        self.backup_prefix = backup_prefix
        # Specifies whether to validate the differential backup and log backup. Valid values: true and false. If you set the value to true, HBR checks whether the required differential backup and log backup are available before the restore job starts. If the differential backup or log backup is unavailable, HBR does not start the restore job.
        self.check_access = check_access
        # Specifies whether to delete all log entries from the log area after the log entries are restored. Valid values: true and false. If you set the value to false, all log entries are deleted from the log area after the log entries are restored.
        self.clear_log = clear_log
        # The ID of the SAP HANA instance that you want to restore.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the database that you want to restore.
        # 
        # This parameter is required.
        self.database_name = database_name
        # The log position to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position
        # The ID of the client where the primary node of the SAP HANA resides.
        self.master_client_id = master_client_id
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: restores the database to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: restores the database to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: restores the database to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: restores the database to a specified log position.
        # 
        # This parameter is required.
        self.mode = mode
        # The point in time to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_POINT_IN_TIME**. HBR restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time
        # The SID admin account that is created by SAP HANA.
        self.sid_admin = sid_admin
        # The name of the source system. This parameter specifies the name of the source database that you want to restore. You must set the parameter in the `<Source database name>@SID` format.
        self.source = source
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id
        # Specifies whether to restore the database to a different instance.
        self.system_copy = system_copy
        # Specifies whether to use a catalog backup to restore the database. This parameter is required only if you set the Mode parameter to **RECOVERY_TO_SPECIFIC_BACKUP**. If you turn off Use Catalog, you must specify the prefix of a backup file. Then, Cloud Backup finds the backup file based on the specified prefix and restores the backup file.
        self.use_catalog = use_catalog
        # Specifies whether to use a differential backup or an incremental backup to restore the database. Valid values: true and false. If you want to use a differential backup or an incremental backup to restore the database, set the value to true. If you set the value to false, HBR uses a log backup to restore the database.
        self.use_delta = use_delta
        # The ID of the backup vault.
        self.vault_id = vault_id
        # The ID of the volume that you want to restore. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix

        if self.check_access is not None:
            result['CheckAccess'] = self.check_access

        if self.clear_log is not None:
            result['ClearLog'] = self.clear_log

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.log_position is not None:
            result['LogPosition'] = self.log_position

        if self.master_client_id is not None:
            result['MasterClientId'] = self.master_client_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time

        if self.sid_admin is not None:
            result['SidAdmin'] = self.sid_admin

        if self.source is not None:
            result['Source'] = self.source

        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id

        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy

        if self.use_catalog is not None:
            result['UseCatalog'] = self.use_catalog

        if self.use_delta is not None:
            result['UseDelta'] = self.use_delta

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')

        if m.get('CheckAccess') is not None:
            self.check_access = m.get('CheckAccess')

        if m.get('ClearLog') is not None:
            self.clear_log = m.get('ClearLog')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')

        if m.get('MasterClientId') is not None:
            self.master_client_id = m.get('MasterClientId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')

        if m.get('SidAdmin') is not None:
            self.sid_admin = m.get('SidAdmin')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')

        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')

        if m.get('UseCatalog') is not None:
            self.use_catalog = m.get('UseCatalog')

        if m.get('UseDelta') is not None:
            self.use_delta = m.get('UseDelta')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')

        return self

