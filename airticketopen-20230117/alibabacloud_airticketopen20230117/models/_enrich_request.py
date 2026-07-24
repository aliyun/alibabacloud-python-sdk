# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class EnrichRequest(DaraModel):
    def __init__(
        self,
        adults: int = None,
        cabin_class: str = None,
        children: int = None,
        infants: int = None,
        journey_param_list: List[main_models.EnrichRequestJourneyParamList] = None,
        solution_id: str = None,
    ):
        # Number of adult passengers 1-9
        self.adults = adults
        # Cabin class ALL_CABIN: all cabin classes; Y: economy; FC: first class and business class; S: premium economy; YS: economy and premium economy; YSC: economy, premium economy, and business class;
        self.cabin_class = cabin_class
        # Number of child passengers 0-9
        self.children = children
        # Number of infant passengers 0-9
        self.infants = infants
        # Journey information
        self.journey_param_list = journey_param_list
        # solution_id returned by Search
        self.solution_id = solution_id

    def validate(self):
        if self.journey_param_list:
            for v1 in self.journey_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adults is not None:
            result['adults'] = self.adults

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.children is not None:
            result['children'] = self.children

        if self.infants is not None:
            result['infants'] = self.infants

        result['journey_param_list'] = []
        if self.journey_param_list is not None:
            for k1 in self.journey_param_list:
                result['journey_param_list'].append(k1.to_map() if k1 else None)

        if self.solution_id is not None:
            result['solution_id'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adults') is not None:
            self.adults = m.get('adults')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('children') is not None:
            self.children = m.get('children')

        if m.get('infants') is not None:
            self.infants = m.get('infants')

        self.journey_param_list = []
        if m.get('journey_param_list') is not None:
            for k1 in m.get('journey_param_list'):
                temp_model = main_models.EnrichRequestJourneyParamList()
                self.journey_param_list.append(temp_model.from_map(k1))

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

class EnrichRequestJourneyParamList(DaraModel):
    def __init__(
        self,
        arrival_city: str = None,
        departure_city: str = None,
        departure_date: str = None,
        segment_param_list: List[main_models.EnrichRequestJourneyParamListSegmentParamList] = None,
    ):
        # Arrival city code (3-letter uppercase)
        # 
        # This parameter is required.
        self.arrival_city = arrival_city
        # Departure city code (3-letter uppercase)
        # 
        # This parameter is required.
        self.departure_city = departure_city
        # Departure date (yyyyMMdd)
        # 
        # This parameter is required.
        self.departure_date = departure_date
        # Specified segment information for this journey
        # 
        # This parameter is required.
        self.segment_param_list = segment_param_list

    def validate(self):
        if self.segment_param_list:
            for v1 in self.segment_param_list:
                 if v1:
                    v1.validate()

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

        result['segment_param_list'] = []
        if self.segment_param_list is not None:
            for k1 in self.segment_param_list:
                result['segment_param_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')

        self.segment_param_list = []
        if m.get('segment_param_list') is not None:
            for k1 in m.get('segment_param_list'):
                temp_model = main_models.EnrichRequestJourneyParamListSegmentParamList()
                self.segment_param_list.append(temp_model.from_map(k1))

        return self

class EnrichRequestJourneyParamListSegmentParamList(DaraModel):
    def __init__(
        self,
        arrival_airport: str = None,
        arrival_city: str = None,
        cabin: str = None,
        child_cabin: str = None,
        departure_airport: str = None,
        departure_city: str = None,
        departure_date: str = None,
        departure_time: str = None,
        marketing_flight_no: str = None,
    ):
        # Flight arrival airport code (3-letter uppercase)
        self.arrival_airport = arrival_airport
        # Flight arrival city code (3-letter uppercase)
        self.arrival_city = arrival_city
        # Booking class
        self.cabin = cabin
        # Child booking class
        self.child_cabin = child_cabin
        # Flight departure airport code (3-letter uppercase)
        self.departure_airport = departure_airport
        # Flight departure city code (3-letter uppercase)
        self.departure_city = departure_city
        self.departure_date = departure_date
        # String, flight departure date and time (yyyy-MM-dd HH:mm:ss)
        self.departure_time = departure_time
        # Marketing carrier flight number (e.g., KA5809)
        # 
        # This parameter is required.
        self.marketing_flight_no = marketing_flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport

        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.child_cabin is not None:
            result['child_cabin'] = self.child_cabin

        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport

        if self.departure_city is not None:
            result['departure_city'] = self.departure_city

        if self.departure_date is not None:
            result['departure_date'] = self.departure_date

        if self.departure_time is not None:
            result['departure_time'] = self.departure_time

        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')

        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('child_cabin') is not None:
            self.child_cabin = m.get('child_cabin')

        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')

        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')

        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')

        return self

