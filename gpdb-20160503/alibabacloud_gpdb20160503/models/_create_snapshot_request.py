# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnapshotRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        lsn: str = None,
        project_id: str = None,
        region_id: str = None,
        snapshot_timestamp: str = None,
    ):
        # The idempotence token. Ensures that repeated requests do not result in duplicate operations.
        self.client_token = client_token
        # The LSN for the snapshot. You must specify either this parameter or SnapshotTimestamp. If this parameter is specified, the snapshot is created based on the specified LSN.
        self.lsn = lsn
        # The Supabase project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID. Specifies the region in which to perform the operation.
        self.region_id = region_id
        # The point in time for the snapshot. You must specify either this parameter or Lsn. If this parameter is specified, the snapshot is created based on the specified point in time.
        self.snapshot_timestamp = snapshot_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.lsn is not None:
            result['Lsn'] = self.lsn

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_timestamp is not None:
            result['SnapshotTimestamp'] = self.snapshot_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Lsn') is not None:
            self.lsn = m.get('Lsn')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotTimestamp') is not None:
            self.snapshot_timestamp = m.get('SnapshotTimestamp')

        return self

