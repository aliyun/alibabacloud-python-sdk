# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomQAShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        keyword: str = None,
        page_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.keyword = keyword
        # This parameter is required.
        self.page_shrink = page_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_shrink is not None:
            result['Page'] = self.page_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')

        return self

