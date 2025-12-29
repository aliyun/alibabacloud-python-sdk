# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteCustomQARequest(DaraModel):
    def __init__(
        self,
        custom_qaids: List[str] = None,
        hotel_id: str = None,
    ):
        self.custom_qaids = custom_qaids
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_qaids is not None:
            result['CustomQAIds'] = self.custom_qaids

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomQAIds') is not None:
            self.custom_qaids = m.get('CustomQAIds')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

