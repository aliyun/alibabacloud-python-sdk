# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteErRouteMapRequest(DaraModel):
    def __init__(
        self,
        er_id: str = None,
        er_route_map_id: str = None,
        er_route_map_ids: List[str] = None,
        region_id: str = None,
    ):
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # routing policy ID
        self.er_route_map_id = er_route_map_id
        # routing policy Instance ID List
        self.er_route_map_ids = er_route_map_ids
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

        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id

        if self.er_route_map_ids is not None:
            result['ErRouteMapIds'] = self.er_route_map_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')

        if m.get('ErRouteMapIds') is not None:
            self.er_route_map_ids = m.get('ErRouteMapIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

