# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobMetricsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        metric_type: str = None,
        start_time: str = None,
        time_step: str = None,
        token: str = None,
    ):
        # The end time of the time range for querying monitoring data, in UTC. Default value: the current time.
        self.end_time = end_time
        # The metric type of the monitoring data to query. Valid values:
        # - GpuCoreUsage: the GPU usage
        # - GpuMemoryUsage: the GPU memory usage
        # - CpuCoreUsage: the CPU usage
        # - MemoryUsage: the memory usage
        # - NetworkInputRate: the network input rate
        # - NetworkOutputRate: the network output rate
        # - DiskReadRate: the disk read rate
        # - DiskWriteRate: the disk write rate
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The start time of the time range for querying monitoring data, in UTC. Default value: 1 hour ago.
        self.start_time = start_time
        # The time interval at which monitoring data is returned. Default value: 5 minutes.
        self.time_step = time_step
        # The temporary token used for authentication.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_step is not None:
            result['TimeStep'] = self.time_step

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

