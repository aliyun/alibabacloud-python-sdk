# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiskReplicaPairProgressResponseBody(DaraModel):
    def __init__(
        self,
        progress: int = None,
        recover_point: int = None,
        request_id: str = None,
    ):
        # The replication progress of the replication pair.
        self.progress = progress
        # The timestamp that indicates the last recovery point in time. The value is returned only after the replication pair works for replicating data.
        self.recover_point = recover_point
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.progress is not None:
            result['Progress'] = self.progress

        if self.recover_point is not None:
            result['RecoverPoint'] = self.recover_point

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RecoverPoint') is not None:
            self.recover_point = m.get('RecoverPoint')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

