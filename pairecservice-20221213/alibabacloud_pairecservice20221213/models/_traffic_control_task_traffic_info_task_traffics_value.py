# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrafficControlTaskTrafficInfoTaskTrafficsValue(DaraModel):
    def __init__(
        self,
        traffic: float = None,
    ):
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic is not None:
            result['Traffic'] = self.traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')

        return self

