# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIpsetsBandwidthLimitResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_allocation_type: str = None,
        bandwidth_limit: int = None,
        request_id: str = None,
    ):
        # The type of the bandwidth that is allocated.
        # 
        # *   **ShareBandwidth:** shared bandwidth.
        # *   **ExclusiveBandwidth:** dedicated bandwidth.
        self.bandwidth_allocation_type = bandwidth_allocation_type
        # The maximum bandwidth of the acceleration area. Unit: Mbit/s.
        self.bandwidth_limit = bandwidth_limit
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_allocation_type is not None:
            result['BandwidthAllocationType'] = self.bandwidth_allocation_type

        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthAllocationType') is not None:
            self.bandwidth_allocation_type = m.get('BandwidthAllocationType')

        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

