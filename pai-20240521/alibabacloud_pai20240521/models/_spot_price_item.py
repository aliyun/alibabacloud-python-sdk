# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SpotPriceItem(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_discount: float = None,
        timestamp: str = None,
        zone_id: str = None,
    ):
        self.instance_type = instance_type
        self.spot_discount = spot_discount
        self.timestamp = timestamp
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.spot_discount is not None:
            result['SpotDiscount'] = self.spot_discount

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotDiscount') is not None:
            self.spot_discount = m.get('SpotDiscount')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

