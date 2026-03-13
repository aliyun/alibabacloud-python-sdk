# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightOtaSearchV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        cabin_type_list_shrink: str = None,
        direct_only: bool = None,
        isv_name: str = None,
        need_share_flight: bool = None,
        search_journeys_shrink: str = None,
        search_mode: int = None,
        trip_type: int = None,
    ):
        self.cabin_type_list_shrink = cabin_type_list_shrink
        self.direct_only = direct_only
        # This parameter is required.
        self.isv_name = isv_name
        self.need_share_flight = need_share_flight
        # This parameter is required.
        self.search_journeys_shrink = search_journeys_shrink
        # This parameter is required.
        self.search_mode = search_mode
        # This parameter is required.
        self.trip_type = trip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin_type_list_shrink is not None:
            result['cabin_type_list'] = self.cabin_type_list_shrink

        if self.direct_only is not None:
            result['direct_only'] = self.direct_only

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.need_share_flight is not None:
            result['need_share_flight'] = self.need_share_flight

        if self.search_journeys_shrink is not None:
            result['search_journeys'] = self.search_journeys_shrink

        if self.search_mode is not None:
            result['search_mode'] = self.search_mode

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin_type_list') is not None:
            self.cabin_type_list_shrink = m.get('cabin_type_list')

        if m.get('direct_only') is not None:
            self.direct_only = m.get('direct_only')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('need_share_flight') is not None:
            self.need_share_flight = m.get('need_share_flight')

        if m.get('search_journeys') is not None:
            self.search_journeys_shrink = m.get('search_journeys')

        if m.get('search_mode') is not None:
            self.search_mode = m.get('search_mode')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

