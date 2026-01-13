# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrafficControlTaskTrafficInfoTargetTrafficsDataValue(DaraModel):
    def __init__(
        self,
        traffic: float = None,
        recorf_time: int = None,
    ):
        self.traffic = traffic
        self.recorf_time = recorf_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic is not None:
            result['Traffic'] = self.traffic

        if self.recorf_time is not None:
            result['RecorfTime'] = self.recorf_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')

        if m.get('RecorfTime') is not None:
            self.recorf_time = m.get('RecorfTime')

        return self

