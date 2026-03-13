# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelCityCodeListRequest(DaraModel):
    def __init__(
        self,
        country_code: str = None,
    ):
        self.country_code = country_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.country_code is not None:
            result['country_code'] = self.country_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        return self

