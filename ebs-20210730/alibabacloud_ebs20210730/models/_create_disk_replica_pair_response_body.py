# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiskReplicaPairResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        replica_pair_id: str = None,
        request_id: str = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

