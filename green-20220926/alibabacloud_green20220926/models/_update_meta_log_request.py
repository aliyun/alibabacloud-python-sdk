# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetaLogRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        delivery_region: str = None,
        storage: int = None,
        ttl: int = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # The delivery region.
        self.delivery_region = delivery_region
        # The storage capacity.
        self.storage = storage
        # The time to live.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.delivery_region is not None:
            result['DeliveryRegion'] = self.delivery_region

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DeliveryRegion') is not None:
            self.delivery_region = m.get('DeliveryRegion')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

