# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSwimmingLaneRequest(DaraModel):
    def __init__(
        self,
        lane_id: int = None,
    ):
        # The ID of the lane.
        # 
        # This parameter is required.
        self.lane_id = lane_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        return self

