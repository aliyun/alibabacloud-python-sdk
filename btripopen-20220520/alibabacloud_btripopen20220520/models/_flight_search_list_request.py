# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightSearchListRequest(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_date: str = None,
        cabin_class: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_date: str = None,
        flight_no: str = None,
        need_multi_class_price: bool = None,
        transfer_city_code: str = None,
        transfer_flight_no: str = None,
        transfer_leave_date: str = None,
        trip_type: str = None,
    ):
        self.airline_code = airline_code
        # This parameter is required.
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_date = arr_date
        self.cabin_class = cabin_class
        # This parameter is required.
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        # This parameter is required.
        self.dep_date = dep_date
        self.flight_no = flight_no
        self.need_multi_class_price = need_multi_class_price
        self.transfer_city_code = transfer_city_code
        self.transfer_flight_no = transfer_flight_no
        self.transfer_leave_date = transfer_leave_date
        # This parameter is required.
        self.trip_type = trip_type

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

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.need_multi_class_price is not None:
            result['need_multi_class_price'] = self.need_multi_class_price

        if self.transfer_city_code is not None:
            result['transfer_city_code'] = self.transfer_city_code

        if self.transfer_flight_no is not None:
            result['transfer_flight_no'] = self.transfer_flight_no

        if self.transfer_leave_date is not None:
            result['transfer_leave_date'] = self.transfer_leave_date

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('need_multi_class_price') is not None:
            self.need_multi_class_price = m.get('need_multi_class_price')

        if m.get('transfer_city_code') is not None:
            self.transfer_city_code = m.get('transfer_city_code')

        if m.get('transfer_flight_no') is not None:
            self.transfer_flight_no = m.get('transfer_flight_no')

        if m.get('transfer_leave_date') is not None:
            self.transfer_leave_date = m.get('transfer_leave_date')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

