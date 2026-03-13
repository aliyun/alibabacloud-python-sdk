# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightModifyListingSearchV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        cabin_class_shrink: str = None,
        dep_date_shrink: str = None,
        interface_caller_is_support_retry: bool = None,
        isv_name: str = None,
        order_id: int = None,
        out_order_id: str = None,
        passenger_segment_relations_shrink: str = None,
        search_mode: int = None,
        search_retry_token: str = None,
        selected_segments_shrink: str = None,
        session_id: str = None,
        voluntary: bool = None,
    ):
        self.cabin_class_shrink = cabin_class_shrink
        self.dep_date_shrink = dep_date_shrink
        self.interface_caller_is_support_retry = interface_caller_is_support_retry
        self.isv_name = isv_name
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.passenger_segment_relations_shrink = passenger_segment_relations_shrink
        self.search_mode = search_mode
        self.search_retry_token = search_retry_token
        self.selected_segments_shrink = selected_segments_shrink
        self.session_id = session_id
        self.voluntary = voluntary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin_class_shrink is not None:
            result['cabin_class'] = self.cabin_class_shrink

        if self.dep_date_shrink is not None:
            result['dep_date'] = self.dep_date_shrink

        if self.interface_caller_is_support_retry is not None:
            result['interface_caller_is_support_retry'] = self.interface_caller_is_support_retry

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.passenger_segment_relations_shrink is not None:
            result['passenger_segment_relations'] = self.passenger_segment_relations_shrink

        if self.search_mode is not None:
            result['search_mode'] = self.search_mode

        if self.search_retry_token is not None:
            result['search_retry_token'] = self.search_retry_token

        if self.selected_segments_shrink is not None:
            result['selected_segments'] = self.selected_segments_shrink

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.voluntary is not None:
            result['voluntary'] = self.voluntary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin_class') is not None:
            self.cabin_class_shrink = m.get('cabin_class')

        if m.get('dep_date') is not None:
            self.dep_date_shrink = m.get('dep_date')

        if m.get('interface_caller_is_support_retry') is not None:
            self.interface_caller_is_support_retry = m.get('interface_caller_is_support_retry')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('passenger_segment_relations') is not None:
            self.passenger_segment_relations_shrink = m.get('passenger_segment_relations')

        if m.get('search_mode') is not None:
            self.search_mode = m.get('search_mode')

        if m.get('search_retry_token') is not None:
            self.search_retry_token = m.get('search_retry_token')

        if m.get('selected_segments') is not None:
            self.selected_segments_shrink = m.get('selected_segments')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('voluntary') is not None:
            self.voluntary = m.get('voluntary')

        return self

