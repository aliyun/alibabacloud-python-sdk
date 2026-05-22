# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeEdgeContainerAppStatsResponseBody(DaraModel):
    def __init__(
        self,
        cpu_usage_seconds_quota_rate_avg: float = None,
        cpu_usage_seconds_total_avg: float = None,
        fs_reads_bytes_avg_avg: float = None,
        fs_writes_bytes_avg_avg: float = None,
        memory_rss_avg: float = None,
        memory_rss_quota_rate_avg: float = None,
        pod_ready_rate_avg: float = None,
        points: List[main_models.DescribeEdgeContainerAppStatsResponseBodyPoints] = None,
        request_id: str = None,
    ):
        # Average CPU limit ratio
        self.cpu_usage_seconds_quota_rate_avg = cpu_usage_seconds_quota_rate_avg
        # Average number of CPU cores
        self.cpu_usage_seconds_total_avg = cpu_usage_seconds_total_avg
        # Average read IO
        self.fs_reads_bytes_avg_avg = fs_reads_bytes_avg_avg
        # Average write IO
        self.fs_writes_bytes_avg_avg = fs_writes_bytes_avg_avg
        # Average memory usage
        self.memory_rss_avg = memory_rss_avg
        # Average memory limit proportion
        self.memory_rss_quota_rate_avg = memory_rss_quota_rate_avg
        # Average PodReady rate
        self.pod_ready_rate_avg = pod_ready_rate_avg
        self.points = points
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.points:
            for v1 in self.points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_usage_seconds_quota_rate_avg is not None:
            result['CpuUsageSecondsQuotaRateAvg'] = self.cpu_usage_seconds_quota_rate_avg

        if self.cpu_usage_seconds_total_avg is not None:
            result['CpuUsageSecondsTotalAvg'] = self.cpu_usage_seconds_total_avg

        if self.fs_reads_bytes_avg_avg is not None:
            result['FsReadsBytesAvgAvg'] = self.fs_reads_bytes_avg_avg

        if self.fs_writes_bytes_avg_avg is not None:
            result['FsWritesBytesAvgAvg'] = self.fs_writes_bytes_avg_avg

        if self.memory_rss_avg is not None:
            result['MemoryRssAvg'] = self.memory_rss_avg

        if self.memory_rss_quota_rate_avg is not None:
            result['MemoryRssQuotaRateAvg'] = self.memory_rss_quota_rate_avg

        if self.pod_ready_rate_avg is not None:
            result['PodReadyRateAvg'] = self.pod_ready_rate_avg

        result['Points'] = []
        if self.points is not None:
            for k1 in self.points:
                result['Points'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuUsageSecondsQuotaRateAvg') is not None:
            self.cpu_usage_seconds_quota_rate_avg = m.get('CpuUsageSecondsQuotaRateAvg')

        if m.get('CpuUsageSecondsTotalAvg') is not None:
            self.cpu_usage_seconds_total_avg = m.get('CpuUsageSecondsTotalAvg')

        if m.get('FsReadsBytesAvgAvg') is not None:
            self.fs_reads_bytes_avg_avg = m.get('FsReadsBytesAvgAvg')

        if m.get('FsWritesBytesAvgAvg') is not None:
            self.fs_writes_bytes_avg_avg = m.get('FsWritesBytesAvgAvg')

        if m.get('MemoryRssAvg') is not None:
            self.memory_rss_avg = m.get('MemoryRssAvg')

        if m.get('MemoryRssQuotaRateAvg') is not None:
            self.memory_rss_quota_rate_avg = m.get('MemoryRssQuotaRateAvg')

        if m.get('PodReadyRateAvg') is not None:
            self.pod_ready_rate_avg = m.get('PodReadyRateAvg')

        self.points = []
        if m.get('Points') is not None:
            for k1 in m.get('Points'):
                temp_model = main_models.DescribeEdgeContainerAppStatsResponseBodyPoints()
                self.points.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEdgeContainerAppStatsResponseBodyPoints(DaraModel):
    def __init__(
        self,
        container_cpu_usage_seconds_quota_rate: float = None,
        container_cpu_usage_seconds_total: float = None,
        container_fs_reads_bytes_avg: float = None,
        container_fs_writes_bytes_avg: float = None,
        container_memory_rss: float = None,
        container_memory_rss_quota_rate: float = None,
        pod_ready_rate: float = None,
        time: str = None,
    ):
        self.container_cpu_usage_seconds_quota_rate = container_cpu_usage_seconds_quota_rate
        self.container_cpu_usage_seconds_total = container_cpu_usage_seconds_total
        self.container_fs_reads_bytes_avg = container_fs_reads_bytes_avg
        self.container_fs_writes_bytes_avg = container_fs_writes_bytes_avg
        self.container_memory_rss = container_memory_rss
        self.container_memory_rss_quota_rate = container_memory_rss_quota_rate
        self.pod_ready_rate = pod_ready_rate
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_cpu_usage_seconds_quota_rate is not None:
            result['ContainerCpuUsageSecondsQuotaRate'] = self.container_cpu_usage_seconds_quota_rate

        if self.container_cpu_usage_seconds_total is not None:
            result['ContainerCpuUsageSecondsTotal'] = self.container_cpu_usage_seconds_total

        if self.container_fs_reads_bytes_avg is not None:
            result['ContainerFsReadsBytesAvg'] = self.container_fs_reads_bytes_avg

        if self.container_fs_writes_bytes_avg is not None:
            result['ContainerFsWritesBytesAvg'] = self.container_fs_writes_bytes_avg

        if self.container_memory_rss is not None:
            result['ContainerMemoryRss'] = self.container_memory_rss

        if self.container_memory_rss_quota_rate is not None:
            result['ContainerMemoryRssQuotaRate'] = self.container_memory_rss_quota_rate

        if self.pod_ready_rate is not None:
            result['PodReadyRate'] = self.pod_ready_rate

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerCpuUsageSecondsQuotaRate') is not None:
            self.container_cpu_usage_seconds_quota_rate = m.get('ContainerCpuUsageSecondsQuotaRate')

        if m.get('ContainerCpuUsageSecondsTotal') is not None:
            self.container_cpu_usage_seconds_total = m.get('ContainerCpuUsageSecondsTotal')

        if m.get('ContainerFsReadsBytesAvg') is not None:
            self.container_fs_reads_bytes_avg = m.get('ContainerFsReadsBytesAvg')

        if m.get('ContainerFsWritesBytesAvg') is not None:
            self.container_fs_writes_bytes_avg = m.get('ContainerFsWritesBytesAvg')

        if m.get('ContainerMemoryRss') is not None:
            self.container_memory_rss = m.get('ContainerMemoryRss')

        if m.get('ContainerMemoryRssQuotaRate') is not None:
            self.container_memory_rss_quota_rate = m.get('ContainerMemoryRssQuotaRate')

        if m.get('PodReadyRate') is not None:
            self.pod_ready_rate = m.get('PodReadyRate')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

