# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePortAttackMaxFlowResponseBody(DaraModel):
    def __init__(
        self,
        bps: int = None,
        pps: int = None,
        request_id: str = None,
    ):
        # The peak bandwidth of attack traffic. Unit: bit/s.
        self.bps = bps
        # The peak packet rate of attack traffic . Unit: packets per second (pps).
        self.pps = pps
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

