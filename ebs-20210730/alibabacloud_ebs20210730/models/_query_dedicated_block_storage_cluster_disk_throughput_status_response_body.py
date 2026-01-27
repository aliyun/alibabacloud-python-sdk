# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDedicatedBlockStorageClusterDiskThroughputStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of the throughput after setting the throughput by SetDedicatedBlockStorageClusterDiskThroughput api.
        # 
        # - SUCCESS: The throughput has been successfully set.
        # - RUNNING: The throughput is currently being set.
        # - WAIT(): The throughput is waiting to be set.
        # - FAIL(): The throughput setting has failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

