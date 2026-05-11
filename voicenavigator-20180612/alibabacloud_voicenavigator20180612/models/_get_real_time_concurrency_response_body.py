# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRealTimeConcurrencyResponseBody(DaraModel):
    def __init__(
        self,
        max_concurrency: int = None,
        real_time_concurrency: int = None,
        request_id: str = None,
        timestamp: int = None,
    ):
        self.max_concurrency = max_concurrency
        self.real_time_concurrency = real_time_concurrency
        self.request_id = request_id
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.real_time_concurrency is not None:
            result['RealTimeConcurrency'] = self.real_time_concurrency

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('RealTimeConcurrency') is not None:
            self.real_time_concurrency = m.get('RealTimeConcurrency')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

