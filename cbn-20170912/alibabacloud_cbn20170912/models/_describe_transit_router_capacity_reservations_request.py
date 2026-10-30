# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTransitRouterCapacityReservationsRequest(DaraModel):
    def __init__(
        self,
        transit_router_id: str = None,
        version: str = None,
    ):
        # The ID of the Enterprise Edition transit router instance.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

