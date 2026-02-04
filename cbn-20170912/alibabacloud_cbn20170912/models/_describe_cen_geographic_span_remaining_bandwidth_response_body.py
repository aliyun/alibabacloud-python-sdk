# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCenGeographicSpanRemainingBandwidthResponseBody(DaraModel):
    def __init__(
        self,
        remaining_bandwidth: int = None,
        request_id: str = None,
    ):
        # The remaining bandwidth of the bandwidth plan. Unit: Mbit/s.
        self.remaining_bandwidth = remaining_bandwidth
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remaining_bandwidth is not None:
            result['RemainingBandwidth'] = self.remaining_bandwidth

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemainingBandwidth') is not None:
            self.remaining_bandwidth = m.get('RemainingBandwidth')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

