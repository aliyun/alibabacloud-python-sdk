# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerResponseBody(DaraModel):
    def __init__(
        self,
        loadbalancer_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the NLB instance.
        self.loadbalancer_id = loadbalancer_id
        # The ID of the order for the NLB instance.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loadbalancer_id is not None:
            result['LoadbalancerId'] = self.loadbalancer_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadbalancerId') is not None:
            self.loadbalancer_id = m.get('LoadbalancerId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

