# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DeleteBackupSnapshotRequest(DaraModel):
    def __init__(
        self,
        backup_region_id_list: List[str] = None,
        backup_snapshot_list: List[main_models.DeleteBackupSnapshotRequestBackupSnapshotList] = None,
        retain_latest_snapshot: bool = None,
    ):
        # The regions for backup.
        self.backup_region_id_list = backup_region_id_list
        # The backup snapshots.
        self.backup_snapshot_list = backup_snapshot_list
        # Specifies whether to retain the latest snapshot. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.retain_latest_snapshot = retain_latest_snapshot

    def validate(self):
        if self.backup_snapshot_list:
            for v1 in self.backup_snapshot_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_region_id_list is not None:
            result['BackupRegionIdList'] = self.backup_region_id_list

        result['BackupSnapshotList'] = []
        if self.backup_snapshot_list is not None:
            for k1 in self.backup_snapshot_list:
                result['BackupSnapshotList'].append(k1.to_map() if k1 else None)

        if self.retain_latest_snapshot is not None:
            result['RetainLatestSnapshot'] = self.retain_latest_snapshot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRegionIdList') is not None:
            self.backup_region_id_list = m.get('BackupRegionIdList')

        self.backup_snapshot_list = []
        if m.get('BackupSnapshotList') is not None:
            for k1 in m.get('BackupSnapshotList'):
                temp_model = main_models.DeleteBackupSnapshotRequestBackupSnapshotList()
                self.backup_snapshot_list.append(temp_model.from_map(k1))

        if m.get('RetainLatestSnapshot') is not None:
            self.retain_latest_snapshot = m.get('RetainLatestSnapshot')

        return self

class DeleteBackupSnapshotRequestBackupSnapshotList(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        # The ID of the Cloud Backup client.
        # 
        # >  You can call the [DescribeSnapshots](~~DescribeSnapshots~~) operation to query the ID.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region in which Security Center is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: China (Hangzhou).
        # *   **ap-southeast-1**: Singapore.
        # *   **cn-beijing**: China (Beijing).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the snapshot that you want to delete.
        # 
        # >  You can call the [DescribeSnapshots](~~DescribeSnapshots~~) operation to query the ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files.
        # *   **OSS**: Object Storage Service (OSS) buckets.
        # *   **NAS**: File Storage NAS (NAS) file systems.
        # *   **OTS_TABLE**: Tablestore instances.
        # 
        # This parameter is required.
        self.source_type = source_type
        # The ID of the backup vault that is used in the restoration task.
        # 
        # >  You can call the [DescribeSnapshots](~~DescribeSnapshots~~) operation to query the ID.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

