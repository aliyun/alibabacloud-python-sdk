# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransitVisaShrinkRequest(DaraModel):
    def __init__(
        self,
        flight_segment_param_list_shrink: str = None,
    ):
        # The list of flight segments that constitute an itinerary. Maximum size: 2.
        self.flight_segment_param_list_shrink = flight_segment_param_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flight_segment_param_list_shrink is not None:
            result['flight_segment_param_list'] = self.flight_segment_param_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flight_segment_param_list') is not None:
            self.flight_segment_param_list_shrink = m.get('flight_segment_param_list')

        return self

