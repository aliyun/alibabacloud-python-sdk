# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddOrQuitLaneCmd(DaraModel):
    def __init__(
        self,
        lane_ids: str = None,
        operate_type: str = None,
        service_group_id: int = None,
    ):
        # This parameter is required.
        self.lane_ids = lane_ids
        # This parameter is required.
        self.operate_type = operate_type
        # This parameter is required.
        self.service_group_id = service_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lane_ids is not None:
            result['laneIds'] = self.lane_ids

        if self.operate_type is not None:
            result['operateType'] = self.operate_type

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('laneIds') is not None:
            self.lane_ids = m.get('laneIds')

        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        return self

