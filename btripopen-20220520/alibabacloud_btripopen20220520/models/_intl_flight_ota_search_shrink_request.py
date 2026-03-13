# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightOtaSearchShrinkRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        buyer_name: str = None,
        cabin_type: int = None,
        isv_name: str = None,
        search_journeys_shrink: str = None,
        search_passenger_list_shrink: str = None,
        trip_type: int = None,
    ):
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        self.cabin_type = cabin_type
        self.isv_name = isv_name
        # This parameter is required.
        self.search_journeys_shrink = search_journeys_shrink
        self.search_passenger_list_shrink = search_passenger_list_shrink
        # This parameter is required.
        self.trip_type = trip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.cabin_type is not None:
            result['cabin_type'] = self.cabin_type

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.search_journeys_shrink is not None:
            result['search_journeys'] = self.search_journeys_shrink

        if self.search_passenger_list_shrink is not None:
            result['search_passenger_list'] = self.search_passenger_list_shrink

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('cabin_type') is not None:
            self.cabin_type = m.get('cabin_type')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('search_journeys') is not None:
            self.search_journeys_shrink = m.get('search_journeys')

        if m.get('search_passenger_list') is not None:
            self.search_passenger_list_shrink = m.get('search_passenger_list')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

