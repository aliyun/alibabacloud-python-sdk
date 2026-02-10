# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppVulScanCycleResponseBody(DaraModel):
    def __init__(
        self,
        cycle: str = None,
        request_id: str = None,
    ):
        # The scan cycle for application vulnerabilities.
        # 
        # *   1week
        # *   2weeks
        # *   3days
        self.cycle = cycle
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

