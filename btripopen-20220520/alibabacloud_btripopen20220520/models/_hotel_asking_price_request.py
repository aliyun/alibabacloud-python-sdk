# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HotelAskingPriceRequest(DaraModel):
    def __init__(
        self,
        adult_num: str = None,
        btrip_user_id: str = None,
        check_in_date: str = None,
        check_out_date: str = None,
        city_code: str = None,
        city_name: str = None,
        dir: int = None,
        hotel_star: str = None,
        is_protocol: bool = None,
        payment_type: int = None,
        shids: List[int] = None,
        sort_code: int = None,
    ):
        self.adult_num = adult_num
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.check_in_date = check_in_date
        # This parameter is required.
        self.check_out_date = check_out_date
        self.city_code = city_code
        self.city_name = city_name
        self.dir = dir
        self.hotel_star = hotel_star
        self.is_protocol = is_protocol
        self.payment_type = payment_type
        # This parameter is required.
        self.shids = shids
        self.sort_code = sort_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_num is not None:
            result['adult_num'] = self.adult_num

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.check_in_date is not None:
            result['check_in_date'] = self.check_in_date

        if self.check_out_date is not None:
            result['check_out_date'] = self.check_out_date

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.dir is not None:
            result['dir'] = self.dir

        if self.hotel_star is not None:
            result['hotel_star'] = self.hotel_star

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.payment_type is not None:
            result['payment_type'] = self.payment_type

        if self.shids is not None:
            result['shids'] = self.shids

        if self.sort_code is not None:
            result['sort_code'] = self.sort_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_num') is not None:
            self.adult_num = m.get('adult_num')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('check_in_date') is not None:
            self.check_in_date = m.get('check_in_date')

        if m.get('check_out_date') is not None:
            self.check_out_date = m.get('check_out_date')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('dir') is not None:
            self.dir = m.get('dir')

        if m.get('hotel_star') is not None:
            self.hotel_star = m.get('hotel_star')

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('payment_type') is not None:
            self.payment_type = m.get('payment_type')

        if m.get('shids') is not None:
            self.shids = m.get('shids')

        if m.get('sort_code') is not None:
            self.sort_code = m.get('sort_code')

        return self

