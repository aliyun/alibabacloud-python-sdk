# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVpdRouteEntryRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vpd_id: str = None,
        vpd_route_entry_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Lingjun CIDR block instance ID
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # The ID of the route entry instance.
        # 
        # This parameter is required.
        self.vpd_route_entry_id = vpd_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_route_entry_id is not None:
            result['VpdRouteEntryId'] = self.vpd_route_entry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdRouteEntryId') is not None:
            self.vpd_route_entry_id = m.get('VpdRouteEntryId')

        return self

