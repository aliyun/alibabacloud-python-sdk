# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeHanaRestoresResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        hana_restore: main_models.DescribeHanaRestoresResponseBodyHanaRestore = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The information about restore jobs.
        self.hana_restore = hana_restore
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hana_restore:
            self.hana_restore.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hana_restore is not None:
            result['HanaRestore'] = self.hana_restore.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HanaRestore') is not None:
            temp_model = main_models.DescribeHanaRestoresResponseBodyHanaRestore()
            self.hana_restore = temp_model.from_map(m.get('HanaRestore'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHanaRestoresResponseBodyHanaRestore(DaraModel):
    def __init__(
        self,
        hana_restores: List[main_models.DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores] = None,
    ):
        self.hana_restores = hana_restores

    def validate(self):
        if self.hana_restores:
            for v1 in self.hana_restores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HanaRestores'] = []
        if self.hana_restores is not None:
            for k1 in self.hana_restores:
                result['HanaRestores'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana_restores = []
        if m.get('HanaRestores') is not None:
            for k1 in m.get('HanaRestores'):
                temp_model = main_models.DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores()
                self.hana_restores.append(temp_model.from_map(k1))

        return self

class DescribeHanaRestoresResponseBodyHanaRestoreHanaRestores(DaraModel):
    def __init__(
        self,
        backup_id: int = None,
        backup_prefix: str = None,
        check_access: bool = None,
        clear_log: bool = None,
        cluster_id: str = None,
        current_phase: int = None,
        current_progress: int = None,
        database_name: str = None,
        database_restore_id: int = None,
        end_time: int = None,
        log_position: int = None,
        max_phase: int = None,
        max_progress: int = None,
        message: str = None,
        mode: str = None,
        phase: str = None,
        reached_time: int = None,
        recovery_point_in_time: int = None,
        restore_id: str = None,
        source: str = None,
        source_cluster_id: str = None,
        start_time: int = None,
        state: str = None,
        status: str = None,
        system_copy: bool = None,
        use_catalog: bool = None,
        use_delta: bool = None,
        vault_id: str = None,
        volume_id: int = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The backup prefix.
        self.backup_prefix = backup_prefix
        # Indicates whether the differential backup and log backup are validated. Valid values:
        # 
        # *   true: Cloud Backup checks whether the required differential backup and log backup are available before the restore job starts. If the differential backup or log backup is unavailable, Cloud Backup does not start the restore job.
        # *   false: Cloud Backup does not check whether the required differential backup and log backup are available before the restore job starts.
        self.check_access = check_access
        # Indicates whether all log entries are deleted from the log area after the log entries are restored. Valid values: true and false. If the return value is false, all log entries are deleted from the log area after the log entries are restored.
        self.clear_log = clear_log
        # The ID of the SAP HANA instance that is restored.
        self.cluster_id = cluster_id
        # The current recovery phase. This value is obtained from SAP HANA.
        self.current_phase = current_phase
        # The current progress. This value is obtained from SAP HANA.
        self.current_progress = current_progress
        # The database name.
        self.database_name = database_name
        # The ID of the database recovery.
        self.database_restore_id = database_restore_id
        # The time when the restore job ends. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The log position to which the database is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position
        # The maximum recovery phase. This value is obtained from SAP HANA.
        self.max_phase = max_phase
        # The maximum progress. This value is obtained from SAP HANA.
        self.max_progress = max_progress
        # The details of the recovery phase.
        self.message = message
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: The database is restored to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: The database is restored to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: The database is restored to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: The database is restored to a specified log position.
        self.mode = mode
        # The recovery phase.
        self.phase = phase
        # The point in time at which the database is restored.
        self.reached_time = reached_time
        # The point in time to which the database is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_POINT_IN_TIME**. Cloud Backup restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time
        # The ID of the restore job.
        self.restore_id = restore_id
        # The name of the source system. This parameter indicates the name of the source database that is restored. Format: `<Source database name>@SID`.
        self.source = source
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id
        # The time when the restore job starts. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The recovery status. This value is obtained from SAP HANA.
        self.state = state
        # The status of the restore job. Valid values:
        # 
        # *   **RUNNING**: The job is running.
        # *   **COMPLETE**: The job is completed.
        # *   **PARTIAL_COMPLETE**: The job is partially completed.
        # *   **FAILED**: The job failed.
        # *   **CANCELED**: The job is canceled.
        # *   **EXPIRED**: The job timed out.
        self.status = status
        # Indicates whether the database is restored to a different instance. Valid values:
        # 
        # *   true: The database is restored to a different instance.
        # *   false: The database is restored within the same instance.
        self.system_copy = system_copy
        # Indicates whether a catalog backup is used to restore the database. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_SPECIFIC_BACKUP**. If the return value is false, Cloud Backup finds the backup file based on the specified prefix and then restores the backup file.
        self.use_catalog = use_catalog
        # Indicates whether a differential backup or an incremental backup is used to restore the database. Valid values: true and false. If the return value is true, Cloud Backup uses a differential backup or an incremental backup to restore the database. If the return value is false, Cloud Backup uses a log backup to restore the database.
        self.use_delta = use_delta
        # The ID of the backup vault.
        self.vault_id = vault_id
        # The ID of the volume that is restored. This parameter is returned only if the value of the Mode parameter is **RECOVERY_TO_LOG_POSITION**.
        self.volume_id = volume_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupID'] = self.backup_id

        if self.backup_prefix is not None:
            result['BackupPrefix'] = self.backup_prefix

        if self.check_access is not None:
            result['CheckAccess'] = self.check_access

        if self.clear_log is not None:
            result['ClearLog'] = self.clear_log

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_phase is not None:
            result['CurrentPhase'] = self.current_phase

        if self.current_progress is not None:
            result['CurrentProgress'] = self.current_progress

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_restore_id is not None:
            result['DatabaseRestoreId'] = self.database_restore_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_position is not None:
            result['LogPosition'] = self.log_position

        if self.max_phase is not None:
            result['MaxPhase'] = self.max_phase

        if self.max_progress is not None:
            result['MaxProgress'] = self.max_progress

        if self.message is not None:
            result['Message'] = self.message

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.reached_time is not None:
            result['ReachedTime'] = self.reached_time

        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time

        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

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
        if m.get('BackupID') is not None:
            self.backup_id = m.get('BackupID')

        if m.get('BackupPrefix') is not None:
            self.backup_prefix = m.get('BackupPrefix')

        if m.get('CheckAccess') is not None:
            self.check_access = m.get('CheckAccess')

        if m.get('ClearLog') is not None:
            self.clear_log = m.get('ClearLog')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPhase') is not None:
            self.current_phase = m.get('CurrentPhase')

        if m.get('CurrentProgress') is not None:
            self.current_progress = m.get('CurrentProgress')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabaseRestoreId') is not None:
            self.database_restore_id = m.get('DatabaseRestoreId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')

        if m.get('MaxPhase') is not None:
            self.max_phase = m.get('MaxPhase')

        if m.get('MaxProgress') is not None:
            self.max_progress = m.get('MaxProgress')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('ReachedTime') is not None:
            self.reached_time = m.get('ReachedTime')

        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')

        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

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

