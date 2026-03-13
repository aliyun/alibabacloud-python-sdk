# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightCreateOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        arr_airport_code: str = None,
        arr_city_code: str = None,
        auto_pay: int = None,
        buyer_name: str = None,
        buyer_unique_key: str = None,
        contact_info_shrink: str = None,
        dep_airport_code: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        dis_order_id: str = None,
        order_attr_shrink: str = None,
        order_params: str = None,
        ota_item_id: str = None,
        price: int = None,
        receipt_address: str = None,
        receipt_target: int = None,
        receipt_title: str = None,
        traveler_info_list_shrink: str = None,
        trip_type: int = None,
    ):
        self.arr_airport_code = arr_airport_code
        # This parameter is required.
        self.arr_city_code = arr_city_code
        self.auto_pay = auto_pay
        self.buyer_name = buyer_name
        # This parameter is required.
        self.buyer_unique_key = buyer_unique_key
        # This parameter is required.
        self.contact_info_shrink = contact_info_shrink
        self.dep_airport_code = dep_airport_code
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.order_attr_shrink = order_attr_shrink
        # This parameter is required.
        self.order_params = order_params
        # This parameter is required.
        self.ota_item_id = ota_item_id
        # This parameter is required.
        self.price = price
        self.receipt_address = receipt_address
        self.receipt_target = receipt_target
        self.receipt_title = receipt_title
        # This parameter is required.
        self.traveler_info_list_shrink = traveler_info_list_shrink
        # This parameter is required.
        self.trip_type = trip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.auto_pay is not None:
            result['auto_pay'] = self.auto_pay

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.buyer_unique_key is not None:
            result['buyer_unique_key'] = self.buyer_unique_key

        if self.contact_info_shrink is not None:
            result['contact_info'] = self.contact_info_shrink

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.order_attr_shrink is not None:
            result['order_attr'] = self.order_attr_shrink

        if self.order_params is not None:
            result['order_params'] = self.order_params

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.price is not None:
            result['price'] = self.price

        if self.receipt_address is not None:
            result['receipt_address'] = self.receipt_address

        if self.receipt_target is not None:
            result['receipt_target'] = self.receipt_target

        if self.receipt_title is not None:
            result['receipt_title'] = self.receipt_title

        if self.traveler_info_list_shrink is not None:
            result['traveler_info_list'] = self.traveler_info_list_shrink

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('auto_pay') is not None:
            self.auto_pay = m.get('auto_pay')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('buyer_unique_key') is not None:
            self.buyer_unique_key = m.get('buyer_unique_key')

        if m.get('contact_info') is not None:
            self.contact_info_shrink = m.get('contact_info')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('order_attr') is not None:
            self.order_attr_shrink = m.get('order_attr')

        if m.get('order_params') is not None:
            self.order_params = m.get('order_params')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('receipt_address') is not None:
            self.receipt_address = m.get('receipt_address')

        if m.get('receipt_target') is not None:
            self.receipt_target = m.get('receipt_target')

        if m.get('receipt_title') is not None:
            self.receipt_title = m.get('receipt_title')

        if m.get('traveler_info_list') is not None:
            self.traveler_info_list_shrink = m.get('traveler_info_list')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

