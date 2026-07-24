# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CollectFlightLowestPriceShrinkRequest(DaraModel):
    def __init__(
        self,
        lowest_price_flight_info_list_shrink: str = None,
    ):
        # The lowest-price flight information.
        # 
        # This parameter is required.
        self.lowest_price_flight_info_list_shrink = lowest_price_flight_info_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lowest_price_flight_info_list_shrink is not None:
            result['lowest_price_flight_info_list'] = self.lowest_price_flight_info_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lowest_price_flight_info_list') is not None:
            self.lowest_price_flight_info_list_shrink = m.get('lowest_price_flight_info_list')

        return self

