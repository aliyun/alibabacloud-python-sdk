# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDdosMaxBurstGbpsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_burst_gbps: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.max_burst_gbps = max_burst_gbps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_burst_gbps is not None:
            result['MaxBurstGbps'] = self.max_burst_gbps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxBurstGbps') is not None:
            self.max_burst_gbps = m.get('MaxBurstGbps')

        return self

