# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDdosMaxBurstGbpsResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_burst_gbps: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.max_burst_gbps = max_burst_gbps
        # Id of the request
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxBurstGbps') is not None:
            self.max_burst_gbps = m.get('MaxBurstGbps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

