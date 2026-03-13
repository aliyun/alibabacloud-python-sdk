# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelOrderPreValidateShrinkRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        check_in: str = None,
        check_out: str = None,
        daily_list_shrink: str = None,
        item_id: int = None,
        number_of_adults_per_room: int = None,
        occupant_info_list_shrink: str = None,
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
        self.daily_list_shrink = daily_list_shrink
        # This parameter is required.
        self.item_id = item_id
        self.number_of_adults_per_room = number_of_adults_per_room
        self.occupant_info_list_shrink = occupant_info_list_shrink
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
        pass

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

        if self.daily_list_shrink is not None:
            result['daily_list'] = self.daily_list_shrink

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.number_of_adults_per_room is not None:
            result['number_of_adults_per_room'] = self.number_of_adults_per_room

        if self.occupant_info_list_shrink is not None:
            result['occupant_info_list'] = self.occupant_info_list_shrink

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

        if m.get('daily_list') is not None:
            self.daily_list_shrink = m.get('daily_list')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('number_of_adults_per_room') is not None:
            self.number_of_adults_per_room = m.get('number_of_adults_per_room')

        if m.get('occupant_info_list') is not None:
            self.occupant_info_list_shrink = m.get('occupant_info_list')

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

