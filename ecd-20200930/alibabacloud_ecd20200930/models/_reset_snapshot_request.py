# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetSnapshotRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        snapshot_id: str = None,
        stop_desktop: bool = None,
    ):
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the snapshot.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        self.stop_desktop = stop_desktop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.stop_desktop is not None:
            result['StopDesktop'] = self.stop_desktop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('StopDesktop') is not None:
            self.stop_desktop = m.get('StopDesktop')

        return self

