# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightInventoryPriceCheckShrinkRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        buyer_name: str = None,
        isv_name: str = None,
        order_price: int = None,
        ota_item_id: str = None,
        passenger_list_shrink: str = None,
    ):
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        self.isv_name = isv_name
        self.order_price = order_price
        # This parameter is required.
        self.ota_item_id = ota_item_id
        # This parameter is required.
        self.passenger_list_shrink = passenger_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.passenger_list_shrink is not None:
            result['passenger_list'] = self.passenger_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('passenger_list') is not None:
            self.passenger_list_shrink = m.get('passenger_list')

        return self

