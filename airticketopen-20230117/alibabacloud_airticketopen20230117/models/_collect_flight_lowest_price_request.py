# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class CollectFlightLowestPriceRequest(DaraModel):
    def __init__(
        self,
        lowest_price_flight_info_list: List[main_models.CollectFlightLowestPriceRequestLowestPriceFlightInfoList] = None,
    ):
        # The lowest-price flight information.
        # 
        # This parameter is required.
        self.lowest_price_flight_info_list = lowest_price_flight_info_list

    def validate(self):
        if self.lowest_price_flight_info_list:
            for v1 in self.lowest_price_flight_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['lowest_price_flight_info_list'] = []
        if self.lowest_price_flight_info_list is not None:
            for k1 in self.lowest_price_flight_info_list:
                result['lowest_price_flight_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lowest_price_flight_info_list = []
        if m.get('lowest_price_flight_info_list') is not None:
            for k1 in m.get('lowest_price_flight_info_list'):
                temp_model = main_models.CollectFlightLowestPriceRequestLowestPriceFlightInfoList()
                self.lowest_price_flight_info_list.append(temp_model.from_map(k1))

        return self

class CollectFlightLowestPriceRequestLowestPriceFlightInfoList(DaraModel):
    def __init__(
        self,
        arrival_city: str = None,
        departure_city: str = None,
        departure_date: str = None,
        departure_flight_number: str = None,
        market_total_price: float = None,
        request_id: str = None,
        return_date: str = None,
        return_flight_number: str = None,
        solution_id: str = None,
        suez_total_price: float = None,
        trip_type: int = None,
    ):
        # The arrival city.
        # 
        # This parameter is required.
        self.arrival_city = arrival_city
        # The departure city.
        # 
        # This parameter is required.
        self.departure_city = departure_city
        # The departure date. Format: yyyy-MM-dd.
        # 
        # This parameter is required.
        self.departure_date = departure_date
        # The list of outbound flight numbers. Multiple segments are split by commas (,).
        # 
        # This parameter is required.
        self.departure_flight_number = departure_flight_number
        # The lowest competitor price in the market, including fare and taxes. The currency is USD.
        # 
        # This parameter is required.
        self.market_total_price = market_total_price
        # The request ID.
        self.request_id = request_id
        # The return date for round-trip scenarios. Format: yyyy-MM-dd.
        self.return_date = return_date
        # The list of return flight numbers. Multiple segments are split by commas (,).
        self.return_flight_number = return_flight_number
        # The solution_id returned by Search/Enrich.
        # 
        # This parameter is required.
        self.solution_id = solution_id
        # The Suez quoted price, including fare and taxes. The currency is USD.
        # 
        # This parameter is required.
        self.suez_total_price = suez_total_price
        # The trip type. Valid values:
        # - 1: one-way
        # - 2: round-trip.
        # 
        # This parameter is required.
        self.trip_type = trip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city

        if self.departure_city is not None:
            result['departure_city'] = self.departure_city

        if self.departure_date is not None:
            result['departure_date'] = self.departure_date

        if self.departure_flight_number is not None:
            result['departure_flight_number'] = self.departure_flight_number

        if self.market_total_price is not None:
            result['market_total_price'] = self.market_total_price

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.return_date is not None:
            result['return_date'] = self.return_date

        if self.return_flight_number is not None:
            result['return_flight_number'] = self.return_flight_number

        if self.solution_id is not None:
            result['solution_id'] = self.solution_id

        if self.suez_total_price is not None:
            result['suez_total_price'] = self.suez_total_price

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')

        if m.get('departure_flight_number') is not None:
            self.departure_flight_number = m.get('departure_flight_number')

        if m.get('market_total_price') is not None:
            self.market_total_price = m.get('market_total_price')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('return_date') is not None:
            self.return_date = m.get('return_date')

        if m.get('return_flight_number') is not None:
            self.return_flight_number = m.get('return_flight_number')

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        if m.get('suez_total_price') is not None:
            self.suez_total_price = m.get('suez_total_price')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

