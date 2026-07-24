# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchShrinkRequest(DaraModel):
    def __init__(
        self,
        adults: int = None,
        air_legs_shrink: str = None,
        cabin_class: str = None,
        children: int = None,
        infants: int = None,
        search_control_options_shrink: str = None,
    ):
        # The number of adult passengers. Valid values: 1 to 9.
        self.adults = adults
        # The journey array.
        # 
        # This parameter is required.
        self.air_legs_shrink = air_legs_shrink
        # The cabin class. Valid values: ALL_CABIN: all cabin classes. Y: economy class. FC: first class and business class. S: premium economy class. YS: economy class and premium economy class. YSC: economy class, premium economy class, and business class.
        self.cabin_class = cabin_class
        # The number of child passengers. Valid values: 0 to 9.
        self.children = children
        # The number of infant passengers. Valid values: 0 to 9.
        self.infants = infants
        # The search control options. This parameter is optional.
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

