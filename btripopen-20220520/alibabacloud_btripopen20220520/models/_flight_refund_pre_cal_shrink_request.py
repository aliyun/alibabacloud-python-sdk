# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightRefundPreCalShrinkRequest(DaraModel):
    def __init__(
        self,
        dis_order_id: str = None,
        is_voluntary: str = None,
        passenger_segment_info_list_shrink: str = None,
    ):
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.is_voluntary = is_voluntary
        # This parameter is required.
        self.passenger_segment_info_list_shrink = passenger_segment_info_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        if self.passenger_segment_info_list_shrink is not None:
            result['passenger_segment_info_list'] = self.passenger_segment_info_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        if m.get('passenger_segment_info_list') is not None:
            self.passenger_segment_info_list_shrink = m.get('passenger_segment_info_list')

        return self

