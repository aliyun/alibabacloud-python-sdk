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
        # Specifies whether to enable the cross-region backup feature on the instance. This parameter specifies whether you can back up data and logs. Valid values:
        # 
        # *   **0**: disables the feature.
        # *   **1:** enables the feature.
        # 
        # > Before you enable the cross-region backup feature, you must configure the CrossBackupRegion parameter.
        self.backup_enabled = backup_enabled
        # The ID of the region in which the cross-region backup files of the instance are stored.
        self.cross_backup_region = cross_backup_region
        # The policy that is used to save the cross-region backup files of the instance. Set the value to **1**. The value 1 specifies that all cross-region backup files are saved.
        self.cross_backup_type = cross_backup_type
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable the cross-region log backup feature on the instance. Valid values:
        # 
        # *   **0**: disables the feature.
        # *   **1:** enables the feature.
        # 
        # > You can enable the cross-region log backup feature only when the cross-region backup feature is enabled.
        self.log_backup_enabled = log_backup_enabled
        self.owner_id = owner_id
        # The region ID of the source instance. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The policy that is used to retain the cross-region backup files of the instance. Set the value to 1. The value **1** specifies that the cross-region backup files of the instance are retained based on the specified retention period.
        self.retent_type = retent_type
        # The number of days for which the cross-region backup files of the instance are retained. Valid values: **7 to 1825**.
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

