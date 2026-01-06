# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEventStreamingBusinessOptionRequest(DaraModel):
    def __init__(
        self,
        business_mode: str = None,
        event_streaming_name: str = None,
        max_capacity_unit_count: int = None,
        min_capacity_unit_count: int = None,
    ):
        # This parameter is required.
        self.business_mode = business_mode
        # This parameter is required.
        self.event_streaming_name = event_streaming_name
        self.max_capacity_unit_count = max_capacity_unit_count
        self.min_capacity_unit_count = min_capacity_unit_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_mode is not None:
            result['BusinessMode'] = self.business_mode

        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name

        if self.max_capacity_unit_count is not None:
            result['MaxCapacityUnitCount'] = self.max_capacity_unit_count

        if self.min_capacity_unit_count is not None:
            result['MinCapacityUnitCount'] = self.min_capacity_unit_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessMode') is not None:
            self.business_mode = m.get('BusinessMode')

        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')

        if m.get('MaxCapacityUnitCount') is not None:
            self.max_capacity_unit_count = m.get('MaxCapacityUnitCount')

        if m.get('MinCapacityUnitCount') is not None:
            self.min_capacity_unit_count = m.get('MinCapacityUnitCount')

        return self

