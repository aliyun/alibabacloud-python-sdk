# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class StandardSearchRequest(DaraModel):
    def __init__(
        self,
        adults: int = None,
        air_legs: List[main_models.StandardSearchRequestAirLegs] = None,
        cabin_class: str = None,
        children: int = None,
        infants: int = None,
        search_control_options: main_models.StandardSearchRequestSearchControlOptions = None,
    ):
        # Number of adult passengers, range 1-9
        self.adults = adults
        # Journey array. At least one of departure_city and departure_airport_list must be non-empty; when departure_airport_list has values, they must belong to the same city. At least one of arrival_city and arrival_airport_list must be non-empty; when arrival_airport_list has values, they must belong to the same city.
        # 
        # This parameter is required.
        self.air_legs = air_legs
        # Defaults to ALL_CABIN if not specified. Cabin class ALL_CABIN: All cabin classes; Y: Economy class; FC: First class and Business class; S: Premium Economy class; YS: Economy class and Premium Economy class; YSC: Economy class, Premium Economy class, and Business class;
        self.cabin_class = cabin_class
        # Number of child passengers, range 0-9
        self.children = children
        # Number of infant passengers, range 0-9
        self.infants = infants
        # Search control options, optional
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
                temp_model = main_models.StandardSearchRequestAirLegs()
                self.air_legs.append(temp_model.from_map(k1))

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('children') is not None:
            self.children = m.get('children')

        if m.get('infants') is not None:
            self.infants = m.get('infants')

        if m.get('search_control_options') is not None:
            temp_model = main_models.StandardSearchRequestSearchControlOptions()
            self.search_control_options = temp_model.from_map(m.get('search_control_options'))

        return self

class StandardSearchRequestSearchControlOptions(DaraModel):
    def __init__(
        self,
        airline_excluded_list: List[str] = None,
        airline_prefer_list: List[str] = None,
        service_quality: str = None,
    ):
        # Excluded airlines list
        self.airline_excluded_list = airline_excluded_list
        # Preferred airlines list
        self.airline_prefer_list = airline_prefer_list
        # Ticketing service quality
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

class StandardSearchRequestAirLegs(DaraModel):
    def __init__(
        self,
        arrival_airport_list: List[str] = None,
        arrival_city: str = None,
        departure_airport_list: List[str] = None,
        departure_city: str = None,
        departure_date: str = None,
    ):
        # Arrival airport three-letter code
        self.arrival_airport_list = arrival_airport_list
        # Arrival city three-letter code
        self.arrival_city = arrival_city
        # Departure airport three-letter code
        self.departure_airport_list = departure_airport_list
        # Departure city three-letter code
        self.departure_city = departure_city
        # Departure date (e.g.: yyyyMMdd)
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

