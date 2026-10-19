# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryMonitorValuesResponseBody(DaraModel):
    def __init__(
        self,
        monitor_history: str = None,
        monitor_legend: str = None,
        request_id: str = None,
    ):
        # The monitoring information returned in JSON format. For more information, see [Monitoring parameter description](https://help.aliyun.com/document_detail/122091.html).
        # 
        # > To improve data transmission efficiency, only non-zero monitoring data is returned. All other monitoring data that is not displayed has a default value of **0**.
        self.monitor_history = monitor_history
        self.monitor_legend = monitor_legend
        # The request ID.
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

        if self.monitor_legend is not None:
            result['MonitorLegend'] = self.monitor_legend

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorHistory') is not None:
            self.monitor_history = m.get('MonitorHistory')

        if m.get('MonitorLegend') is not None:
            self.monitor_legend = m.get('MonitorLegend')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

