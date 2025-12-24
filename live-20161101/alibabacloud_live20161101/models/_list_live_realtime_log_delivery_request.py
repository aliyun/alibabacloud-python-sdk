# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveRealtimeLogDeliveryRequest(DaraModel):
    def __init__(
        self,
        live_openapi_reserve: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # This parameter has no practical significance.
        self.live_openapi_reserve = live_openapi_reserve
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_openapi_reserve is not None:
            result['LiveOpenapiReserve'] = self.live_openapi_reserve

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveOpenapiReserve') is not None:
            self.live_openapi_reserve = m.get('LiveOpenapiReserve')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

