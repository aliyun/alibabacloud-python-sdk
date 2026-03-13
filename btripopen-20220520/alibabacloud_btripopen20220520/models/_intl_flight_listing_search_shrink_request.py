# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightListingSearchShrinkRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        buyer_name: str = None,
        cabin_type: int = None,
        isv_name: str = None,
        out_wheel_search: bool = None,
        query_record_id: str = None,
        search_journeys_shrink: str = None,
        search_mode: int = None,
        search_passenger_list_shrink: str = None,
        token: str = None,
        trip_type: int = None,
    ):
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        # This parameter is required.
        self.cabin_type = cabin_type
        # This parameter is required.
        self.isv_name = isv_name
        # This parameter is required.
        self.out_wheel_search = out_wheel_search
        self.query_record_id = query_record_id
        # This parameter is required.
        self.search_journeys_shrink = search_journeys_shrink
        # This parameter is required.
        self.search_mode = search_mode
        self.search_passenger_list_shrink = search_passenger_list_shrink
        self.token = token
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

        if self.out_wheel_search is not None:
            result['out_wheel_search'] = self.out_wheel_search

        if self.query_record_id is not None:
            result['query_record_id'] = self.query_record_id

        if self.search_journeys_shrink is not None:
            result['search_journeys'] = self.search_journeys_shrink

        if self.search_mode is not None:
            result['search_mode'] = self.search_mode

        if self.search_passenger_list_shrink is not None:
            result['search_passenger_list'] = self.search_passenger_list_shrink

        if self.token is not None:
            result['token'] = self.token

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

        if m.get('out_wheel_search') is not None:
            self.out_wheel_search = m.get('out_wheel_search')

        if m.get('query_record_id') is not None:
            self.query_record_id = m.get('query_record_id')

        if m.get('search_journeys') is not None:
            self.search_journeys_shrink = m.get('search_journeys')

        if m.get('search_mode') is not None:
            self.search_mode = m.get('search_mode')

        if m.get('search_passenger_list') is not None:
            self.search_passenger_list_shrink = m.get('search_passenger_list')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

