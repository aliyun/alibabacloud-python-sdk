# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGpuClusterListAlarmRecordRequest(DaraModel):
    def __init__(
        self,
        alarm_cluster: str = None,
        alarm_ext_info: str = None,
        alarm_task: str = None,
        alarm_time: str = None,
        alarm_type: str = None,
        current: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The cluster to query. Specify a cluster, such as "cluster1". To query multiple clusters, separate them with commas, such as "cluster1,cluster2,cluster3".
        self.alarm_cluster = alarm_cluster
        # The instance ID or container used to filter anomalies.
        self.alarm_ext_info = alarm_ext_info
        # The task to query. Specify a task, such as "task1". To query multiple tasks, separate them with commas, such as "task1,task2,task3".
        self.alarm_task = alarm_task
        # The specific time or time range to query. Specify a specific time, such as "2025-08-22 18:16:25". To specify a time range, use the "start,end" format, such as "2025-08-22 18:16:25,2025-08-23 18:16:25".
        self.alarm_time = alarm_time
        # The anomaly type used to filter results, such as GPU memory access out of bounds or task hang.
        self.alarm_type = alarm_type
        # The current page number for pagination.
        # 
        # This parameter is required.
        self.current = current
        # The number of entries per page for pagination.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The task status used to filter results. Valid values: blocking, running, exited, and restart.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_cluster is not None:
            result['alarmCluster'] = self.alarm_cluster

        if self.alarm_ext_info is not None:
            result['alarmExtInfo'] = self.alarm_ext_info

        if self.alarm_task is not None:
            result['alarmTask'] = self.alarm_task

        if self.alarm_time is not None:
            result['alarmTime'] = self.alarm_time

        if self.alarm_type is not None:
            result['alarmType'] = self.alarm_type

        if self.current is not None:
            result['current'] = self.current

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmCluster') is not None:
            self.alarm_cluster = m.get('alarmCluster')

        if m.get('alarmExtInfo') is not None:
            self.alarm_ext_info = m.get('alarmExtInfo')

        if m.get('alarmTask') is not None:
            self.alarm_task = m.get('alarmTask')

        if m.get('alarmTime') is not None:
            self.alarm_time = m.get('alarmTime')

        if m.get('alarmType') is not None:
            self.alarm_type = m.get('alarmType')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

