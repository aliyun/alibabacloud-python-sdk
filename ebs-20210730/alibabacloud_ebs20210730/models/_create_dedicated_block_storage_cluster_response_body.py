# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDedicatedBlockStorageClusterResponseBody(DaraModel):
    def __init__(
        self,
        dbsc_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the dedicated block storage cluster.
        self.dbsc_id = dbsc_id
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

