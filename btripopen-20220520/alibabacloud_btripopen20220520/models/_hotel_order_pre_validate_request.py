# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderPreValidateRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        check_in: str = None,
        check_out: str = None,
        daily_list: List[main_models.HotelOrderPreValidateRequestDailyList] = None,
        item_id: int = None,
        number_of_adults_per_room: int = None,
        occupant_info_list: List[main_models.HotelOrderPreValidateRequestOccupantInfoList] = None,
        rate_key: str = None,
        rate_plan_id: int = None,
        room_id: int = None,
        room_num: int = None,
        search_room_price: int = None,
        seller_id: int = None,
        shid: int = None,
    ):
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.check_in = check_in
        # This parameter is required.
        self.check_out = check_out
        # This parameter is required.
        self.daily_list = daily_list
        # This parameter is required.
        self.item_id = item_id
        self.number_of_adults_per_room = number_of_adults_per_room
        self.occupant_info_list = occupant_info_list
        self.rate_key = rate_key
        # This parameter is required.
        self.rate_plan_id = rate_plan_id
        # This parameter is required.
        self.room_id = room_id
        # This parameter is required.
        self.room_num = room_num
        # This parameter is required.
        self.search_room_price = search_room_price
        # This parameter is required.
        self.seller_id = seller_id
        # This parameter is required.
        self.shid = shid

    def validate(self):
        if self.daily_list:
            for v1 in self.daily_list:
                 if v1:
                    v1.validate()
        if self.occupant_info_list:
            for v1 in self.occupant_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        result['daily_list'] = []
        if self.daily_list is not None:
            for k1 in self.daily_list:
                result['daily_list'].append(k1.to_map() if k1 else None)

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.number_of_adults_per_room is not None:
            result['number_of_adults_per_room'] = self.number_of_adults_per_room

        result['occupant_info_list'] = []
        if self.occupant_info_list is not None:
            for k1 in self.occupant_info_list:
                result['occupant_info_list'].append(k1.to_map() if k1 else None)

        if self.rate_key is not None:
            result['rate_key'] = self.rate_key

        if self.rate_plan_id is not None:
            result['rate_plan_id'] = self.rate_plan_id

        if self.room_id is not None:
            result['room_id'] = self.room_id

        if self.room_num is not None:
            result['room_num'] = self.room_num

        if self.search_room_price is not None:
            result['search_room_price'] = self.search_room_price

        if self.seller_id is not None:
            result['seller_id'] = self.seller_id

        if self.shid is not None:
            result['shid'] = self.shid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        self.daily_list = []
        if m.get('daily_list') is not None:
            for k1 in m.get('daily_list'):
                temp_model = main_models.HotelOrderPreValidateRequestDailyList()
                self.daily_list.append(temp_model.from_map(k1))

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('number_of_adults_per_room') is not None:
            self.number_of_adults_per_room = m.get('number_of_adults_per_room')

        self.occupant_info_list = []
        if m.get('occupant_info_list') is not None:
            for k1 in m.get('occupant_info_list'):
                temp_model = main_models.HotelOrderPreValidateRequestOccupantInfoList()
                self.occupant_info_list.append(temp_model.from_map(k1))

        if m.get('rate_key') is not None:
            self.rate_key = m.get('rate_key')

        if m.get('rate_plan_id') is not None:
            self.rate_plan_id = m.get('rate_plan_id')

        if m.get('room_id') is not None:
            self.room_id = m.get('room_id')

        if m.get('room_num') is not None:
            self.room_num = m.get('room_num')

        if m.get('search_room_price') is not None:
            self.search_room_price = m.get('search_room_price')

        if m.get('seller_id') is not None:
            self.seller_id = m.get('seller_id')

        if m.get('shid') is not None:
            self.shid = m.get('shid')

        return self

class HotelOrderPreValidateRequestOccupantInfoList(DaraModel):
    def __init__(
        self,
        card_no: str = None,
        card_type: int = None,
        name: str = None,
        phone: str = None,
        staff_no: str = None,
        user_type: int = None,
    ):
        self.card_no = card_no
        self.card_type = card_type
        self.name = name
        self.phone = phone
        self.staff_no = staff_no
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_no is not None:
            result['card_no'] = self.card_no

        if self.card_type is not None:
            result['card_type'] = self.card_type

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.staff_no is not None:
            result['staff_no'] = self.staff_no

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('card_no') is not None:
            self.card_no = m.get('card_no')

        if m.get('card_type') is not None:
            self.card_type = m.get('card_type')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('staff_no') is not None:
            self.staff_no = m.get('staff_no')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class HotelOrderPreValidateRequestDailyList(DaraModel):
    def __init__(
        self,
        board: str = None,
        price: int = None,
        rate_start_time: str = None,
        room_count: int = None,
    ):
        self.board = board
        self.price = price
        self.rate_start_time = rate_start_time
        self.room_count = room_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.board is not None:
            result['board'] = self.board

        if self.price is not None:
            result['price'] = self.price

        if self.rate_start_time is not None:
            result['rate_start_time'] = self.rate_start_time

        if self.room_count is not None:
            result['room_count'] = self.room_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('board') is not None:
            self.board = m.get('board')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('rate_start_time') is not None:
            self.rate_start_time = m.get('rate_start_time')

        if m.get('room_count') is not None:
            self.room_count = m.get('room_count')

        return self

