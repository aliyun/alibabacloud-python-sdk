# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTransitRouterAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: List[str] = None,
        master_zones: List[str] = None,
        request_id: str = None,
        slave_zones: List[str] = None,
        support_multicast: bool = None,
    ):
        # A list of zone IDs.
        self.available_zones = available_zones
        # A list of primary zones.
        self.master_zones = master_zones
        # The request ID.
        self.request_id = request_id
        # A list of secondary zone IDs.
        self.slave_zones = slave_zones
        # Indicates whether the zone supports the multicast feature.
        self.support_multicast = support_multicast

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones

        if self.master_zones is not None:
            result['MasterZones'] = self.master_zones

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slave_zones is not None:
            result['SlaveZones'] = self.slave_zones

        if self.support_multicast is not None:
            result['SupportMulticast'] = self.support_multicast

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')

        if m.get('MasterZones') is not None:
            self.master_zones = m.get('MasterZones')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlaveZones') is not None:
            self.slave_zones = m.get('SlaveZones')

        if m.get('SupportMulticast') is not None:
            self.support_multicast = m.get('SupportMulticast')

        return self

