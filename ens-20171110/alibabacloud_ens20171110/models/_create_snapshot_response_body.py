# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        snap_shot_id: List[str] = None,
    ):
        # The ID of the order.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The IDs of the snapshots.
        self.snap_shot_id = snap_shot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snap_shot_id is not None:
            result['SnapShotId'] = self.snap_shot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapShotId') is not None:
            self.snap_shot_id = m.get('SnapShotId')

        return self

