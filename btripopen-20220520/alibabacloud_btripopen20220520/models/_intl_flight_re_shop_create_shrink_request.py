# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightReShopCreateShrinkRequest(DaraModel):
    def __init__(
        self,
        async_apply_key: str = None,
        async_apply_mode: bool = None,
        order_id: str = None,
        ota_item_id: str = None,
        out_order_id: str = None,
        out_re_shop_apply_id: str = None,
        passenger_journey_group_key: str = None,
        re_shop_reason_code: str = None,
        selected_passengers_shrink: str = None,
        total_re_shop_fee: int = None,
    ):
        # The key for the asynchronous application.
        self.async_apply_key = async_apply_key
        # Specifies whether to use the asynchronous commit pattern. If asynchronous commit is used, only a key is returned before the application result is available.
        self.async_apply_mode = async_apply_mode
        # The business travel order ID. This parameter is required.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The ID of the rebooking product.
        # 
        # This parameter is required.
        self.ota_item_id = ota_item_id
        # The external order ID.
        self.out_order_id = out_order_id
        # The external rebooking application ID.
        self.out_re_shop_apply_id = out_re_shop_apply_id
        # The rebooking group key returned by the inquiry operation.
        # 
        # This parameter is required.
        self.passenger_journey_group_key = passenger_journey_group_key
        # The rebooking reason code.
        # 
        # This parameter is required.
        self.re_shop_reason_code = re_shop_reason_code
        # The list of passengers selected for rebooking.
        # 
        # This parameter is required.
        self.selected_passengers_shrink = selected_passengers_shrink
        # The total rebooking fee (excluding the service fee), in cents.
        #      * Total rebooking fee = cabin upgrade fee + handling fee + tax difference (applicable to international flights).
        #      * Pass in this parameter when fees are incurred to verify whether the price has changed.
        self.total_re_shop_fee = total_re_shop_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_apply_key is not None:
            result['async_apply_key'] = self.async_apply_key

        if self.async_apply_mode is not None:
            result['async_apply_mode'] = self.async_apply_mode

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_re_shop_apply_id is not None:
            result['out_re_shop_apply_id'] = self.out_re_shop_apply_id

        if self.passenger_journey_group_key is not None:
            result['passenger_journey_group_key'] = self.passenger_journey_group_key

        if self.re_shop_reason_code is not None:
            result['re_shop_reason_code'] = self.re_shop_reason_code

        if self.selected_passengers_shrink is not None:
            result['selected_passengers'] = self.selected_passengers_shrink

        if self.total_re_shop_fee is not None:
            result['total_re_shop_fee'] = self.total_re_shop_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_apply_key') is not None:
            self.async_apply_key = m.get('async_apply_key')

        if m.get('async_apply_mode') is not None:
            self.async_apply_mode = m.get('async_apply_mode')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_re_shop_apply_id') is not None:
            self.out_re_shop_apply_id = m.get('out_re_shop_apply_id')

        if m.get('passenger_journey_group_key') is not None:
            self.passenger_journey_group_key = m.get('passenger_journey_group_key')

        if m.get('re_shop_reason_code') is not None:
            self.re_shop_reason_code = m.get('re_shop_reason_code')

        if m.get('selected_passengers') is not None:
            self.selected_passengers_shrink = m.get('selected_passengers')

        if m.get('total_re_shop_fee') is not None:
            self.total_re_shop_fee = m.get('total_re_shop_fee')

        return self

