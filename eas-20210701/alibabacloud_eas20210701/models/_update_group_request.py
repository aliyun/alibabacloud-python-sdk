# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGroupRequest(DaraModel):
    def __init__(
        self,
        traffic_mode: str = None,
    ):
        # The traffic mode. Valid values: auto and customized. auto: The traffic is automatically allocated based on the proportion of the number of instances to the total number of instances. customized: The traffic is allocated based on a custom weight.
        self.traffic_mode = traffic_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic_mode is not None:
            result['TrafficMode'] = self.traffic_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficMode') is not None:
            self.traffic_mode = m.get('TrafficMode')

        return self

