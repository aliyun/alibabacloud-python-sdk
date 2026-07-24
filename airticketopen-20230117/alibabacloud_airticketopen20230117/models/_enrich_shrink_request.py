# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnrichShrinkRequest(DaraModel):
    def __init__(
        self,
        adults: int = None,
        cabin_class: str = None,
        children: int = None,
        infants: int = None,
        journey_param_list_shrink: str = None,
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
        self.journey_param_list_shrink = journey_param_list_shrink
        # solution_id returned by Search
        self.solution_id = solution_id

    def validate(self):
        pass

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

        if self.journey_param_list_shrink is not None:
            result['journey_param_list'] = self.journey_param_list_shrink

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

        if m.get('journey_param_list') is not None:
            self.journey_param_list_shrink = m.get('journey_param_list')

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

