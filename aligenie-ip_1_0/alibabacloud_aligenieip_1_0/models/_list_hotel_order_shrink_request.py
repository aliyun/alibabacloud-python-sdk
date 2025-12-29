# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotelOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

