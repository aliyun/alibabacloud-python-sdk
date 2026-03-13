# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightOtaSearchRequest(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        arr_city_code: str = None,
        cabin_class: str = None,
        carrier_flight_no: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        flight_no: str = None,
    ):
        self.airline_code = airline_code
        # This parameter is required.
        self.arr_city_code = arr_city_code
        self.cabin_class = cabin_class
        self.carrier_flight_no = carrier_flight_no
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.flight_no = flight_no

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

        if self.carrier_flight_no is not None:
            result['carrier_flight_no'] = self.carrier_flight_no

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('carrier_flight_no') is not None:
            self.carrier_flight_no = m.get('carrier_flight_no')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

