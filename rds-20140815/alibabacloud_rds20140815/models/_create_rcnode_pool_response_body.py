# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateRCNodePoolResponseBody(DaraModel):
    def __init__(
        self,
        instance_id_sets: List[str] = None,
        node_pool_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The instance IDs.
        self.instance_id_sets = instance_id_sets
        # The node pool ID.
        self.node_pool_id = node_pool_id
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
        if self.instance_id_sets is not None:
            result['InstanceIdSets'] = self.instance_id_sets

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdSets') is not None:
            self.instance_id_sets = m.get('InstanceIdSets')

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

