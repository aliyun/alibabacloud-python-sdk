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
        # The Enterprise Edition transit router instance ID. After creation, the instance is in the Creating state. Wait until the instance status changes to Active before performing subsequent operations. You can call the [ListTransitRouters](https://help.aliyun.com/document_detail/261219.html) operation to query the Enterprise Edition transit router instance status.
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

