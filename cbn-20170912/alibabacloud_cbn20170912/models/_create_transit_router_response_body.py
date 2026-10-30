# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTransitRouterResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transit_router_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The Enterprise Edition transit router instance ID, which is used to forward traffic and perform routing. After the instance is created, it is in the Creating state. You must wait until the instance enters the Active state before you can proceed to What to do next. You can invoke the ListTransitRouters operation to query the instance status.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

