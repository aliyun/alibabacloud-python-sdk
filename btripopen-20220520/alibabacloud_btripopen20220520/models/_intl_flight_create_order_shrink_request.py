# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightCreateOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        async_create_order_key: str = None,
        async_create_order_mode: bool = None,
        btrip_user_id: str = None,
        buyer_name: str = None,
        contact_info_shrink: str = None,
        extra_info_shrink: str = None,
        isv_name: str = None,
        order_price: int = None,
        ota_item_id: str = None,
        out_order_id: str = None,
        passenger_list_shrink: str = None,
        render_key: str = None,
    ):
        self.async_create_order_key = async_create_order_key
        self.async_create_order_mode = async_create_order_mode
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.buyer_name = buyer_name
        # This parameter is required.
        self.contact_info_shrink = contact_info_shrink
        self.extra_info_shrink = extra_info_shrink
        self.isv_name = isv_name
        self.order_price = order_price
        # This parameter is required.
        self.ota_item_id = ota_item_id
        self.out_order_id = out_order_id
        # This parameter is required.
        self.passenger_list_shrink = passenger_list_shrink
        self.render_key = render_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_create_order_key is not None:
            result['async_create_order_key'] = self.async_create_order_key

        if self.async_create_order_mode is not None:
            result['async_create_order_mode'] = self.async_create_order_mode

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.contact_info_shrink is not None:
            result['contact_info'] = self.contact_info_shrink

        if self.extra_info_shrink is not None:
            result['extra_info'] = self.extra_info_shrink

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.passenger_list_shrink is not None:
            result['passenger_list'] = self.passenger_list_shrink

        if self.render_key is not None:
            result['render_key'] = self.render_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_create_order_key') is not None:
            self.async_create_order_key = m.get('async_create_order_key')

        if m.get('async_create_order_mode') is not None:
            self.async_create_order_mode = m.get('async_create_order_mode')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('contact_info') is not None:
            self.contact_info_shrink = m.get('contact_info')

        if m.get('extra_info') is not None:
            self.extra_info_shrink = m.get('extra_info')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('passenger_list') is not None:
            self.passenger_list_shrink = m.get('passenger_list')

        if m.get('render_key') is not None:
            self.render_key = m.get('render_key')

        return self

