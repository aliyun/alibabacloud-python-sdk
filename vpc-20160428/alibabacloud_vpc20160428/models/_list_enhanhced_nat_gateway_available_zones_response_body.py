# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListEnhanhcedNatGatewayAvailableZonesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[main_models.ListEnhanhcedNatGatewayAvailableZonesResponseBodyZones] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.ListEnhanhcedNatGatewayAvailableZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListEnhanhcedNatGatewayAvailableZonesResponseBodyZones(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        # The name of the zone.
        self.local_name = local_name
        # The ID of the zone where the instance is deployed.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

