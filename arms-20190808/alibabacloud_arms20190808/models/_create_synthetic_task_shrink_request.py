# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSyntheticTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        common_param_shrink: str = None,
        download_shrink: str = None,
        extend_interval_shrink: str = None,
        interval_time: str = None,
        interval_type: str = None,
        ip_type: int = None,
        monitor_list_shrink: str = None,
        navigation_shrink: str = None,
        net_shrink: str = None,
        protocol_shrink: str = None,
        region_id: str = None,
        task_name: str = None,
        task_type: int = None,
        update_task: bool = None,
        url: str = None,
    ):
        # The common parameters.
        self.common_param_shrink = common_param_shrink
        # The file download task.
        self.download_shrink = download_shrink
        # The frequency.
        self.extend_interval_shrink = extend_interval_shrink
        # The interval at which synthetic monitoring is performed. Unit: minutes. Valid values:
        # 
        # *   1
        # *   5
        # *   10
        # *   15
        # *   20
        # *   30
        # *   60
        # *   120
        # *   180
        # *   240
        # *   360
        # *   480
        # *   720
        # *   1440
        # 
        # This parameter is required.
        self.interval_time = interval_time
        # The interval type.
        # 
        # *   0: daily
        # *   1: custom frequency
        # 
        # This parameter is required.
        self.interval_type = interval_type
        # The IP address type:
        # 
        # *   0: an automatic IP address
        # *   1: IPv4
        # *   2: IPv6
        # 
        # This parameter is required.
        self.ip_type = ip_type
        # The list of monitoring points.
        # 
        # This parameter is required.
        self.monitor_list_shrink = monitor_list_shrink
        # The monitoring items that are associated with the browse tasks.
        self.navigation_shrink = navigation_shrink
        # The network synthetic monitoring task.
        self.net_shrink = net_shrink
        # The API performance synthetic monitoring task.
        self.protocol_shrink = protocol_shrink
        # The ID of the region in which the application is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the task. To update a synthetic monitoring task, enter the task name and set the **UpdateTask** parameter to **true**.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The type of the monitoring task. Valid values:
        # 
        # 1.  3: web page performance - IE
        # 2.  34: web Page Performance - Chrome
        # 3.  0: network quality
        # 4.  40: file download
        # 5.  7:API performance
        # 
        # This parameter is required.
        self.task_type = task_type
        # Specifies whether to update existing synthetic monitoring tasks.
        # 
        # *   true: updates existing synthetic monitoring tasks.
        # *   false: creates new synthetic monitoring tasks.
        self.update_task = update_task
        # The URL for synthetic monitoring.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_param_shrink is not None:
            result['CommonParam'] = self.common_param_shrink

        if self.download_shrink is not None:
            result['Download'] = self.download_shrink

        if self.extend_interval_shrink is not None:
            result['ExtendInterval'] = self.extend_interval_shrink

        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time

        if self.interval_type is not None:
            result['IntervalType'] = self.interval_type

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.monitor_list_shrink is not None:
            result['MonitorList'] = self.monitor_list_shrink

        if self.navigation_shrink is not None:
            result['Navigation'] = self.navigation_shrink

        if self.net_shrink is not None:
            result['Net'] = self.net_shrink

        if self.protocol_shrink is not None:
            result['Protocol'] = self.protocol_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.update_task is not None:
            result['UpdateTask'] = self.update_task

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonParam') is not None:
            self.common_param_shrink = m.get('CommonParam')

        if m.get('Download') is not None:
            self.download_shrink = m.get('Download')

        if m.get('ExtendInterval') is not None:
            self.extend_interval_shrink = m.get('ExtendInterval')

        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')

        if m.get('IntervalType') is not None:
            self.interval_type = m.get('IntervalType')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('MonitorList') is not None:
            self.monitor_list_shrink = m.get('MonitorList')

        if m.get('Navigation') is not None:
            self.navigation_shrink = m.get('Navigation')

        if m.get('Net') is not None:
            self.net_shrink = m.get('Net')

        if m.get('Protocol') is not None:
            self.protocol_shrink = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTask') is not None:
            self.update_task = m.get('UpdateTask')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

