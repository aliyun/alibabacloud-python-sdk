# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRestoreJobRequest(DaraModel):
    def __init__(
        self,
        includes: str = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        snapshot_version: str = None,
        source_type: str = None,
        target: str = None,
        uuid: str = None,
        vault_id: str = None,
    ):
        # The directory in which the files included in the restoration task are located. This parameter is specified when you create the anti-ransomware policy. The value is a directory that requires protection.
        # 
        # This parameter is required.
        self.includes = includes
        # The hash value of the snapshot.
        # 
        # > You can call the [DescribeSnapshots](~~DescribeSnapshots~~) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.snapshot_hash = snapshot_hash
        # The ID of the snapshot that you want to use for restoration.
        # 
        # > You can call the [DescribeSnapshots](~~DescribeSnapshots~~) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # The version of the backup data.
        # 
        # > You can call the [DescribeSnapshots](~~DescribeSnapshots~~) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.snapshot_version = snapshot_version
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **File**: backup snapshots for on-premises servers
        self.source_type = source_type
        # The path to which you want to restore data.
        # 
        # This parameter is required.
        self.target = target
        # The UUID of the server whose data you want to restore.
        # 
        # This parameter is required.
        self.uuid = uuid
        # The ID of the backup vault that is used in the restoration task.
        # 
        # > You can call the [DescribeSnapshots](~~DescribeSnapshots~~) operation to obtain the value of this parameter.
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
        if self.includes is not None:
            result['Includes'] = self.includes

        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_version is not None:
            result['SnapshotVersion'] = self.snapshot_version

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.target is not None:
            result['Target'] = self.target

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Includes') is not None:
            self.includes = m.get('Includes')

        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotVersion') is not None:
            self.snapshot_version = m.get('SnapshotVersion')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

