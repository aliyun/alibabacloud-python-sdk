# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightListingSearchRequest(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        arr_city_code: str = None,
        cabin_class: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
    ):
        self.airline_code = airline_code
        # This parameter is required.
        self.arr_city_code = arr_city_code
        self.cabin_class = cabin_class
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.dep_date = dep_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        return self

