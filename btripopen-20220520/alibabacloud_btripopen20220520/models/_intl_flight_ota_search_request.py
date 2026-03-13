# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightOtaSearchRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        buyer_name: str = None,
        cabin_type: int = None,
        isv_name: str = None,
        search_journeys: List[main_models.IntlFlightOtaSearchRequestSearchJourneys] = None,
        search_passenger_list: List[main_models.IntlFlightOtaSearchRequestSearchPassengerList] = None,
        trip_type: int = None,
    ):
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        self.cabin_type = cabin_type
        self.isv_name = isv_name
        # This parameter is required.
        self.search_journeys = search_journeys
        self.search_passenger_list = search_passenger_list
        # This parameter is required.
        self.trip_type = trip_type

    def validate(self):
        if self.search_journeys:
            for v1 in self.search_journeys:
                 if v1:
                    v1.validate()
        if self.search_passenger_list:
            for v1 in self.search_passenger_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.cabin_type is not None:
            result['cabin_type'] = self.cabin_type

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        result['search_journeys'] = []
        if self.search_journeys is not None:
            for k1 in self.search_journeys:
                result['search_journeys'].append(k1.to_map() if k1 else None)

        result['search_passenger_list'] = []
        if self.search_passenger_list is not None:
            for k1 in self.search_passenger_list:
                result['search_passenger_list'].append(k1.to_map() if k1 else None)

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('cabin_type') is not None:
            self.cabin_type = m.get('cabin_type')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        self.search_journeys = []
        if m.get('search_journeys') is not None:
            for k1 in m.get('search_journeys'):
                temp_model = main_models.IntlFlightOtaSearchRequestSearchJourneys()
                self.search_journeys.append(temp_model.from_map(k1))

        self.search_passenger_list = []
        if m.get('search_passenger_list') is not None:
            for k1 in m.get('search_passenger_list'):
                temp_model = main_models.IntlFlightOtaSearchRequestSearchPassengerList()
                self.search_passenger_list.append(temp_model.from_map(k1))

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class IntlFlightOtaSearchRequestSearchPassengerList(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        cert_type: int = None,
        full_name: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.cert_no = cert_no
        # This parameter is required.
        self.cert_type = cert_type
        # This parameter is required.
        self.full_name = full_name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class IntlFlightOtaSearchRequestSearchJourneys(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        selected_flights: List[main_models.IntlFlightOtaSearchRequestSearchJourneysSelectedFlights] = None,
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
                temp_model = main_models.IntlFlightOtaSearchRequestSearchJourneysSelectedFlights()
                self.selected_flights.append(temp_model.from_map(k1))

        return self

class IntlFlightOtaSearchRequestSearchJourneysSelectedFlights(DaraModel):
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
        # This parameter is required.
        self.arr_city_code = arr_city_code
        self.dep_airport_code = dep_airport_code
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
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

