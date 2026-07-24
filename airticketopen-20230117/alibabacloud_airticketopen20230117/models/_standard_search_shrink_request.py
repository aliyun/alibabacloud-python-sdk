# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StandardSearchShrinkRequest(DaraModel):
    def __init__(
        self,
        adults: int = None,
        air_legs_shrink: str = None,
        cabin_class: str = None,
        children: int = None,
        infants: int = None,
        search_control_options_shrink: str = None,
    ):
        # Number of adult passengers, range 1-9
        self.adults = adults
        # Journey array. At least one of departure_city and departure_airport_list must be non-empty; when departure_airport_list has values, they must belong to the same city. At least one of arrival_city and arrival_airport_list must be non-empty; when arrival_airport_list has values, they must belong to the same city.
        # 
        # This parameter is required.
        self.air_legs_shrink = air_legs_shrink
        # Defaults to ALL_CABIN if not specified. Cabin class ALL_CABIN: All cabin classes; Y: Economy class; FC: First class and Business class; S: Premium Economy class; YS: Economy class and Premium Economy class; YSC: Economy class, Premium Economy class, and Business class;
        self.cabin_class = cabin_class
        # Number of child passengers, range 0-9
        self.children = children
        # Number of infant passengers, range 0-9
        self.infants = infants
        # Search control options, optional
        self.search_control_options_shrink = search_control_options_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adults is not None:
            result['adults'] = self.adults

        if self.air_legs_shrink is not None:
            result['air_legs'] = self.air_legs_shrink

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.children is not None:
            result['children'] = self.children

        if self.infants is not None:
            result['infants'] = self.infants

        if self.search_control_options_shrink is not None:
            result['search_control_options'] = self.search_control_options_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adults') is not None:
            self.adults = m.get('adults')

        if m.get('air_legs') is not None:
            self.air_legs_shrink = m.get('air_legs')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('children') is not None:
            self.children = m.get('children')

        if m.get('infants') is not None:
            self.infants = m.get('infants')

        if m.get('search_control_options') is not None:
            self.search_control_options_shrink = m.get('search_control_options')

        return self

