# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudBasicMonitorResponseBody(DaraModel):
    def __init__(
        self,
        basic_monitors: List[main_models.DescribeHybridCloudBasicMonitorResponseBodyBasicMonitors] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The basic metrics.
        self.basic_monitors = basic_monitors
        # The ID of the request.
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.basic_monitors:
            for v1 in self.basic_monitors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BasicMonitors'] = []
        if self.basic_monitors is not None:
            for k1 in self.basic_monitors:
                result['BasicMonitors'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.basic_monitors = []
        if m.get('BasicMonitors') is not None:
            for k1 in m.get('BasicMonitors'):
                temp_model = main_models.DescribeHybridCloudBasicMonitorResponseBodyBasicMonitors()
                self.basic_monitors.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHybridCloudBasicMonitorResponseBodyBasicMonitors(DaraModel):
    def __init__(
        self,
        levle: str = None,
        monitor_name: str = None,
        use_ratio: int = None,
    ):
        self.levle = levle
        # The metric. Valid values:
        # 
        # *   **basic_monitor_cpu_usage**: the CPU.
        # *   **basic_monitor_memory_usage**: the memory.
        # *   **basic_monitor_disk_usage**: the disk.
        self.monitor_name = monitor_name
        # The resource usage.
        self.use_ratio = use_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.levle is not None:
            result['Levle'] = self.levle

        if self.monitor_name is not None:
            result['MonitorName'] = self.monitor_name

        if self.use_ratio is not None:
            result['UseRatio'] = self.use_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Levle') is not None:
            self.levle = m.get('Levle')

        if m.get('MonitorName') is not None:
            self.monitor_name = m.get('MonitorName')

        if m.get('UseRatio') is not None:
            self.use_ratio = m.get('UseRatio')

        return self

