# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class SearchRequest(DaraModel):
    def __init__(
        self,
        adults: int = None,
        air_legs: List[main_models.SearchRequestAirLegs] = None,
        cabin_class: str = None,
        children: int = None,
        infants: int = None,
        search_control_options: main_models.SearchRequestSearchControlOptions = None,
    ):
        # The number of adult passengers. Valid values: 1 to 9.
        self.adults = adults
        # The journey array.
        # 
        # This parameter is required.
        self.air_legs = air_legs
        # The cabin class. Valid values: ALL_CABIN: all cabin classes. Y: economy class. FC: first class and business class. S: premium economy class. YS: economy class and premium economy class. YSC: economy class, premium economy class, and business class.
        self.cabin_class = cabin_class
        # The number of child passengers. Valid values: 0 to 9.
        self.children = children
        # The number of infant passengers. Valid values: 0 to 9.
        self.infants = infants
        # The search control options. This parameter is optional.
        self.search_control_options = search_control_options

    def validate(self):
        if self.air_legs:
            for v1 in self.air_legs:
                 if v1:
                    v1.validate()
        if self.search_control_options:
            self.search_control_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adults is not None:
            result['adults'] = self.adults

        result['air_legs'] = []
        if self.air_legs is not None:
            for k1 in self.air_legs:
                result['air_legs'].append(k1.to_map() if k1 else None)

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.children is not None:
            result['children'] = self.children

        if self.infants is not None:
            result['infants'] = self.infants

        if self.search_control_options is not None:
            result['search_control_options'] = self.search_control_options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adults') is not None:
            self.adults = m.get('adults')

        self.air_legs = []
        if m.get('air_legs') is not None:
            for k1 in m.get('air_legs'):
                temp_model = main_models.SearchRequestAirLegs()
                self.air_legs.append(temp_model.from_map(k1))

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('children') is not None:
            self.children = m.get('children')

        if m.get('infants') is not None:
            self.infants = m.get('infants')

        if m.get('search_control_options') is not None:
            temp_model = main_models.SearchRequestSearchControlOptions()
            self.search_control_options = temp_model.from_map(m.get('search_control_options'))

        return self

class SearchRequestSearchControlOptions(DaraModel):
    def __init__(
        self,
        airline_excluded_list: List[str] = None,
        airline_prefer_list: List[str] = None,
        service_quality: str = None,
    ):
        # The list of excluded airlines.
        self.airline_excluded_list = airline_excluded_list
        # The list of preferred airlines.
        self.airline_prefer_list = airline_prefer_list
        # The service quality identifier.
        self.service_quality = service_quality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_excluded_list is not None:
            result['airline_excluded_list'] = self.airline_excluded_list

        if self.airline_prefer_list is not None:
            result['airline_prefer_list'] = self.airline_prefer_list

        if self.service_quality is not None:
            result['service_quality'] = self.service_quality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_excluded_list') is not None:
            self.airline_excluded_list = m.get('airline_excluded_list')

        if m.get('airline_prefer_list') is not None:
            self.airline_prefer_list = m.get('airline_prefer_list')

        if m.get('service_quality') is not None:
            self.service_quality = m.get('service_quality')

        return self

class SearchRequestAirLegs(DaraModel):
    def __init__(
        self,
        arrival_airport_list: List[str] = None,
        arrival_city: str = None,
        departure_airport_list: List[str] = None,
        departure_city: str = None,
        departure_date: str = None,
    ):
        # The list of three-letter codes of arrival airports.
        self.arrival_airport_list = arrival_airport_list
        # The three-letter code of the arrival city.
        self.arrival_city = arrival_city
        # The list of three-letter codes of departure airports.
        self.departure_airport_list = departure_airport_list
        # The three-letter code of the departure city.
        self.departure_city = departure_city
        # The departure date (for example, yyyyMMdd).
        # 
        # This parameter is required.
        self.departure_date = departure_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_airport_list is not None:
            result['arrival_airport_list'] = self.arrival_airport_list

        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city

        if self.departure_airport_list is not None:
            result['departure_airport_list'] = self.departure_airport_list

        if self.departure_city is not None:
            result['departure_city'] = self.departure_city

        if self.departure_date is not None:
            result['departure_date'] = self.departure_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_airport_list') is not None:
            self.arrival_airport_list = m.get('arrival_airport_list')

        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('departure_airport_list') is not None:
            self.departure_airport_list = m.get('departure_airport_list')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')

        return self

