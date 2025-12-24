# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSnapshotsUsageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_count: int = None,
        snapshot_size: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The number of snapshots stored in the current region.
        self.snapshot_count = snapshot_count
        # The total size of snapshots stored in the current region. Unit: bytes.
        self.snapshot_size = snapshot_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count

        if self.snapshot_size is not None:
            result['SnapshotSize'] = self.snapshot_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')

        if m.get('SnapshotSize') is not None:
            self.snapshot_size = m.get('SnapshotSize')

        return self

