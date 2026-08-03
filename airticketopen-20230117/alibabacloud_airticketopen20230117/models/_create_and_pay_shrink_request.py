# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAndPayShrinkRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        contact_shrink: str = None,
        external_order_no: str = None,
        guests_shrink: str = None,
        item_offer_id: str = None,
        room_count: int = None,
        tracer_id: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.contact_shrink = contact_shrink
        self.external_order_no = external_order_no
        # This parameter is required.
        self.guests_shrink = guests_shrink
        # This parameter is required.
        self.item_offer_id = item_offer_id
        # This parameter is required.
        self.room_count = room_count
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

        if self.contact_shrink is not None:
            result['Contact'] = self.contact_shrink

        if self.external_order_no is not None:
            result['ExternalOrderNo'] = self.external_order_no

        if self.guests_shrink is not None:
            result['Guests'] = self.guests_shrink

        if self.item_offer_id is not None:
            result['ItemOfferId'] = self.item_offer_id

        if self.room_count is not None:
            result['RoomCount'] = self.room_count

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('Contact') is not None:
            self.contact_shrink = m.get('Contact')

        if m.get('ExternalOrderNo') is not None:
            self.external_order_no = m.get('ExternalOrderNo')

        if m.get('Guests') is not None:
            self.guests_shrink = m.get('Guests')

        if m.get('ItemOfferId') is not None:
            self.item_offer_id = m.get('ItemOfferId')

        if m.get('RoomCount') is not None:
            self.room_count = m.get('RoomCount')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

