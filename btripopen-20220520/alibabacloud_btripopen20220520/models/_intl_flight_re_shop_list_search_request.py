# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightReShopListSearchRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        out_wheel_search: bool = None,
        passenger_journey_group_key: str = None,
        re_shop_reason_code: str = None,
        search_journeys: List[main_models.IntlFlightReShopListSearchRequestSearchJourneys] = None,
        selected_passengers: List[main_models.IntlFlightReShopListSearchRequestSelectedPassengers] = None,
        token: str = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_wheel_search = out_wheel_search
        # This parameter is required.
        self.passenger_journey_group_key = passenger_journey_group_key
        self.re_shop_reason_code = re_shop_reason_code
        # This parameter is required.
        self.search_journeys = search_journeys
        # This parameter is required.
        self.selected_passengers = selected_passengers
        self.token = token

    def validate(self):
        if self.search_journeys:
            for v1 in self.search_journeys:
                 if v1:
                    v1.validate()
        if self.selected_passengers:
            for v1 in self.selected_passengers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_wheel_search is not None:
            result['out_wheel_search'] = self.out_wheel_search

        if self.passenger_journey_group_key is not None:
            result['passenger_journey_group_key'] = self.passenger_journey_group_key

        if self.re_shop_reason_code is not None:
            result['re_shop_reason_code'] = self.re_shop_reason_code

        result['search_journeys'] = []
        if self.search_journeys is not None:
            for k1 in self.search_journeys:
                result['search_journeys'].append(k1.to_map() if k1 else None)

        result['selected_passengers'] = []
        if self.selected_passengers is not None:
            for k1 in self.selected_passengers:
                result['selected_passengers'].append(k1.to_map() if k1 else None)

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_wheel_search') is not None:
            self.out_wheel_search = m.get('out_wheel_search')

        if m.get('passenger_journey_group_key') is not None:
            self.passenger_journey_group_key = m.get('passenger_journey_group_key')

        if m.get('re_shop_reason_code') is not None:
            self.re_shop_reason_code = m.get('re_shop_reason_code')

        self.search_journeys = []
        if m.get('search_journeys') is not None:
            for k1 in m.get('search_journeys'):
                temp_model = main_models.IntlFlightReShopListSearchRequestSearchJourneys()
                self.search_journeys.append(temp_model.from_map(k1))

        self.selected_passengers = []
        if m.get('selected_passengers') is not None:
            for k1 in m.get('selected_passengers'):
                temp_model = main_models.IntlFlightReShopListSearchRequestSelectedPassengers()
                self.selected_passengers.append(temp_model.from_map(k1))

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

class IntlFlightReShopListSearchRequestSelectedPassengers(DaraModel):
    def __init__(
        self,
        full_name: str = None,
        passenger_id: int = None,
    ):
        self.full_name = full_name
        self.passenger_id = passenger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        return self

class IntlFlightReShopListSearchRequestSearchJourneys(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        selected_flights: List[main_models.IntlFlightReShopListSearchRequestSearchJourneysSelectedFlights] = None,
    ):
        self.arr_city_code = arr_city_code
        self.dep_city_code = dep_city_code
        self.dep_date = dep_date
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
                temp_model = main_models.IntlFlightReShopListSearchRequestSearchJourneysSelectedFlights()
                self.selected_flights.append(temp_model.from_map(k1))

        return self

class IntlFlightReShopListSearchRequestSearchJourneysSelectedFlights(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        flight_time: str = None,
        market_flight_no: str = None,
    ):
        self.arr_city_code = arr_city_code
        self.dep_city_code = dep_city_code
        self.flight_time = flight_time
        self.market_flight_no = market_flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.flight_time is not None:
            result['flight_time'] = self.flight_time

        if self.market_flight_no is not None:
            result['market_flight_no'] = self.market_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('flight_time') is not None:
            self.flight_time = m.get('flight_time')

        if m.get('market_flight_no') is not None:
            self.market_flight_no = m.get('market_flight_no')

        return self

