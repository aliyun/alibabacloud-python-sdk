# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TunnelQos(DaraModel):
    def __init__(
        self,
        max_bandwidth: int = None,
        max_qps: int = None,
    ):
        self.max_bandwidth = max_bandwidth
        self.max_qps = max_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth

        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')

        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')

        return self

