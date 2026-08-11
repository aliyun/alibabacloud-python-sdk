# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GlobalHotelValidatePriceShrinkRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        adults: int = None,
        children: int = None,
        children_ages_shrink: str = None,
        item_offer_key: str = None,
        room_count: int = None,
        tracer_id: str = None,
    ):
        # The distributor account ID.
        # 
        # This parameter is required.
        self.account_no = account_no
        # The number of adults per room.
        # 
        # This parameter is required.
        self.adults = adults
        # The number of children per room.
        self.children = children
        # The list of children ages.
        self.children_ages_shrink = children_ages_shrink
        # The offer key.
        # 
        # This parameter is required.
        self.item_offer_key = item_offer_key
        # The number of rooms.
        # 
        # This parameter is required.
        self.room_count = room_count
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.adults is not None:
            result['Adults'] = self.adults

        if self.children is not None:
            result['Children'] = self.children

        if self.children_ages_shrink is not None:
            result['ChildrenAges'] = self.children_ages_shrink

        if self.item_offer_key is not None:
            result['ItemOfferKey'] = self.item_offer_key

        if self.room_count is not None:
            result['RoomCount'] = self.room_count

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('Adults') is not None:
            self.adults = m.get('Adults')

        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('ChildrenAges') is not None:
            self.children_ages_shrink = m.get('ChildrenAges')

        if m.get('ItemOfferKey') is not None:
            self.item_offer_key = m.get('ItemOfferKey')

        if m.get('RoomCount') is not None:
            self.room_count = m.get('RoomCount')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

