# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightReShopCreateRequest(DaraModel):
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
        selected_passengers: List[main_models.IntlFlightReShopCreateRequestSelectedPassengers] = None,
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
        self.selected_passengers = selected_passengers
        # The total rebooking fee (excluding the service fee), in cents.
        #      * Total rebooking fee = cabin upgrade fee + handling fee + tax difference (applicable to international flights).
        #      * Pass in this parameter when fees are incurred to verify whether the price has changed.
        self.total_re_shop_fee = total_re_shop_fee

    def validate(self):
        if self.selected_passengers:
            for v1 in self.selected_passengers:
                 if v1:
                    v1.validate()

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

        result['selected_passengers'] = []
        if self.selected_passengers is not None:
            for k1 in self.selected_passengers:
                result['selected_passengers'].append(k1.to_map() if k1 else None)

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

        self.selected_passengers = []
        if m.get('selected_passengers') is not None:
            for k1 in m.get('selected_passengers'):
                temp_model = main_models.IntlFlightReShopCreateRequestSelectedPassengers()
                self.selected_passengers.append(temp_model.from_map(k1))

        if m.get('total_re_shop_fee') is not None:
            self.total_re_shop_fee = m.get('total_re_shop_fee')

        return self

class IntlFlightReShopCreateRequestSelectedPassengers(DaraModel):
    def __init__(
        self,
        full_name: str = None,
        passenger_id: int = None,
    ):
        # The full name of the passenger.
        self.full_name = full_name
        # The ID of the passenger.
        self.passenger_id = passenger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        return self

