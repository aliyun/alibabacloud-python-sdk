# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDosEventMaxResponseBody(DaraModel):
    def __init__(
        self,
        cps: int = None,
        mbps: int = None,
        qps: int = None,
        request_id: str = None,
    ):
        # The peak of connection flood attacks. Unit: connections per seconds (CPS).
        self.cps = cps
        # The peak of volumetric attacks. Unit: Mbit/s.
        self.mbps = mbps
        # The peak of resource exhaustion attacks. Unit: queries per second (QPS).
        self.qps = qps
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cps is not None:
            result['Cps'] = self.cps

        if self.mbps is not None:
            result['Mbps'] = self.mbps

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

