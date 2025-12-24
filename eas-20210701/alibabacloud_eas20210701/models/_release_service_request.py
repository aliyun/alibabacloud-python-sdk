# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseServiceRequest(DaraModel):
    def __init__(
        self,
        traffic_state: str = None,
        weight: int = None,
    ):
        # The traffic state. Valid values:
        # 
        # *   standalone: independent traffic.
        # *   grouping: grouped traffic.
        self.traffic_state = traffic_state
        # The weight of the service. Valid values: [-1, 1000].
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic_state is not None:
            result['TrafficState'] = self.traffic_state

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficState') is not None:
            self.traffic_state = m.get('TrafficState')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

