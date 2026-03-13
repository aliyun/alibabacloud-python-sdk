# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightOtaSearchV2Request(DaraModel):
    def __init__(
        self,
        cabin_type_list: List[int] = None,
        direct_only: bool = None,
        isv_name: str = None,
        need_share_flight: bool = None,
        search_journeys: List[main_models.FlightOtaSearchV2RequestSearchJourneys] = None,
        search_mode: int = None,
        trip_type: int = None,
    ):
        self.cabin_type_list = cabin_type_list
        self.direct_only = direct_only
        # This parameter is required.
        self.isv_name = isv_name
        self.need_share_flight = need_share_flight
        # This parameter is required.
        self.search_journeys = search_journeys
        # This parameter is required.
        self.search_mode = search_mode
        # This parameter is required.
        self.trip_type = trip_type

    def validate(self):
        if self.search_journeys:
            for v1 in self.search_journeys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin_type_list is not None:
            result['cabin_type_list'] = self.cabin_type_list

        if self.direct_only is not None:
            result['direct_only'] = self.direct_only

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.need_share_flight is not None:
            result['need_share_flight'] = self.need_share_flight

        result['search_journeys'] = []
        if self.search_journeys is not None:
            for k1 in self.search_journeys:
                result['search_journeys'].append(k1.to_map() if k1 else None)

        if self.search_mode is not None:
            result['search_mode'] = self.search_mode

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin_type_list') is not None:
            self.cabin_type_list = m.get('cabin_type_list')

        if m.get('direct_only') is not None:
            self.direct_only = m.get('direct_only')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('need_share_flight') is not None:
            self.need_share_flight = m.get('need_share_flight')

        self.search_journeys = []
        if m.get('search_journeys') is not None:
            for k1 in m.get('search_journeys'):
                temp_model = main_models.FlightOtaSearchV2RequestSearchJourneys()
                self.search_journeys.append(temp_model.from_map(k1))

        if m.get('search_mode') is not None:
            self.search_mode = m.get('search_mode')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class FlightOtaSearchV2RequestSearchJourneys(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        selected_flights: List[main_models.FlightOtaSearchV2RequestSearchJourneysSelectedFlights] = None,
    ):
        # This parameter is required.
        self.arr_city_code = arr_city_code
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.selected_flights = selected_flights

    def validate(self):
        if self.selected_flights:
            for v1 in self.selected_flights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        result['selected_flights'] = []
        if self.selected_flights is not None:
            for k1 in self.selected_flights:
                result['selected_flights'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        self.selected_flights = []
        if m.get('selected_flights') is not None:
            for k1 in m.get('selected_flights'):
                temp_model = main_models.FlightOtaSearchV2RequestSearchJourneysSelectedFlights()
                self.selected_flights.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchV2RequestSearchJourneysSelectedFlights(DaraModel):
    def __init__(
        self,
        arr_airport_code: str = None,
        arr_city_code: str = None,
        dep_airport_code: str = None,
        dep_city_code: str = None,
        flight_time: str = None,
        market_flight_no: str = None,
        operate_flight_no: str = None,
    ):
        self.arr_airport_code = arr_airport_code
        self.arr_city_code = arr_city_code
        self.dep_airport_code = dep_airport_code
        self.dep_city_code = dep_city_code
        self.flight_time = flight_time
        # This parameter is required.
        self.market_flight_no = market_flight_no
        self.operate_flight_no = operate_flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.flight_time is not None:
            result['flight_time'] = self.flight_time

        if self.market_flight_no is not None:
            result['market_flight_no'] = self.market_flight_no

        if self.operate_flight_no is not None:
            result['operate_flight_no'] = self.operate_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('flight_time') is not None:
            self.flight_time = m.get('flight_time')

        if m.get('market_flight_no') is not None:
            self.market_flight_no = m.get('market_flight_no')

        if m.get('operate_flight_no') is not None:
            self.operate_flight_no = m.get('operate_flight_no')

        return self

