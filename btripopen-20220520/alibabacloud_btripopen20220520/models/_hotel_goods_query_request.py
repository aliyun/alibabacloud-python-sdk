# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelGoodsQueryRequest(DaraModel):
    def __init__(
        self,
        adult_num: str = None,
        agreement_price: bool = None,
        begin_date: str = None,
        breakfast_included: bool = None,
        btrip_user_id: str = None,
        city_code: str = None,
        end_date: str = None,
        hotel_id: str = None,
        pay_over_type: int = None,
        payment_type: int = None,
        special_invoice: bool = None,
        super_man: int = None,
    ):
        self.adult_num = adult_num
        self.agreement_price = agreement_price
        # This parameter is required.
        self.begin_date = begin_date
        self.breakfast_included = breakfast_included
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        self.city_code = city_code
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.hotel_id = hotel_id
        self.pay_over_type = pay_over_type
        self.payment_type = payment_type
        self.special_invoice = special_invoice
        self.super_man = super_man

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_num is not None:
            result['adult_num'] = self.adult_num

        if self.agreement_price is not None:
            result['agreement_price'] = self.agreement_price

        if self.begin_date is not None:
            result['begin_date'] = self.begin_date

        if self.breakfast_included is not None:
            result['breakfast_included'] = self.breakfast_included

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.end_date is not None:
            result['end_date'] = self.end_date

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.pay_over_type is not None:
            result['pay_over_type'] = self.pay_over_type

        if self.payment_type is not None:
            result['payment_type'] = self.payment_type

        if self.special_invoice is not None:
            result['special_invoice'] = self.special_invoice

        if self.super_man is not None:
            result['super_man'] = self.super_man

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_num') is not None:
            self.adult_num = m.get('adult_num')

        if m.get('agreement_price') is not None:
            self.agreement_price = m.get('agreement_price')

        if m.get('begin_date') is not None:
            self.begin_date = m.get('begin_date')

        if m.get('breakfast_included') is not None:
            self.breakfast_included = m.get('breakfast_included')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('pay_over_type') is not None:
            self.pay_over_type = m.get('pay_over_type')

        if m.get('payment_type') is not None:
            self.payment_type = m.get('payment_type')

        if m.get('special_invoice') is not None:
            self.special_invoice = m.get('special_invoice')

        if m.get('super_man') is not None:
            self.super_man = m.get('super_man')

        return self

