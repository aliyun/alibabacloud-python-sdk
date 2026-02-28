# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetErRouteEntryRequest(DaraModel):
    def __init__(
        self,
        er_id: str = None,
        er_route_entry_id: str = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the route entry.
        # 
        # This parameter is required.
        self.er_route_entry_id = er_route_entry_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_route_entry_id is not None:
            result['ErRouteEntryId'] = self.er_route_entry_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErRouteEntryId') is not None:
            self.er_route_entry_id = m.get('ErRouteEntryId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

