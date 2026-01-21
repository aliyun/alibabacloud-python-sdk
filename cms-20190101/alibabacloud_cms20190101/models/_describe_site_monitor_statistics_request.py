# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteMonitorStatisticsRequest(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        region_id: str = None,
        start_time: str = None,
        task_id: str = None,
        time_range: str = None,
    ):
        # The metric name. Valid values:
        # 
        # *   Availability
        # *   ErrorRate
        # *   ResponseTime
        # 
        # This parameter is required.
        self.metric_name = metric_name
        self.region_id = region_id
        # The beginning of the time range to query.
        # 
        # Unit: milliseconds. The default value is 1 hour ahead of the current time.
        self.start_time = start_time
        # The ID of the site monitoring task.
        # 
        # For more information about how to obtain the ID of a site monitoring task, see [DescribeSiteMonitorList](https://help.aliyun.com/document_detail/115052.html).
        # 
        # This parameter is required.
        self.task_id = task_id
        # The statistical period.
        # 
        # Unit: minutes. Default value: 1440 (one day). Maximum value: 43200 (30 days).
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

