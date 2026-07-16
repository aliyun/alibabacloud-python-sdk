# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightReShopListSearchShrinkRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        out_wheel_search: bool = None,
        passenger_journey_group_key: str = None,
        re_shop_reason_code: str = None,
        search_journeys_shrink: str = None,
        selected_passengers_shrink: str = None,
        token: str = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_wheel_search = out_wheel_search
        # This parameter is required.
        self.passenger_journey_group_key = passenger_journey_group_key
        self.re_shop_reason_code = re_shop_reason_code
        # This parameter is required.
        self.search_journeys_shrink = search_journeys_shrink
        # This parameter is required.
        self.selected_passengers_shrink = selected_passengers_shrink
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_wheel_search is not None:
            result['out_wheel_search'] = self.out_wheel_search

        if self.passenger_journey_group_key is not None:
            result['passenger_journey_group_key'] = self.passenger_journey_group_key

        if self.re_shop_reason_code is not None:
            result['re_shop_reason_code'] = self.re_shop_reason_code

        if self.search_journeys_shrink is not None:
            result['search_journeys'] = self.search_journeys_shrink

        if self.selected_passengers_shrink is not None:
            result['selected_passengers'] = self.selected_passengers_shrink

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_wheel_search') is not None:
            self.out_wheel_search = m.get('out_wheel_search')

        if m.get('passenger_journey_group_key') is not None:
            self.passenger_journey_group_key = m.get('passenger_journey_group_key')

        if m.get('re_shop_reason_code') is not None:
            self.re_shop_reason_code = m.get('re_shop_reason_code')

        if m.get('search_journeys') is not None:
            self.search_journeys_shrink = m.get('search_journeys')

        if m.get('selected_passengers') is not None:
            self.selected_passengers_shrink = m.get('selected_passengers')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

