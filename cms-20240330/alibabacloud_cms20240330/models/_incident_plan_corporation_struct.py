# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IncidentPlanCorporationStruct(DaraModel):
    def __init__(
        self,
        channel: str = None,
        robot_id: str = None,
    ):
        self.channel = channel
        self.robot_id = robot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.robot_id is not None:
            result['robotId'] = self.robot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('robotId') is not None:
            self.robot_id = m.get('robotId')

        return self

