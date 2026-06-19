# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRouterInterfaceResponseBody(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
        router_interface_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.router_interface_id = router_interface_id

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

        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')

        return self

