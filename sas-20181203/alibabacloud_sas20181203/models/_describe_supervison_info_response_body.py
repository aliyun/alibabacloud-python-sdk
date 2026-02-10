# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSupervisonInfoResponseBody(DaraModel):
    def __init__(
        self,
        latest_scan_time: int = None,
        request_id: str = None,
    ):
        # The time of the last system vulnerability scan. The value is a UNIX timestamp. Unit: milliseconds.
        self.latest_scan_time = latest_scan_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest_scan_time is not None:
            result['LatestScanTime'] = self.latest_scan_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestScanTime') is not None:
            self.latest_scan_time = m.get('LatestScanTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

