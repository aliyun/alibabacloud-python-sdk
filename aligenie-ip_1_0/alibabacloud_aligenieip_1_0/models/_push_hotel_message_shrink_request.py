# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushHotelMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        push_hotel_message_req_shrink: str = None,
    ):
        # pushHotelMessageReq
        # 
        # This parameter is required.
        self.push_hotel_message_req_shrink = push_hotel_message_req_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_hotel_message_req_shrink is not None:
            result['PushHotelMessageReq'] = self.push_hotel_message_req_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushHotelMessageReq') is not None:
            self.push_hotel_message_req_shrink = m.get('PushHotelMessageReq')

        return self

