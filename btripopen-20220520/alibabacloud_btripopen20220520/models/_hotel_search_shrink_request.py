# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelSearchShrinkRequest(DaraModel):
    def __init__(
        self,
        adult_num: str = None,
        brand_code_shrink: str = None,
        btrip_user_id: str = None,
        check_in_date: str = None,
        check_out_date: str = None,
        city_code: str = None,
        dir: int = None,
        distance: int = None,
        district_code: str = None,
        hotel_star: str = None,
        is_protocol: bool = None,
        key_words: str = None,
        location: str = None,
        max_price: float = None,
        min_price: float = None,
        page_no: int = None,
        page_size: int = None,
        pay_over_type: int = None,
        payment_type: int = None,
        shids_shrink: str = None,
        sort_code: int = None,
        super_man: int = None,
    ):
        self.adult_num = adult_num
        self.brand_code_shrink = brand_code_shrink
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.check_in_date = check_in_date
        # This parameter is required.
        self.check_out_date = check_out_date
        self.city_code = city_code
        self.dir = dir
        self.distance = distance
        self.district_code = district_code
        self.hotel_star = hotel_star
        self.is_protocol = is_protocol
        self.key_words = key_words
        self.location = location
        self.max_price = max_price
        self.min_price = min_price
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.pay_over_type = pay_over_type
        self.payment_type = payment_type
        self.shids_shrink = shids_shrink
        # This parameter is required.
        self.sort_code = sort_code
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

        if self.brand_code_shrink is not None:
            result['brand_code'] = self.brand_code_shrink

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.check_in_date is not None:
            result['check_in_date'] = self.check_in_date

        if self.check_out_date is not None:
            result['check_out_date'] = self.check_out_date

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.dir is not None:
            result['dir'] = self.dir

        if self.distance is not None:
            result['distance'] = self.distance

        if self.district_code is not None:
            result['district_code'] = self.district_code

        if self.hotel_star is not None:
            result['hotel_star'] = self.hotel_star

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.key_words is not None:
            result['key_words'] = self.key_words

        if self.location is not None:
            result['location'] = self.location

        if self.max_price is not None:
            result['max_price'] = self.max_price

        if self.min_price is not None:
            result['min_price'] = self.min_price

        if self.page_no is not None:
            result['page_no'] = self.page_no

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.pay_over_type is not None:
            result['pay_over_type'] = self.pay_over_type

        if self.payment_type is not None:
            result['payment_type'] = self.payment_type

        if self.shids_shrink is not None:
            result['shids'] = self.shids_shrink

        if self.sort_code is not None:
            result['sort_code'] = self.sort_code

        if self.super_man is not None:
            result['super_man'] = self.super_man

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_num') is not None:
            self.adult_num = m.get('adult_num')

        if m.get('brand_code') is not None:
            self.brand_code_shrink = m.get('brand_code')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('check_in_date') is not None:
            self.check_in_date = m.get('check_in_date')

        if m.get('check_out_date') is not None:
            self.check_out_date = m.get('check_out_date')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('dir') is not None:
            self.dir = m.get('dir')

        if m.get('distance') is not None:
            self.distance = m.get('distance')

        if m.get('district_code') is not None:
            self.district_code = m.get('district_code')

        if m.get('hotel_star') is not None:
            self.hotel_star = m.get('hotel_star')

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('key_words') is not None:
            self.key_words = m.get('key_words')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('max_price') is not None:
            self.max_price = m.get('max_price')

        if m.get('min_price') is not None:
            self.min_price = m.get('min_price')

        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('pay_over_type') is not None:
            self.pay_over_type = m.get('pay_over_type')

        if m.get('payment_type') is not None:
            self.payment_type = m.get('payment_type')

        if m.get('shids') is not None:
            self.shids_shrink = m.get('shids')

        if m.get('sort_code') is not None:
            self.sort_code = m.get('sort_code')

        if m.get('super_man') is not None:
            self.super_man = m.get('super_man')

        return self

