# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotelsShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_request_shrink: str = None,
        page_shrink: str = None,
        status: int = None,
    ):
        self.hotel_request_shrink = hotel_request_shrink
        # This parameter is required.
        self.page_shrink = page_shrink
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_request_shrink is not None:
            result['HotelRequest'] = self.hotel_request_shrink

        if self.page_shrink is not None:
            result['Page'] = self.page_shrink

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelRequest') is not None:
            self.hotel_request_shrink = m.get('HotelRequest')

        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

