# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelSuggestV2Request(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        check_in: str = None,
        check_out: str = None,
        city_code: str = None,
        keyword: str = None,
        search_type: int = None,
    ):
        self.btrip_user_id = btrip_user_id
        self.check_in = check_in
        self.check_out = check_out
        self.city_code = city_code
        self.keyword = keyword
        # This parameter is required.
        self.search_type = search_type

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

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.search_type is not None:
            result['search_type'] = self.search_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('search_type') is not None:
            self.search_type = m.get('search_type')

        return self

