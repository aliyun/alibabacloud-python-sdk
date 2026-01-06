# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHanaBackupsAsyncRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        include_differential: bool = None,
        include_incremental: bool = None,
        include_log: bool = None,
        log_position: int = None,
        mode: str = None,
        page_number: int = None,
        page_size: int = None,
        recovery_point_in_time: int = None,
        resource_group_id: str = None,
        source: str = None,
        source_cluster_id: str = None,
        system_copy: bool = None,
        use_backint: bool = None,
        vault_id: str = None,
        volume_id: int = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # Specifies whether to include differential backups in the query results. Valid values:
        # 
        # *   true: includes differential backups.
        # *   false: excludes differential backups.
        self.include_differential = include_differential
        # Specifies whether to include incremental backups in the query results. Valid values:
        # 
        # *   true: includes incremental backups.
        # *   false: excludes incremental backups.
        self.include_incremental = include_incremental
        # Specifies whether to include log backups in the query results. Valid values:
        # 
        # *   true: includes log backups.
        # *   false: excludes log backups.
        self.include_log = include_log
        # The log position to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_LOG_POSITION**.
        self.log_position = log_position
        # The recovery mode. Valid values:
        # 
        # *   **RECOVERY_TO_MOST_RECENT**: restores the database to the recently available state to which the database has been backed up.
        # *   **RECOVERY_TO_POINT_IN_TIME**: restores the database to a specified point in time.
        # *   **RECOVERY_TO_SPECIFIC_BACKUP**: restores the database to a specified backup.
        # *   **RECOVERY_TO_LOG_POSITION**: restores the database to a specified log position.
        self.mode = mode
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The point in time to which you want to restore the database. This parameter is valid only if you set the Mode parameter to **RECOVERY_TO_POINT_IN_TIME**. Cloud Backup restores the database to a state closest to the specified point in time.
        self.recovery_point_in_time = recovery_point_in_time
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the source system. This parameter specifies the name of the source database that you want to restore. You must set the parameter in the `<Source database name>@SID` format.
        self.source = source
        # The ID of the source SAP HANA instance.
        self.source_cluster_id = source_cluster_id
        # Specifies whether to restore the database to a different instance.
        # 
        # *   true: restores the database to a different instance.
        # *   false: restores the database within the same instance.
        self.system_copy = system_copy
        # Specifies whether Backint is used. Valid values:
        # 
        # *   true: Backint is used.
        # *   false: Backint is not used.
        self.use_backint = use_backint
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.include_differential is not None:
            result['IncludeDifferential'] = self.include_differential

        if self.include_incremental is not None:
            result['IncludeIncremental'] = self.include_incremental

        if self.include_log is not None:
            result['IncludeLog'] = self.include_log

        if self.log_position is not None:
            result['LogPosition'] = self.log_position

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.recovery_point_in_time is not None:
            result['RecoveryPointInTime'] = self.recovery_point_in_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_cluster_id is not None:
            result['SourceClusterId'] = self.source_cluster_id

        if self.system_copy is not None:
            result['SystemCopy'] = self.system_copy

        if self.use_backint is not None:
            result['UseBackint'] = self.use_backint

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('IncludeDifferential') is not None:
            self.include_differential = m.get('IncludeDifferential')

        if m.get('IncludeIncremental') is not None:
            self.include_incremental = m.get('IncludeIncremental')

        if m.get('IncludeLog') is not None:
            self.include_log = m.get('IncludeLog')

        if m.get('LogPosition') is not None:
            self.log_position = m.get('LogPosition')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecoveryPointInTime') is not None:
            self.recovery_point_in_time = m.get('RecoveryPointInTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceClusterId') is not None:
            self.source_cluster_id = m.get('SourceClusterId')

        if m.get('SystemCopy') is not None:
            self.system_copy = m.get('SystemCopy')

        if m.get('UseBackint') is not None:
            self.use_backint = m.get('UseBackint')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')

        return self

