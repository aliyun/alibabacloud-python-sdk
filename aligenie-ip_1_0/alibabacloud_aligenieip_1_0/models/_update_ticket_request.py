# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTicketRequest(DaraModel):
    def __init__(
        self,
        group_key: str = None,
        hotel_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.group_key = group_key
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_key is not None:
            result['GroupKey'] = self.group_key

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

