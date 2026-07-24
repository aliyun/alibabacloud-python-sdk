# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class LuggageDirectRequest(DaraModel):
    def __init__(
        self,
        flight_segment_param_list: List[main_models.LuggageDirectRequestFlightSegmentParamList] = None,
    ):
        # The list of flight segments that constitute an itinerary. Maximum size: 2.
        self.flight_segment_param_list = flight_segment_param_list

    def validate(self):
        if self.flight_segment_param_list:
            for v1 in self.flight_segment_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_segment_param_list'] = []
        if self.flight_segment_param_list is not None:
            for k1 in self.flight_segment_param_list:
                result['flight_segment_param_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_segment_param_list = []
        if m.get('flight_segment_param_list') is not None:
            for k1 in m.get('flight_segment_param_list'):
                temp_model = main_models.LuggageDirectRequestFlightSegmentParamList()
                self.flight_segment_param_list.append(temp_model.from_map(k1))

        return self

class LuggageDirectRequestFlightSegmentParamList(DaraModel):
    def __init__(
        self,
        arrival_airport: str = None,
        arrival_terminal: str = None,
        arrival_time: int = None,
        code_share: bool = None,
        departure_airport: str = None,
        departure_terminal: str = None,
        departure_time: int = None,
        marketing_airline: str = None,
        marketing_flight_no: str = None,
        operating_airline: str = None,
        stop_city_list: str = None,
        ticketing_airline: str = None,
    ):
        # The three-letter IATA code of the arrival airport.
        # 
        # This parameter is required.
        self.arrival_airport = arrival_airport
        # The arrival terminal.
        self.arrival_terminal = arrival_terminal
        # The arrival time. A 13-digit UNIX timestamp.
        # 
        # This parameter is required.
        self.arrival_time = arrival_time
        # Indicates whether the flight is a codeshare flight.
        # 
        # This parameter is required.
        self.code_share = code_share
        # The three-letter IATA code of the departure airport.
        # 
        # This parameter is required.
        self.departure_airport = departure_airport
        # The departure terminal.
        self.departure_terminal = departure_terminal
        # The departure time. A 13-digit UNIX timestamp.
        # 
        # This parameter is required.
        self.departure_time = departure_time
        # The marketing airline.
        # 
        # This parameter is required.
        self.marketing_airline = marketing_airline
        # The flight number.
        # 
        # This parameter is required.
        self.marketing_flight_no = marketing_flight_no
        # The operating airline.
        self.operating_airline = operating_airline
        # The three-letter IATA codes of stopover cities.
        self.stop_city_list = stop_city_list
        # The ticketing airline.
        self.ticketing_airline = ticketing_airline

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport

        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal

        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time

        if self.code_share is not None:
            result['code_share'] = self.code_share

        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport

        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal

        if self.departure_time is not None:
            result['departure_time'] = self.departure_time

        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline

        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no

        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline

        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list

        if self.ticketing_airline is not None:
            result['ticketing_airline'] = self.ticketing_airline

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')

        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')

        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')

        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')

        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')

        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')

        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')

        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')

        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')

        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')

        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')

        if m.get('ticketing_airline') is not None:
            self.ticketing_airline = m.get('ticketing_airline')

        return self

