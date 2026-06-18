# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        lsn: str = None,
        request_id: str = None,
        timestamp: str = None,
    ):
        # The branch ID to which the snapshot belongs.
        self.branch_id = branch_id
        # The LSN for the snapshot. You must specify either this parameter or SnapshotTimestamp. If this parameter is specified, the snapshot is created based on the specified LSN.
        self.lsn = lsn
        # The request ID.
        self.request_id = request_id
        # The actual point in time that corresponds to the created snapshot.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.lsn is not None:
            result['Lsn'] = self.lsn

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('Lsn') is not None:
            self.lsn = m.get('Lsn')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

