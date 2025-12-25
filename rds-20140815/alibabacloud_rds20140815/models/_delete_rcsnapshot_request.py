# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRCSnapshotRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        # Specifies whether to forcefully delete the snapshot that is used to create cloud disks. Valid values:
        # 
        # *   **true**: forcefully deletes the snapshot After the snapshot is forcefully deleted, the cloud disks created from the snapshot cannot be re-initialized.
        # *   **false**(default): does not forcefully delete the snapshot.
        self.force = force
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

