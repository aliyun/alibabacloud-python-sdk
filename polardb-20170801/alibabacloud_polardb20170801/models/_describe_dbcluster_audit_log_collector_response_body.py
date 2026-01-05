# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterAuditLogCollectorResponseBody(DaraModel):
    def __init__(
        self,
        collector_status: str = None,
        request_id: str = None,
    ):
        # The status of SQL collector. Valid values:
        # 
        # *   Enable
        # *   Disabled
        self.collector_status = collector_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collector_status is not None:
            result['CollectorStatus'] = self.collector_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectorStatus') is not None:
            self.collector_status = m.get('CollectorStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

