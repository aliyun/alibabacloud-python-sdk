# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryMonitorValuesResponseBody(DaraModel):
    def __init__(
        self,
        monitor_history: str = None,
        request_id: str = None,
    ):
        # The monitoring data returned as a JSON-formatted string. For more information, see [Monitoring parameters](https://help.aliyun.com/document_detail/122091.html).
        # 
        # > To improve data transfer efficiency, the system returns only monitoring data for metrics with non-zero values. If a metric is not returned, its value is **0**.
        self.monitor_history = monitor_history
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_history is not None:
            result['MonitorHistory'] = self.monitor_history

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorHistory') is not None:
            self.monitor_history = m.get('MonitorHistory')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

