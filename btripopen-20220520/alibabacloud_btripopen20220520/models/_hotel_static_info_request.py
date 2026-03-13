# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HotelStaticInfoRequest(DaraModel):
    def __init__(
        self,
        hotel_ids: List[str] = None,
    ):
        # This parameter is required.
        self.hotel_ids = hotel_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_ids is not None:
            result['hotel_ids'] = self.hotel_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotel_ids') is not None:
            self.hotel_ids = m.get('hotel_ids')

        return self

