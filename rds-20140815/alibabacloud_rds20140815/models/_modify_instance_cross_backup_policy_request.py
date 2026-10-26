# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceCrossBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        backup_enabled: str = None,
        cross_backup_region: str = None,
        cross_backup_type: str = None,
        dbinstance_id: str = None,
        log_backup_enabled: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retent_type: int = None,
        retention: int = None,
    ):
        # Specifies whether to enable the overall cross-region backup feature, which includes data backup and log backup. Valid values:
        # * **0**: disabled
        # * **1**: enabled
        # 
        # > When you enable cross-region backup, you must specify the destination region ID.
        self.backup_enabled = backup_enabled
        # The ID of the destination region for cross-region backup.
        self.cross_backup_region = cross_backup_region
        # The retention type of cross-region backups. Only **1** is supported, which indicates that all backups are retained.
        self.cross_backup_type = cross_backup_type
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable cross-region log backup. Valid values:
        # * **0**: disabled
        # * **1**: enabled
        # 
        # > You can configure this parameter only when the overall cross-region backup feature is enabled.
        self.log_backup_enabled = log_backup_enabled
        self.owner_id = owner_id
        # The region ID of the source instance. You can call the DescribeRegions operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention method for cross-region backups. Only **1** is supported, which indicates that backups are retained based on a specified retention period.
        self.retent_type = retent_type
        # The retention period of cross-region backups. Valid values: **7 to 1825**. Unit: days.
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

        if self.cross_backup_region is not None:
            result['CrossBackupRegion'] = self.cross_backup_region

        if self.cross_backup_type is not None:
            result['CrossBackupType'] = self.cross_backup_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.log_backup_enabled is not None:
            result['LogBackupEnabled'] = self.log_backup_enabled

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retent_type is not None:
            result['RetentType'] = self.retent_type

        if self.retention is not None:
            result['Retention'] = self.retention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEnabled') is not None:
            self.backup_enabled = m.get('BackupEnabled')

        if m.get('CrossBackupRegion') is not None:
            self.cross_backup_region = m.get('CrossBackupRegion')

        if m.get('CrossBackupType') is not None:
            self.cross_backup_type = m.get('CrossBackupType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('LogBackupEnabled') is not None:
            self.log_backup_enabled = m.get('LogBackupEnabled')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetentType') is not None:
            self.retent_type = m.get('RetentType')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        return self

